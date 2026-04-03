import { BriefcaseBusiness, LayoutDashboard, MoonStar, Search, SunMedium } from "lucide-react";

export function Shell({ children, theme, onToggleTheme }) {
  return (
    <div className="min-h-screen">
      <div className="mx-auto flex min-h-screen max-w-[1600px] flex-col lg:flex-row">
        <aside className="glass animate-fade-in m-4 rounded-[28px] border border-white/10 p-6 lg:m-6 lg:w-72">
          <div className="mb-10 flex items-center gap-3">
            <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-sky-400/20 text-sky-300">
              <BriefcaseBusiness size={24} />
            </div>
            <div>
              <p className="font-display text-xl font-semibold">JATS</p>
              <p className="text-sm text-[var(--muted)]">Career command center</p>
            </div>
          </div>

          <nav className="space-y-3">
            {[
              { icon: LayoutDashboard, label: "Dashboard" },
              { icon: Search, label: "Pipeline" },
            ].map((item) => (
              <button
                key={item.label}
                className="flex w-full items-center gap-3 rounded-2xl border border-white/10 bg-white/5 px-4 py-3 text-left text-sm font-semibold transition hover:-translate-y-0.5 hover:bg-white/10"
              >
                <item.icon size={18} />
                {item.label}
              </button>
            ))}
          </nav>

          <div className="mt-10 rounded-3xl border border-sky-300/20 bg-sky-400/10 p-5">
            <p className="text-sm font-semibold text-sky-200">Follow-up automation</p>
            <p className="mt-2 text-sm text-slate-300">
              Celery-ready reminders keep your next touchpoint visible without cluttering the board.
            </p>
          </div>

          <button
            onClick={onToggleTheme}
            className="mt-10 flex w-full items-center justify-between rounded-2xl border border-white/10 bg-white/5 px-4 py-3 text-sm font-semibold transition hover:bg-white/10"
          >
            <span>{theme === "dark" ? "Dark theme" : "Light theme"}</span>
            {theme === "dark" ? <MoonStar size={18} /> : <SunMedium size={18} />}
          </button>
        </aside>

        <main className="flex-1 p-4 lg:p-6">{children}</main>
      </div>
    </div>
  );
}

