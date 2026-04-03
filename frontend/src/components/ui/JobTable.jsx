export function JobTable({ jobs, onDelete, onEdit }) {
  return (
    <div className="glass overflow-hidden rounded-[28px]">
      <div className="overflow-x-auto">
        <table className="min-w-full text-left">
          <thead className="border-b border-white/10 text-xs uppercase tracking-[0.25em] text-[var(--muted)]">
            <tr>
              <th className="px-6 py-4">Role</th>
              <th className="px-6 py-4">Company</th>
              <th className="px-6 py-4">Status</th>
              <th className="px-6 py-4">Applied</th>
              <th className="px-6 py-4">Tags</th>
              <th className="px-6 py-4">Actions</th>
            </tr>
          </thead>
          <tbody>
            {jobs.map((job) => (
              <tr key={job.id} className="border-b border-white/5 text-sm transition hover:bg-white/5">
                <td className="px-6 py-4 font-semibold">{job.role}</td>
                <td className="px-6 py-4">{job.company.name}</td>
                <td className="px-6 py-4 capitalize">{job.status}</td>
                <td className="px-6 py-4">{job.application_date}</td>
                <td className="px-6 py-4">
                  <div className="flex flex-wrap gap-2">
                    {job.tags.map((tag) => (
                      <span key={tag.id} className="rounded-full border border-white/10 px-2 py-1 text-xs">
                        {tag.name}
                      </span>
                    ))}
                  </div>
                </td>
                <td className="px-6 py-4">
                  <div className="flex gap-2">
                    <button onClick={() => onEdit(job)} className="rounded-full border border-white/10 px-3 py-1 text-xs font-semibold">
                      Edit
                    </button>
                    <button onClick={() => onDelete(job.id)} className="rounded-full border border-red-400/30 px-3 py-1 text-xs font-semibold text-red-200">
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
