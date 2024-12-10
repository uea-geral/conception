import "./css/styles.css";

const fileLabel = document.querySelectorAll(".import-file");
const fileInput = document.querySelector("#file");
const forms = document.querySelector("#forms");
const notification = document.querySelector(".notifications");
const notificationLabel = document.querySelector(".notifications label");
const input = document.querySelector("#prompt");
const code = document.querySelector(".code");

const options = document.querySelector(".options");

const API_URL = "http://127.0.0.1:5000";

async function submit() {
  notify("Identificando os requisitos");
  let response;
  const prompt = input?.value;
  response = await fetch(`${API_URL}/requirements/prompt`, {
    method: "POST",
    mode: "cors",
    body: JSON.stringify({
      prompt: prompt,
    }),
  });
  const data = await response.json();
  const requirements = data.requirements.filter(
    (requirement: string) => requirement.length > 0
  );
  if (options) options.innerHTML = "";
  for (const requirement of requirements) {
    if (options) {
      options.innerHTML += `<li class="option">${requirement}</li>`;
    }
  }
  notify("Gerando código para as funcionalidades identificadas");
  response = await fetch(`${API_URL}/requirements/generate/code`, {
    method: "POST",
    mode: "cors",
    body: JSON.stringify({
      requirements: requirements,
      past: "",
    }),
  });
  const codeContent = await response.json();
  if (code) code.innerHTML = codeContent.code;
  closeNotifications();
}

function notify(message: string) {
  if (notificationLabel) notificationLabel.textContent = message;
  notification?.classList.add("open");
}

function closeNotifications() {
  notification?.classList.remove("open");
}

function addEvents() {
  fileLabel.forEach((label) => {
    label.addEventListener("click", () => {
      fileInput.click();
    });
  });

  fileInput?.addEventListener("change", (event) => {
    event.preventDefault();
    if (fileInput.files[0] !== undefined) submit();
  });

  forms?.addEventListener("submit", (event) => {
    event?.preventDefault();
    submit();
  });
}

function main() {
  addEvents();
}

main();
