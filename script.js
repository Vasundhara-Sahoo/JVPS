function getSuggestions() {
  const input = document.getElementById("symptomsInput").value;
  const responseBox = document.getElementById("responseBox");

  if (!input.trim()) {
    responseBox.innerHTML = "❗ Please enter at least one symptom.";
    return;
  }

  fetch("/check", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ symptoms: input })
  })
  .then(res => res.json())
  .then(data => {
    if (data.status === "success") {
      let html = "<strong>Suggestions:</strong><ul>";
      for (let symptom in data.results) {
        html += `<li><strong>${symptom}</strong>: ${data.results[symptom]}</li>`; 
      }
      html += "</ul>";
      responseBox.innerHTML = html;
    } else {
      responseBox.innerHTML = "❗ " + data.message;
    }
  })
  .catch(err => {
    responseBox.innerHTML = "❌ Something went wrong. Please try again.";
    console.error(err);
  });
}