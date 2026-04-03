import { Area, AreaChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

export function MonthlyApplicationsChart({ data }) {
  return (
    <div className="glass rounded-[28px] p-6">
      <div className="mb-6">
        <p className="text-sm uppercase tracking-[0.3em] text-[var(--muted)]">Momentum</p>
        <h3 className="font-display text-xl font-semibold">Monthly applications</h3>
      </div>
      <div className="h-72">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={data}>
            <defs>
              <linearGradient id="appsGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#38bdf8" stopOpacity={0.5} />
                <stop offset="95%" stopColor="#38bdf8" stopOpacity={0.02} />
              </linearGradient>
            </defs>
            <CartesianGrid stroke="rgba(148, 163, 184, 0.1)" vertical={false} />
            <XAxis dataKey="month" stroke="rgba(148, 163, 184, 0.7)" />
            <YAxis stroke="rgba(148, 163, 184, 0.7)" />
            <Tooltip contentStyle={{ background: "#0f172a", border: "1px solid rgba(148, 163, 184, 0.2)", borderRadius: "16px" }} />
            <Area type="monotone" dataKey="count" stroke="#38bdf8" fill="url(#appsGradient)" strokeWidth={3} />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

