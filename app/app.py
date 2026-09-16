from flask import Flask, jsonify, request
import pandas as pd
from pathlib import Path

app = Flask(__name__)

PREDICTIONS_FILE = Path(__file__).resolve().parent.parent / "predictions.csv"


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/predictions")
def predictions():
    week = request.args.get("week")

    if not week:
        return jsonify({"error": "week parameter is required"}), 400

    if not PREDICTIONS_FILE.exists():
        return jsonify({"error": "predictions.csv not found"}), 500

    df = pd.read_csv(PREDICTIONS_FILE)

    result = df[df["week_start"].astype(str) == week]

    if result.empty:
        return jsonify({"error": f"No predictions found for week {week}"}), 404

    return jsonify(result.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
