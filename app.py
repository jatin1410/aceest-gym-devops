from flask import Flask, jsonify, request

app = Flask(__name__)

members = []

@app.route("/")
def home():
    return jsonify({"message": "Welcome to ACEest Fitness & Gym API"})


@app.route("/health")
def health_check():
    return jsonify({"status": "API is running"})


@app.route("/programs")
def programs():
    programs = [
        {"name": "Fat Loss Program", "duration": "12 weeks"},
        {"name": "Muscle Gain Program", "duration": "16 weeks"},
        {"name": "General Fitness Program", "duration": "8 weeks"}
    ]
    return jsonify(programs)


@app.route("/members", methods=["GET"])
def get_members():
    return jsonify(members)


@app.route("/members", methods=["POST"])
def add_member():
    data = request.json

    member = {
        "name": data.get("name"),
        "age": data.get("age"),
        "goal": data.get("goal")
    }

    members.append(member)

    return jsonify({"message": "Member added successfully", "member": member})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)