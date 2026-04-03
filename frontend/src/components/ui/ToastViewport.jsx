import { CheckCircle2, Info, TriangleAlert, X } from "lucide-react";

import { useToast } from "../../hooks/useToast";

const toneMap = {
  success: { icon: CheckCircle2, className: "border-emerald-400/40 bg-emerald-400/10 text-emerald-100" },
  warning: { icon: TriangleAlert, className: "border-amber-400/40 bg-amber-400/10 text-amber-100" },
  info: { icon: Info, className: "border-sky-400/40 bg-sky-400/10 text-sky-100" },
};

export function ToastViewport() {
  const { toasts, dismissToast } = useToast();

  return (
    <div className="pointer-events-none fixed right-4 top-4 z-50 space-y-3">
      {toasts.map((toast) => {
        const tone = toneMap[toast.tone] || toneMap.info;
        const Icon = tone.icon;
        return (
          <div
            key={toast.id}
            className={`pointer-events-auto animate-fade-in glass flex min-w-[300px] items-start gap-3 rounded-2xl border px-4 py-3 ${tone.className}`}
          >
            <Icon size={18} className="mt-0.5 shrink-0" />
            <p className="flex-1 text-sm font-medium">{toast.message}</p>
            <button onClick={() => dismissToast(toast.id)} className="opacity-70 transition hover:opacity-100">
              <X size={16} />
            </button>
          </div>
        );
      })}
    </div>
  );
}

