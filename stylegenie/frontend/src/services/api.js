// api.js
// -------
// One shared Axios instance for talking to the FastAPI backend.
// Every service/component imports `api` from here instead of hard-coding URLs.

import axios from "axios";

// Vite exposes env vars that start with VITE_ on import.meta.env.
// Falls back to localhost if the .env file is missing.
const baseURL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api";

const api = axios.create({
  baseURL,
  headers: { "Content-Type": "application/json" },
});

// In later phases we will attach the JWT token to every request here:
//
// api.interceptors.request.use((config) => {
//   const token = localStorage.getItem("token");
//   if (token) config.headers.Authorization = `Bearer ${token}`;
//   return config;
// });

export default api;
