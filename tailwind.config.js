/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/app/**/*.{js,jsx,mdx}",
    "./src/components/**/*.{js,jsx,mdx}",
    "./src/pages/**/*.{js,jsx,mdx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        background: "#0D0D0D",
        surface: "#151515",
        card: "#1C1C1C",
        border: "#262626",
        foreground: "#F5F5F5",
        muted: "#A1A1AA",
        accent: {
          DEFAULT: "#7C3AED",
          hover: "#8B5CF6",
          soft: "rgba(124, 58, 237, 0.15)",
        },
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
        display: ["'Plus Jakarta Sans'", "Inter", "sans-serif"],
        mono: ["'JetBrains Mono'", "monospace"],
      },
      boxShadow: {
        glow: "0 0 40px -10px rgba(124, 58, 237, 0.35)",
        "glow-lg": "0 0 80px -20px rgba(124, 58, 237, 0.45)",
        card: "0 1px 0 0 rgba(255,255,255,0.04) inset, 0 8px 24px -12px rgba(0,0,0,0.6)",
      },
      backgroundImage: {
        "grid-dark":
          "linear-gradient(to right, rgba(255,255,255,0.04) 1px, transparent 1px), linear-gradient(to bottom, rgba(255,255,255,0.04) 1px, transparent 1px)",
        "radial-fade":
          "radial-gradient(ellipse at top, rgba(124,58,237,0.25), transparent 50%)",
      },
      animation: {
        "fade-in": "fadeIn 0.6s ease-out forwards",
        "fade-up": "fadeUp 0.8s ease-out forwards",
        shimmer: "shimmer 2.5s linear infinite",
        float: "float 6s ease-in-out infinite",
      },
      keyframes: {
        fadeIn: {
          "0%": { opacity: 0 },
          "100%": { opacity: 1 },
        },
        fadeUp: {
          "0%": { opacity: 0, transform: "translateY(20px)" },
          "100%": { opacity: 1, transform: "translateY(0)" },
        },
        shimmer: {
          "0%": { backgroundPosition: "-200% 0" },
          "100%": { backgroundPosition: "200% 0" },
        },
        float: {
          "0%, 100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-8px)" },
        },
      },
    },
  },
  plugins: [],
};
