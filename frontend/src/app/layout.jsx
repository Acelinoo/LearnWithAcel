import "./globals.css";
import { Inter, Plus_Jakarta_Sans, JetBrains_Mono } from "next/font/google";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import { AuthProvider } from "@/components/providers/AuthProvider";
import { getServerUser } from "@/lib/api/server";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

const jakarta = Plus_Jakarta_Sans({
  subsets: ["latin"],
  variable: "--font-jakarta",
  display: "swap",
});

const mono = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-mono",
  display: "swap",
});

export const metadata = {
  metadataBase: new URL("https://learnwithacel.dev"),
  title: {
    default: "Learn With Acel — Belajar Web Development Dari Nol",
    template: "%s — Learn With Acel",
  },
  description:
    "Platform belajar web development modern untuk pemula. Roadmap terstruktur, materi mudah dipahami, dan level progression dari nol hingga siap membuat project nyata.",
  keywords: [
    "belajar web development",
    "frontend developer indonesia",
    "roadmap frontend",
    "belajar react",
    "belajar javascript",
    "learn with acel",
  ],
  authors: [{ name: "Acel" }],
  openGraph: {
    title: "Learn With Acel — Belajar Web Development Dari Nol",
    description: "From Beginner to Real Developer.",
    type: "website",
    locale: "id_ID",
  },
  twitter: {
    card: "summary_large_image",
    title: "Learn With Acel",
    description: "Belajar Web Development Dari Nol.",
  },
};

export const viewport = {
  themeColor: "#0D0D0D",
  width: "device-width",
  initialScale: 1,
};

export default async function RootLayout({ children }) {
  const user = await getServerUser();

  return (
    <html
      lang="id"
      className={`${inter.variable} ${jakarta.variable} ${mono.variable} dark`}
      suppressHydrationWarning
    >
      <body className="min-h-screen bg-background font-sans text-foreground antialiased">
        <AuthProvider initialUser={user}>
          <div className="pointer-events-none fixed inset-0 -z-10 overflow-hidden">
            <div className="absolute inset-x-0 top-0 h-[500px] bg-radial-fade opacity-60" />
            <div className="absolute inset-0 bg-grid opacity-30 mask-fade-radial" />
          </div>
          <Navbar />
          <main className="relative pt-20">{children}</main>
          <Footer />
        </AuthProvider>
      </body>
    </html>
  );
}
