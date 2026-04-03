import { useState } from "react";

const INITIAL_STATE = {
  company: { name: "", website: "", location: "", notes: "" },
  role: "",
  status: "applied",
  salary_min: "",
  salary_max: "",
  job_url: "",
  notes: "",
  application_date: new Date().toISOString().slice(0, 10),
  follow_up_date: "",
  is_remote: false,
  tag_names: "",
};

function mapInitialData(initialData) {
  if (!initialData) {
    return INITIAL_STATE;
  }

  return {
    company: {
      name: initialData.company?.name || "",
      website: initialData.company?.website || "",
      location: initialData.company?.location || "",
      notes: initialData.company?.notes || "",
    },
    role: initialData.role || "",
    status: initialData.status || "applied",
    salary_min: initialData.salary_min || "",
    salary_max: initialData.salary_max || "",
    job_url: initialData.job_url || "",
    notes: initialData.notes || "",
    application_date: initialData.application_date || new Date().toISOString().slice(0, 10),
    follow_up_date: initialData.follow_up_date || "",
    is_remote: Boolean(initialData.is_remote),
    tag_names: (initialData.tags || []).map((tag) => tag.name).join(", "),
  };
}

export function JobFormModal({ initialData, onClose, onSubmit }) {
  const [form, setForm] = useState(() => mapInitialData(initialData));
  const [saving, setSaving] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();
    setSaving(true);
    await onSubmit({
      ...form,
      salary_min: form.salary_min ? Number(form.salary_min) : null,
      salary_max: form.salary_max ? Number(form.salary_max) : null,
      follow_up_date: form.follow_up_date || null,
      tag_names: form.tag_names
        .split(",")
        .map((item) => item.trim())
        .filter(Boolean),
    });
    setSaving(false);
  }

  return (
    <div className="fixed inset-0 z-40 flex items-center justify-center bg-slate-950/70 p-4 backdrop-blur-sm">
      <form onSubmit={handleSubmit} className="glass max-h-[90vh] w-full max-w-3xl overflow-y-auto rounded-[32px] p-6">
        <div className="mb-6 flex items-center justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-[var(--muted)]">{initialData ? "Refine opportunity" : "New opportunity"}</p>
            <h3 className="font-display text-2xl font-semibold">{initialData ? "Edit job application" : "Add job application"}</h3>
          </div>
          <button type="button" onClick={onClose} className="rounded-full border border-white/10 px-3 py-1 text-sm">
            Close
          </button>
        </div>

        <div className="grid gap-4 md:grid-cols-2">
          <input className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Company name" value={form.company.name} onChange={(e) => setForm({ ...form, company: { ...form.company, name: e.target.value } })} required />
          <input className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Role" value={form.role} onChange={(e) => setForm({ ...form, role: e.target.value })} required />
          <input className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Company website" value={form.company.website} onChange={(e) => setForm({ ...form, company: { ...form.company, website: e.target.value } })} />
          <input className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Location" value={form.company.location} onChange={(e) => setForm({ ...form, company: { ...form.company, location: e.target.value } })} />
          <input type="date" className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3" value={form.application_date} onChange={(e) => setForm({ ...form, application_date: e.target.value })} />
          <input type="date" className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3" value={form.follow_up_date} onChange={(e) => setForm({ ...form, follow_up_date: e.target.value })} />
          <select className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3" value={form.status} onChange={(e) => setForm({ ...form, status: e.target.value })}>
            <option value="applied">Applied</option>
            <option value="interview">Interview</option>
            <option value="offer">Offer</option>
            <option value="rejected">Rejected</option>
          </select>
          <input className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Salary min" type="number" value={form.salary_min} onChange={(e) => setForm({ ...form, salary_min: e.target.value })} />
          <input className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Salary max" type="number" value={form.salary_max} onChange={(e) => setForm({ ...form, salary_max: e.target.value })} />
          <input className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Job URL" value={form.job_url} onChange={(e) => setForm({ ...form, job_url: e.target.value })} />
          <input className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Tags: Frontend, Remote" value={form.tag_names} onChange={(e) => setForm({ ...form, tag_names: e.target.value })} />
        </div>

        <textarea className="mt-4 min-h-28 w-full rounded-2xl border border-white/10 bg-white/5 px-4 py-3" placeholder="Application notes" value={form.notes} onChange={(e) => setForm({ ...form, notes: e.target.value })} />

        <label className="mt-4 flex items-center gap-3 text-sm">
          <input type="checkbox" checked={form.is_remote} onChange={(e) => setForm({ ...form, is_remote: e.target.checked })} />
          Mark as remote opportunity
        </label>

        <div className="mt-6 flex justify-end gap-3">
          <button type="button" onClick={onClose} className="rounded-2xl border border-white/10 px-5 py-3 text-sm font-semibold">
            Cancel
          </button>
          <button type="submit" disabled={saving} className="rounded-2xl bg-sky-400 px-5 py-3 text-sm font-semibold text-slate-950">
            {saving ? "Saving..." : initialData ? "Save changes" : "Create application"}
          </button>
        </div>
      </form>
    </div>
  );
}
