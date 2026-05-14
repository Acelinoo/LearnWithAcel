import { z } from "zod";

export const loginSchema = z.object({
  email: z
    .string()
    .min(1, "Email wajib diisi")
    .email("Format email tidak valid"),
  password: z
    .string()
    .min(1, "Password wajib diisi")
    .min(6, "Password minimal 6 karakter"),
  remember: z.boolean().optional(),
});

export const registerSchema = z
  .object({
    username: z
      .string()
      .min(1, "Username wajib diisi")
      .min(3, "Username minimal 3 karakter")
      .max(24, "Username maksimal 24 karakter")
      .regex(
        /^[a-zA-Z0-9_.]+$/,
        "Hanya huruf, angka, titik, dan underscore yang diizinkan"
      ),
    email: z
      .string()
      .min(1, "Email wajib diisi")
      .email("Format email tidak valid"),
    password: z
      .string()
      .min(8, "Password minimal 8 karakter")
      .regex(/[A-Za-z]/, "Password harus mengandung huruf")
      .regex(/\d/, "Password harus mengandung angka"),
    confirmPassword: z.string().min(1, "Konfirmasi password wajib diisi"),
  })
  .refine((data) => data.password === data.confirmPassword, {
    path: ["confirmPassword"],
    message: "Konfirmasi password tidak cocok",
  });

export type LoginInput = z.infer<typeof loginSchema>;
export type RegisterInput = z.infer<typeof registerSchema>;
