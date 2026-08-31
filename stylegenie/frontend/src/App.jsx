// App.jsx
// -------
// PHASE 1 placeholder. Right now it just checks that the frontend can reach
// the backend health endpoint, so you can confirm the two halves talk to
// each other. In Phase 2 this becomes the router with Header, Home, product
// pages, etc.

import { useEffect, useState } from "react";
import api from "./services/api";

export default function App() {
  const [status, setStatus] = useState("checking...");

  useEffect(() => {
    api
      .get("/health")
      .then((res) => setStatus(res.data.status))
      .catch(() => setStatus("backend not reachable"));
  }, []);

  return (
    <main style={{ fontFamily: "system-ui", textAlign: "center", padding: "4rem" }}>
      <h1>✨ StyleGenie</h1>
      <p>AI Fashion Shopping Assistant</p>
      <p>
        Backend status: <strong>{status}</strong>
      </p>
      <p style={{ color: "#888" }}>Phase 1 setup complete.</p>
    </main>
  );
}
