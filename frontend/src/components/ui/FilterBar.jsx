export function FilterBar({ filters, onFilterChange }) {
  return (
    <div className="glass flex flex-col gap-4 rounded-[28px] p-5 lg:flex-row lg:items-center">
      <input
        type="text"
        placeholder="Search role, company, or notes"
        value={filters.search}
        onChange={(event) => onFilterChange("search", event.target.value)}
        className="flex-1 rounded-2xl border border-white/10 bg-white/5 px-4 py-3 outline-none transition focus:border-sky-400/40"
      />
      <select
        value={filters.status}
        onChange={(event) => onFilterChange("status", event.target.value)}
        className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3 outline-none"
      >
        <option value="">All statuses</option>
        <option value="applied">Applied</option>
        <option value="interview">Interview</option>
        <option value="offer">Offer</option>
        <option value="rejected">Rejected</option>
      </select>
      <input
        type="text"
        placeholder="Tag"
        value={filters.tag}
        onChange={(event) => onFilterChange("tag", event.target.value)}
        className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3 outline-none transition focus:border-sky-400/40"
      />
    </div>
  );
}
