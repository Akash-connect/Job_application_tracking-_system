import { useState } from "react";
import { BellRing, Plus } from "lucide-react";

import { api } from "../lib/api";
import { useJobs } from "../hooks/useJobs";
import { useToast } from "../hooks/useToast";
import { MonthlyApplicationsChart } from "../components/charts/MonthlyApplicationsChart";
import { StatusDistributionChart } from "../components/charts/StatusDistributionChart";
import { FilterBar } from "../components/ui/FilterBar";
import { JobFormModal } from "../components/ui/JobFormModal";
import { JobTable } from "../components/ui/JobTable";
import { KanbanBoard } from "../components/ui/KanbanBoard";
import { SkeletonCard } from "../components/ui/SkeletonCard";
import { StatCard } from "../components/ui/StatCard";

export function DashboardPage() {
  const [filters, setFilters] = useState({ search: "", status: "", tag: "" });
  const [showModal, setShowModal] = useState(false);
  const [editingJob, setEditingJob] = useState(null);
  const { jobs, stats, analytics, loading, reload } = useJobs(filters);
  const { pushToast } = useToast();

  async function handleCreate(payload) {
    try {
      await api.createJob(payload);
      setShowModal(false);
      pushToast("Application added to your pipeline.", "success");
      await reload();
    } catch (error) {
      pushToast(error.message, "warning");
    }
  }

  async function handleStatusChange(jobId, nextStatus) {
    try {
      await api.updateJob(jobId, { status: nextStatus });
      pushToast(`Moved application to ${nextStatus}.`, "info");
      await reload();
    } catch (error) {
      pushToast(error.message, "warning");
    }
  }

  async function handleDelete(jobId) {
    try {
      await api.deleteJob(jobId);
      pushToast("Application removed.", "info");
      await reload();
    } catch (error) {
      pushToast(error.message, "warning");
    }
  }

  async function handleUpdate(payload) {
    if (!editingJob) {
      return;
    }

    try {
      await api.updateJob(editingJob.id, payload);
      setEditingJob(null);
      pushToast("Application updated.", "success");
      await reload();
    } catch (error) {
      pushToast(error.message, "warning");
    }
  }

  return (
    <div className="space-y-6">
      <section className="glass animate-fade-in rounded-[32px] p-6 lg:p-8">
        <div className="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.35em] text-[var(--muted)]">Career pipeline intelligence</p>
            <h1 className="mt-3 font-display text-4xl font-semibold">Stay on top of every application touchpoint.</h1>
            <p className="mt-3 max-w-2xl text-base text-[var(--muted)]">
              Blend analytics, pipeline management, reminders, and admin workflows in one polished system.
            </p>
          </div>
          <div className="flex flex-wrap gap-3">
            <button className="rounded-2xl border border-white/10 bg-white/5 px-5 py-3 text-sm font-semibold">
              <span className="inline-flex items-center gap-2"><BellRing size={16} /> Reminder queue</span>
            </button>
            <button onClick={() => setShowModal(true)} className="rounded-2xl bg-sky-400 px-5 py-3 text-sm font-semibold text-slate-950">
              <span className="inline-flex items-center gap-2"><Plus size={16} /> Add job</span>
            </button>
          </div>
        </div>
      </section>

      <FilterBar filters={filters} onFilterChange={(key, value) => setFilters((current) => ({ ...current, [key]: value }))} />

      {loading || !stats || !analytics ? (
        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-5">
          {Array.from({ length: 5 }).map((_, index) => (
            <SkeletonCard key={index} />
          ))}
        </div>
      ) : (
        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-5">
          <StatCard label="Total applications" value={stats.total_applications} accent="#38bdf8" />
          <StatCard label="Interviews" value={stats.interviews} accent="#f59e0b" />
          <StatCard label="Offers" value={stats.offers} accent="#34d399" />
          <StatCard label="Rejections" value={stats.rejections} accent="#f87171" />
          <StatCard label="Active follow-ups" value={stats.active_followups} accent="#c084fc" />
        </div>
      )}

      {analytics ? (
        <div className="grid gap-4 xl:grid-cols-[1.35fr_0.65fr]">
          <MonthlyApplicationsChart data={analytics.monthly_applications} />
          <StatusDistributionChart data={analytics.status_distribution} />
        </div>
      ) : null}

      <section className="space-y-4">
        <div className="flex items-center justify-between">
          <h2 className="font-display text-2xl font-semibold">Kanban board</h2>
          <p className="text-sm text-[var(--muted)]">Drag cards across statuses to keep the pipeline current.</p>
        </div>
        <KanbanBoard jobs={jobs} onStatusChange={handleStatusChange} />
      </section>

      <section className="space-y-4">
        <div className="flex items-center justify-between">
          <h2 className="font-display text-2xl font-semibold">Application ledger</h2>
          <p className="text-sm text-[var(--muted)]">A searchable table for detail-oriented review.</p>
        </div>
        <JobTable jobs={jobs} onDelete={handleDelete} onEdit={setEditingJob} />
      </section>

      {showModal ? <JobFormModal onClose={() => setShowModal(false)} onSubmit={handleCreate} /> : null}
      {editingJob ? <JobFormModal initialData={editingJob} onClose={() => setEditingJob(null)} onSubmit={handleUpdate} /> : null}
    </div>
  );
}
