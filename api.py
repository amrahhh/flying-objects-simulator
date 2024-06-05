from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

log_data = []
with open("simulation.log", "r") as file:
    for line in file:
        try:
            log_entry = json.loads(line)
            log_data.append(log_entry)
        except json.JSONDecodeError:
            continue


@app.route("/trajectory", methods=["GET"])
def get_trajectory():
    object_id = request.args.get("object_id")
    start_time = datetime.fromisoformat(request.args.get("start_time"))
    end_time = datetime.fromisoformat(request.args.get("end_time"))

    trajectory = []
    for entry in log_data:
        entry_time = datetime.fromisoformat(entry["timestamp"])
        if (
            entry["object_data"]["object_id"] == object_id
            and start_time <= entry_time <= end_time
        ):
            trajectory.append(entry)

    print(f"Query for object_id {object_id} from {start_time} to {end_time}")
    print(f"Found {len(trajectory)} matching entries")
    return jsonify(trajectory)


@app.route("/snapshot", methods=["GET"])
def get_snapshot():
    sector_id = request.args.get("sector_id")
    start_time = datetime.fromisoformat(request.args.get("start_time"))
    end_time = datetime.fromisoformat(request.args.get("end_time"))

    snapshot = []
    for entry in log_data:
        entry_time = datetime.fromisoformat(entry["timestamp"])
        if (
            entry["object_data"]["sector"] == sector_id
            and start_time <= entry_time <= end_time
        ):
            snapshot.append(entry)

    print(f"Query for sector_id {sector_id} from {start_time} to {end_time}")
    print(f"Found {len(snapshot)} matching entries")
    return jsonify(snapshot)


if __name__ == "__main__":
    app.run(debug=True)
