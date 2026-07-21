/**
 * Map raw backend / network auth errors to friendly Indonesian messages.
 */
export function friendlyAuthError(message?: string | null): string {
  if (!message) return "Terjadi kesalahan. Coba lagi.";
  const m = message.toLowerCase();

  if (
    m.includes("invalid email or password") ||
    m.includes("invalid login credentials") ||
    m.includes("incorrect password")
  )
    return "Email atau password salah.";
  if (
    m.includes("email is already registered") ||
    m.includes("user already registered") ||
    m.includes("already registered") ||
    m.includes("already exists")
  )
    return "Email ini sudah terdaftar. Silakan login.";
  if (m.includes("password") && m.includes("at least"))
    return "Password terlalu pendek (minimal 8 karakter).";
  if (m.includes("rate limit") || m.includes("too many"))
    return "Terlalu banyak percobaan. Coba lagi beberapa saat.";
  if (
    m.includes("failed to fetch") ||
    m.includes("network") ||
    m.includes("networkerror")
  )
    return "Tidak bisa terhubung ke server. Pastikan backend berjalan.";
  if (m.includes("token has expired") || m.includes("invalid token"))
    return "Sesi kamu sudah berakhir. Silakan login ulang.";
  return message;
}
