import { Navigate, Route, Routes } from "react-router-dom";
import { useEffect, useState } from "react";

import { api } from "./lib/api";
import { useTheme } from "./hooks/useTheme";
import { ToastProvider } from "./hooks/useToast";
import { Shell } from "./components/layout/Shell";
import { ToastViewport } from "./components/ui/ToastViewport";
import { DashboardPage } from "./pages/DashboardPage";
import { LoginPage } from "./pages/LoginPage";

function ProtectedApp() {
  const { theme, toggleTheme } = useTheme();
  return (
    <div className={theme}>
      <Shell theme={theme} onToggleTheme={toggleTheme}>
        <DashboardPage />
      </Shell>
    </div>
  );
}

export default function App() {
  const [user, setUser] = useState(undefined);

  useEffect(() => {
    const token = localStorage.getItem("jats-token");
    if (!token) {
      setUser(null);
      return;
    }

    api
      .me()
      .then((payload) => setUser(payload))
      .catch(() => {
        localStorage.removeItem("jats-token");
        setUser(null);
      });
  }, []);

  if (user === undefined) {
    return <div className="flex min-h-screen items-center justify-center text-slate-200">Loading workspace...</div>;
  }

  return (
    <ToastProvider>
      <Routes>
        <Route path="/login" element={user ? <Navigate to="/" replace /> : <LoginPage onAuthenticated={setUser} />} />
        <Route path="/" element={user ? <ProtectedApp /> : <Navigate to="/login" replace />} />
      </Routes>
      <ToastViewport />
    </ToastProvider>
  );
}

