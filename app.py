from flask import Flask, request, jsonify
from deadlift_analysis import run_deadlift_analysis

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'video' not in request.files:
        return jsonify({"error": "No video file uploaded"}), 400

    file = request.files['video']
    filepath = "temp.mp4"
    file.save(filepath)
    result = run_deadlift_analysis(filepath)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
