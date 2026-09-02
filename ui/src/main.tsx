import React from "react";
import ReactDOM from "react-dom/client";
import { App } from "./App";
import { installLogCapture } from "./log/install";
import "./styles/tokens.css";

installLogCapture();

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
