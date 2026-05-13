from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory list of tasks (instead of database)
tasks = [{"id": 1, "title": "Learn APIs", "done": False}]


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)  # Returns JSON


@app.route("/tasks", methods=["POST"])
def create_task():
    new_task = request.get_json()  # Get JSON from request body
    new_task["id"] = len(tasks) + 1  # Simple ID
    new_task["done"] = False  # Default
    tasks.append(new_task)  # Save it
    return jsonify(new_task), 201  # Return it + status 201


# GET: Retrieve data
@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify({"message": "Data retrieved successfully"})


# POST: Create new data
@app.route("/api/data", methods=["POST"])
def create_data():
    new_item = request.json  # Get JSON data from request body
    return jsonify({"message": "Item created", "data": new_item}), 201


# PUT: Update existing data
@app.route("/api/data/<int:item_id>", methods=["PUT"])
def update_data(item_id):
    updated_info = request.json
    return jsonify({"id": item_id, "updated_to": updated_info})


# DELETE: Remove data
@app.route("/api/data/<int:item_id>", methods=["DELETE"])
def delete_data(item_id):
    return jsonify({"message": f"Item {item_id} deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
