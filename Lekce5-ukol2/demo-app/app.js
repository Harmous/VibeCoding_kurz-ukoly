const status = document.querySelector("#status");
const button = document.querySelector("#refresh-button");

function buildStatusMessage() {
  return "The local demo app is ready for Codex setup checks.";
}

function refreshStatus() {
  status.textContent = buildStatusMessage();
}

function neverUsedHelper() {
  return "This function is intentionally unused for dead-code analysis.";
}

const staleValue = "unused constant";

button.addEventListener("click", refreshStatus);
refreshStatus();
