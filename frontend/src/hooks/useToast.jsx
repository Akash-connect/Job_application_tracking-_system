import { createContext, useContext, useState } from "react";

const ToastContext = createContext(null);

export function ToastProvider({ children }) {
  const [toasts, setToasts] = useState([]);

  const value = {
    toasts,
    pushToast: (message, tone = "info") => {
      const id = crypto.randomUUID();
      setToasts((current) => [...current, { id, message, tone }]);
      setTimeout(() => {
        setToasts((current) => current.filter((toast) => toast.id !== id));
      }, 3500);
    },
    dismissToast: (id) => setToasts((current) => current.filter((toast) => toast.id !== id)),
  };

  return <ToastContext.Provider value={value}>{children}</ToastContext.Provider>;
}

export function useToast() {
  const context = useContext(ToastContext);
  if (!context) {
    throw new Error("useToast must be used inside ToastProvider");
  }
  return context;
}
