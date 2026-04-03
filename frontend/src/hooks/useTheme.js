import { useEffect, useState } from "react";

export function useTheme() {
  const [theme, setTheme] = useState(() => localStorage.getItem("jats-theme") || "dark");

  useEffect(() => {
    document.documentElement.classList.toggle("dark", theme === "dark");
    document.documentElement.classList.toggle("light", theme === "light");
    localStorage.setItem("jats-theme", theme);
  }, [theme]);

  return {
    theme,
    toggleTheme: () => setTheme((current) => (current === "dark" ? "light" : "dark")),
  };
}

