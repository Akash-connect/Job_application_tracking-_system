export function StatCard({ label, value, accent }) {
  return (
    <div className="glass rounded-[28px] p-5 transition duration-300 hover:-translate-y-1">
      <div className="mb-4 h-2 w-16 rounded-full" style={{ background: accent }} />
      <p className="text-sm text-[var(--muted)]">{label}</p>
      <p className="mt-2 font-display text-3xl font-semibold">{value}</p>
    </div>
  );
}

