
javascript
document.getElementById("styleForm").onsubmit = async (e) => {
  e.preventDefault();
  let formData = new FormData(e.target);
  let response = await fetch("http://127.0.0.1:8000/recommend", {
    method: "POST",
    body: formData
  });
  let data = await response.json();
  document.getElementById("results").textContent = JSON.stringify(data, null, 2);
};
