const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8001/api/v1";

async function request(path, options = {}) {
  const token = localStorage.getItem("jats-token");
  const response = await fetch(`${API_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    },
    ...options,
  });

  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({ detail: "Something went wrong" }));
    throw new Error(errorBody.detail || "Request failed");
  }

  if (response.status === 204) {
    return null;
  }

  return response.json();
}

export const api = {
  login: (payload) => request("/auth/login", { method: "POST", body: JSON.stringify(payload) }),
  register: (payload) => request("/auth/register", { method: "POST", body: JSON.stringify(payload) }),
  me: () => request("/auth/me"),
  jobs: (params = {}) => {
    const search = new URLSearchParams(params).toString();
    return request(`/jobs${search ? `?${search}` : ""}`);
  },
  createJob: (payload) => request("/jobs", { method: "POST", body: JSON.stringify(payload) }),
  updateJob: (id, payload) => request(`/jobs/${id}`, { method: "PUT", body: JSON.stringify(payload) }),
  deleteJob: (id) => request(`/jobs/${id}`, { method: "DELETE" }),
  analytics: () => request("/analytics"),
  dashboardStats: () => request("/dashboard-stats"),
};

