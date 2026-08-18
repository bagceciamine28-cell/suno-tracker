from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.get("/")
def home():
    return "Suno Follow Compare API çalışıyor."

@app.get("/check")
def check():

    username = request.args.get("username", "").strip()

    if not username:
        return jsonify({
            "ok": False,
            "error": "username gerekli"
        }), 400

    url = f"https://suno.com/@{username}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        return jsonify({
            "ok": response.ok,
            "status": response.status_code,
            "length": len(response.text),
            "url": url
        })

    except Exception as e:

        return jsonify({
            "ok": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
