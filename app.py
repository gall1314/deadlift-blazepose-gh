from flask import Flask, request, jsonify
import os
from deadlift_analysis import run_deadlift_analysis  # שים לב שאתה צריך את הפונקציה הזו בקוד שלך

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ API is alive and running on RunPod"

@app.route("/analyze", methods=["POST"])
def analyze():
    if "video" not in request.files:
        return jsonify({"error": "No video file uploaded"}), 400

    video_file = request.files["video"]
    save_path = "/tmp/uploaded_video.mp4"
    video_file.save(save_path)

    # הרצת ניתוח על הוידאו עם הפונקציה שלך
    result = run_deadlift_analysis(save_path)

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
