from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

from ice_breaker import ice_breaker_with_name

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form.get("name")
    summary, profile_pic = ice_breaker_with_name(name)
    return jsonify({"summary": summary.to_dict(), "profile_pic": profile_pic})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)

