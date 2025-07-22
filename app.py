from flask import Flask, request, jsonify
import os

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

    result = {
        "filename": video_file.filename,
        "size_MB": round(os.path.getsize(save_path) / 1024 / 1024, 2),
        "status": "✅ Video received and saved successfully"
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
