import { Cell, Pie, PieChart, ResponsiveContainer, Tooltip } from "recharts";

const COLORS = {
  applied: "#38bdf8",
  interview: "#f59e0b",
  offer: "#34d399",
  rejected: "#f87171",
};

export function StatusDistributionChart({ data }) {
  return (
    <div className="glass rounded-[28px] p-6">
      <div className="mb-6">
        <p className="text-sm uppercase tracking-[0.3em] text-[var(--muted)]">Mix</p>
        <h3 className="font-display text-xl font-semibold">Status distribution</h3>
      </div>
      <div className="h-72">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie data={data} dataKey="count" nameKey="status" innerRadius={68} outerRadius={100} paddingAngle={4}>
              {data.map((entry) => (
                <Cell key={entry.status} fill={COLORS[entry.status] || "#94a3b8"} />
              ))}
            </Pie>
            <Tooltip contentStyle={{ background: "#0f172a", border: "1px solid rgba(148, 163, 184, 0.2)", borderRadius: "16px" }} />
          </PieChart>
        </ResponsiveContainer>
      </div>
      <div className="mt-4 flex flex-wrap gap-3">
        {data.map((entry) => (
          <span key={entry.status} className="rounded-full border border-white/10 px-3 py-1 text-xs font-semibold">
            {entry.status}: {entry.count}
          </span>
        ))}
      </div>
    </div>
  );
}

