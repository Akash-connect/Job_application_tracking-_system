const COLUMNS = ["applied", "interview", "offer", "rejected"];

export function KanbanBoard({ jobs, onStatusChange }) {
  function handleDrop(event, nextStatus) {
    event.preventDefault();
    const jobId = Number(event.dataTransfer.getData("jobId"));
    onStatusChange(jobId, nextStatus);
  }

  return (
    <div className="grid gap-4 xl:grid-cols-4">
      {COLUMNS.map((status) => (
        <div
          key={status}
          className="glass min-h-80 rounded-[28px] p-4"
          onDragOver={(event) => event.preventDefault()}
          onDrop={(event) => handleDrop(event, status)}
        >
          <div className="mb-4 flex items-center justify-between">
            <h3 className="font-display text-lg font-semibold capitalize">{status}</h3>
            <span className="rounded-full border border-white/10 px-3 py-1 text-xs">{jobs.filter((job) => job.status === status).length}</span>
          </div>
          <div className="space-y-3">
            {jobs
              .filter((job) => job.status === status)
              .map((job) => (
                <article
                  key={job.id}
                  draggable
                  onDragStart={(event) => event.dataTransfer.setData("jobId", String(job.id))}
                  className="rounded-3xl border border-white/10 bg-white/5 p-4 transition hover:-translate-y-1"
                >
                  <p className="font-semibold">{job.role}</p>
                  <p className="mt-1 text-sm text-[var(--muted)]">{job.company.name}</p>
                  <div className="mt-4 flex flex-wrap gap-2">
                    {job.tags.map((tag) => (
                      <span key={tag.id} className="rounded-full bg-white/10 px-2 py-1 text-xs">
                        {tag.name}
                      </span>
                    ))}
                  </div>
                </article>
              ))}
          </div>
        </div>
      ))}
    </div>
  );
}
