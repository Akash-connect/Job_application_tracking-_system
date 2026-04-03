/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  darkMode: ["class"],
  theme: {
    extend: {
      fontFamily: {
        display: ["Poppins", "sans-serif"],
        body: ["Manrope", "sans-serif"],
      },
      boxShadow: {
        glass: "0 24px 80px rgba(15, 23, 42, 0.18)",
      },
      backgroundImage: {
        mesh: "radial-gradient(circle at top left, rgba(14, 165, 233, 0.25), transparent 35%), radial-gradient(circle at bottom right, rgba(249, 115, 22, 0.2), transparent 30%)",
      },
    },
  },
  plugins: [],
};

