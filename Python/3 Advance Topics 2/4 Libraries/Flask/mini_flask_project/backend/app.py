from flask import Flask, request, jsonify, render_template
from main import add_numbers

app = Flask(__name__, 
            static_folder='../frontend/static', 
            template_folder='../frontend/templates')

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/api/add", methods=["POST"])
def add():
    data: dict[str, int] = request.json
    result: int = add_numbers(data['a'], data['b'])
    return jsonify({'result': result})

if __name__ == "__main__" :
    app.run(debug=True)