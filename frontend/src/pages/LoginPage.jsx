import { useState } from "react";

import { api } from "../lib/api";
import { useToast } from "../hooks/useToast";

export function LoginPage({ onAuthenticated }) {
  const [mode, setMode] = useState("login");
  const [form, setForm] = useState({ username: "", email: "", password: "", title: "" });
  const [loading, setLoading] = useState(false);
  const { pushToast } = useToast();

  async function handleSubmit(event) {
    event.preventDefault();
    setLoading(true);
    try {
      const payload =
        mode === "login"
          ? await api.login({ username: form.username, password: form.password })
          : await api.register(form);
      localStorage.setItem("jats-token", payload.access_token);
      const user = await api.me();
      pushToast(mode === "login" ? "Welcome back." : "Account created.", "success");
      onAuthenticated(user);
    } catch (error) {
      pushToast(error.message, "warning");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center px-4">
      <div className="glass grid w-full max-w-5xl gap-8 rounded-[36px] p-6 lg:grid-cols-[1.15fr_0.85fr] lg:p-10">
        <section className="rounded-[30px] bg-mesh p-8">
          <p className="rounded-full border border-white/10 bg-white/10 px-4 py-2 text-xs uppercase tracking-[0.3em] text-sky-100">
            Premium pipeline management
          </p>
          <h1 className="mt-6 max-w-xl font-display text-4xl font-semibold leading-tight lg:text-5xl">
            Track every application with the focus of a modern revenue dashboard.
          </h1>
          <p className="mt-4 max-w-lg text-base text-slate-300">
            JATS blends analytics, kanban flow, reminders, and admin controls into one career operating system.
          </p>
          <div className="mt-8 grid gap-4 sm:grid-cols-3">
            {[
              ["120+", "Applications managed"],
              ["4x", "Faster follow-ups"],
              ["24/7", "Admin visibility"],
            ].map(([value, label]) => (
              <div key={label} className="rounded-3xl border border-white/10 bg-white/10 p-4">
                <p className="font-display text-2xl font-semibold">{value}</p>
                <p className="mt-2 text-sm text-slate-300">{label}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="p-4 lg:p-6">
          <p className="text-sm uppercase tracking-[0.3em] text-[var(--muted)]">{mode === "login" ? "Welcome back" : "Create account"}</p>
          <h2 className="mt-3 font-display text-3xl font-semibold">{mode === "login" ? "Sign in" : "Start tracking"}</h2>
          <form onSubmit={handleSubmit} className="mt-8 space-y-4">
            <input className="w-full rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Username" value={form.username} onChange={(e) => setForm({ ...form, username: e.target.value })} required />
            {mode === "register" ? (
              <>
                <input className="w-full rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Email" type="email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} required />
                <input className="w-full rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Professional title" value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} />
              </>
            ) : null}
            <input className="w-full rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Password" type="password" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} required />
            <button type="submit" disabled={loading} className="w-full rounded-2xl bg-sky-400 px-4 py-3 font-semibold text-slate-950">
              {loading ? "Please wait..." : mode === "login" ? "Sign in" : "Create account"}
            </button>
          </form>
          <button onClick={() => setMode((current) => (current === "login" ? "register" : "login"))} className="mt-6 text-sm text-sky-300">
            {mode === "login" ? "Need an account? Register" : "Already have an account? Login"}
          </button>
        </section>
      </div>
    </div>
  );
}

