from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
from celery_worker import process_csv_task
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "uploads/"
RESULT_FOLDER = "results/"
ALLOWED_EXTENSIONS = {"csv"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESULT_FOLDER"] = RESULT_FOLDER

# Helper function to check if file has allowed extension


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/api/upload", methods=["POST"])
def upload_csv():
    creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Check if a file is included in the request
    if "csvFile" not in request.files:
        return jsonify({"error": "No CSV file provided"}), 400

    file = request.files["csvFile"]

    # Check if a file with a valid filename and extension is uploaded
    if file.filename == "" or not allowed_file(file.filename):
        return jsonify({"error": "Invalid or missing CSV file"}), 400

    filename = secure_filename(file.filename)

    # Create file path by joining upload folder, filename, and current date/time
    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"], filename.replace(".csv", creation_date + ".csv")
    )

    # Save the uploaded file
    file.save(file_path)

    # Generate a task ID
    task_id = process_csv_task.delay(
        file_path,
        app.config["RESULT_FOLDER"]
        + filename.replace(".csv", creation_date + "_output.csv"),
    ).id

    return jsonify({"task_id": task_id}), 200


@app.route("/api/result/<task_id>", methods=["GET"])
def get_result(task_id):
    # Check if the task ID is valid
    result = process_csv_task.AsyncResult(task_id)
    if not result.ready():
        return jsonify({"status": str(result.state)}), 200

    # Check if the output CSV file exists
    if not os.path.exists(result.get()):
        return jsonify({"error": "Result not available"}), 404

    # Send the output CSV file as a download
    return send_file(result.get(), as_attachment=True, mimetype="text/csv")


if __name__ == "__main__":
    app.run()
