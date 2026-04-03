import { useEffect, useState } from "react";

import { api } from "../lib/api";

export function useJobs(filters = {}) {
  const [jobs, setJobs] = useState([]);
  const [stats, setStats] = useState(null);
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);

  async function load() {
    setLoading(true);
    const [jobsData, statsData, analyticsData] = await Promise.all([
      api.jobs(filters),
      api.dashboardStats(),
      api.analytics(),
    ]);
    setJobs(jobsData);
    setStats(statsData);
    setAnalytics(analyticsData);
    setLoading(false);
  }

  useEffect(() => {
    load();
  }, [filters.search, filters.status, filters.tag]);

  return {
    jobs,
    stats,
    analytics,
    loading,
    reload: load,
    setJobs,
  };
}
