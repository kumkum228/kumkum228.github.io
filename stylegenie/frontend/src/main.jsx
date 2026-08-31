// main.jsx
// --------
// The very first file the browser runs. It renders the <App /> component
// into the #root div from index.html and wraps it in the Router so we can
// have multiple pages (added in Phase 2).

import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
