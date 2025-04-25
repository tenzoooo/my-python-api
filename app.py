# app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run():
    data = request.json
    file_url = data.get("file_url")
    if not file_url:
        return jsonify({"error": "No file URL provided"}), 400

    # ファイルを取得
    file = requests.get(file_url)
    with open("file.pdf", "wb") as f:
        f.write(file.content)

    return jsonify({
        "message": "ファイルを受け取りました！",
        "file_url": file_url
    })

# for Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
