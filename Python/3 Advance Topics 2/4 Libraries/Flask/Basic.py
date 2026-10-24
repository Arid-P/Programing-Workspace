# ==============================================
# Flask Notes - Backend Web Development
# ==============================================

# 1️⃣ Importing Flask and Related Modules

# Flask itself: used to create the server and define routes
# request: access incoming request data (JSON, form, etc.)
# jsonify: send Python data as JSON response
# render_template: serve HTML files from /templates folder

from flask import Flask, request, jsonify, render_template
from main import add_numbers  # your business logic, separate from Flask

# ----------------------------------------------
# 2️⃣ Creating the Flask App Object

# Flask app object is the "central server" object.
# It manages routes, configuration, and request handling.
# It does NOT hold request data itself.
# __name__ tells Flask where the app lives (module reference)
app = Flask(__name__, 
            static_folder='../frontend/static',       # Path for CSS/JS/images
            template_folder='../frontend/templates') # Path for HTML files

# ==============================================
# 3️⃣ Route Definition

# Routes map URLs + HTTP methods → Python functions.
# Decorator syntax: @app.route("URL", methods=[...])
# Function executes when the URL is requested with the specified HTTP method

# Example: Serve HTML page at "/"
@app.route("/", methods=["GET"])
def home():
    # render_template looks for the HTML in the 'templates' folder
    return render_template("index.html")


# Example: API route for adding numbers
@app.route("/api/add", methods=["POST"])
def add():
    # 1. Access request data from frontend
    data: dict[str, int] = request.json   # request.json gives a Python dict
    # 2. Extract values and call business logic
    result: int = add_numbers(data['a'], data['b'])
    # 3. Return response as JSON to frontend
    return jsonify({'result': result})

# ==============================================
# 4️⃣ Running the Flask App

# Ensures the server runs only if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # debug=True enables hot reload and error pages

# ==============================================
# 5️⃣ Key Concepts Recap

# - app: central Flask object, controls routing & config
# - request: contains incoming request data (request.json for JSON)
# - jsonify: sends Python dict/list as JSON
# - render_template: serves HTML files from /templates
# - Routes: map URL + HTTP method → Python function
# - POST requests: used to send data from frontend to backend
# - GET requests: used to fetch pages or data
# - Folder structure:

# project/
# ├─ backend/
# │   └─ app.py
# │   └─ main.py   business logic, pure Python
# ├─ frontend/
#      ├─ static/      # CSS, JS
#      └─ templates/   # HTML files


# - Frontend JS should convert inputs to correct types before sending JSON
# - Separation of concerns:
#   * main.py → pure logic
#   * app.py → Flask routing & glue
#   * frontend → HTML/CSS/JS UI

# ==============================================
# 6️⃣ Example JS Fetch (Frontend → Flask API)

# <script>
# const btn = document.getElementById("addBtn");
# const output = document.getElementById("output");
# btn.addEventListener("click", async () => {
#     const a = Number(document.getElementById("a").value);
#     const b = Number(document.getElementById("b").value);
#     const response = await fetch("http://127.0.0.1:5000/api/add", {
#         method: "POST",
#         headers: { "Content-Type": "application/json" },
#         body: JSON.stringify({ a: a, b: b })
#     });
#     const data = await response.json();
#     output.textContent = "Result: " + data.result;
# });
# </script>

# ==============================================
# ✅ Notes Summary

# 1. Flask apps are modular: logic separate from routing.
# 2. request.json is always a dict (Python) when JSON is sent.
# 3. All JS fetch POST requests must match JSON expected by backend.
# 4. app.run(debug=True) for development only; production uses WSGI server.
# 5. Folder structure and `template_folder`/`static_folder` are crucial.
# 6. Always use uppercase HTTP methods in decorators ("GET", "POST").