"""
Email sending utility using fastapi-mail.

Provides a single send_reset_password_email() helper used by the
forgot-password flow. The mailer is lazily initialised so the app
still starts even when SMTP credentials are not configured (useful
for local development — the reset link is logged to stdout instead).
"""

import logging

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType

from app.core.config import settings

logger = logging.getLogger(__name__)

# ── Mail connection config ────────────────────────────────────────────────────
_mail_config = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=bool(settings.MAIL_USERNAME),
    VALIDATE_CERTS=True,
)

_mailer = FastMail(_mail_config)


# ── Email templates ───────────────────────────────────────────────────────────
def _reset_password_html(full_name: str, reset_url: str, expires_minutes: int) -> str:
    return f"""
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Reset Password — LearnWithAcel</title>
</head>
<body style="margin:0;padding:0;background:#0d0d0d;font-family:system-ui,sans-serif;color:#f5f5f5;">
  <table width="100%" cellpadding="0" cellspacing="0" style="padding:40px 0;">
    <tr>
      <td align="center">
        <table width="560" cellpadding="0" cellspacing="0"
               style="background:#1c1c1c;border-radius:16px;padding:40px;border:1px solid #262626;">

          <!-- Logo / brand -->
          <tr>
            <td style="padding-bottom:32px;">
              <span style="font-size:22px;font-weight:700;color:#8b5cf6;">LearnWithAcel</span>
            </td>
          </tr>

          <!-- Greeting -->
          <tr>
            <td style="padding-bottom:16px;">
              <h1 style="margin:0;font-size:24px;font-weight:700;color:#f5f5f5;">
                Reset Password Kamu
              </h1>
            </td>
          </tr>

          <!-- Body -->
          <tr>
            <td style="padding-bottom:32px;line-height:1.7;color:#a3a3a3;font-size:15px;">
              <p style="margin:0 0 12px;">Halo <strong style="color:#f5f5f5;">{full_name}</strong>,</p>
              <p style="margin:0 0 12px;">
                Kami menerima permintaan untuk mereset password akun LearnWithAcel kamu.
                Klik tombol di bawah untuk membuat password baru.
              </p>
              <p style="margin:0;">
                Link ini hanya berlaku selama
                <strong style="color:#f5f5f5;">{expires_minutes} menit</strong>.
                Jika kamu tidak meminta reset password, abaikan email ini — akunmu aman.
              </p>
            </td>
          </tr>

          <!-- CTA button -->
          <tr>
            <td style="padding-bottom:32px;" align="center">
              <a href="{reset_url}"
                 style="display:inline-block;background:#8b5cf6;color:#ffffff;
                        text-decoration:none;font-weight:600;font-size:15px;
                        padding:14px 32px;border-radius:10px;">
                Reset Password
              </a>
            </td>
          </tr>

          <!-- Fallback URL -->
          <tr>
            <td style="padding-bottom:32px;">
              <p style="margin:0;font-size:13px;color:#737373;">
                Tombol tidak berfungsi? Salin link berikut ke browser kamu:
              </p>
              <p style="margin:8px 0 0;font-size:13px;word-break:break-all;">
                <a href="{reset_url}" style="color:#8b5cf6;">{reset_url}</a>
              </p>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="border-top:1px solid #262626;padding-top:24px;">
              <p style="margin:0;font-size:12px;color:#525252;">
                Email ini dikirim secara otomatis. Jangan balas email ini.
                &copy; 2025 LearnWithAcel
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""


# ── Public helper ─────────────────────────────────────────────────────────────
async def send_reset_password_email(
    to_email: str,
    full_name: str,
    reset_token: str,
) -> None:
    """
    Send a password-reset email to the user.

    The reset URL is built from FRONTEND_RESET_PASSWORD_URL + ?token=<token>.

    If MAIL_USERNAME is not configured (local dev), the reset URL is printed
    to stdout instead of sending a real email so development stays frictionless.
    """
    reset_url = f"{settings.FRONTEND_RESET_PASSWORD_URL}?token={reset_token}"

    if not settings.MAIL_USERNAME:
        # Dev mode: print to console instead of sending
        logger.warning(
            "MAIL_USERNAME not set — skipping email send.\n"
            "  → Reset URL: %s",
            reset_url,
        )
        return

    message = MessageSchema(
        subject="Reset Password LearnWithAcel",
        recipients=[to_email],
        body=_reset_password_html(
            full_name=full_name,
            reset_url=reset_url,
            expires_minutes=settings.RESET_TOKEN_EXPIRE_MINUTES,
        ),
        subtype=MessageType.html,
    )

    await _mailer.send_message(message)
    logger.info("Password reset email sent to %s", to_email)
