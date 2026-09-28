const btn = document.getElementById("addBtn");
const output = document.getElementById("output");

btn.addEventListener("click", async () => {
  const a = document.getElementById("a").value;
  const b = document.getElementById("b").value;

  const response = await fetch("http://127.0.0.1:5000/api/add", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      a: Number(a),
      b: Number(b)
    })
  });

  const  data = await response.json();
  output.textContent = "Result: " + data.result;
});