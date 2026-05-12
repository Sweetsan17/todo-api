from flask import Flask, jsonify
from flask import request   # Add this to the imports

app = Flask(__name__)

# In-memory list of tasks (instead of database)
tasks = [
    {"id": 1, "title": "Learn APIs", "done": False}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)  # Returns JSON

@app.route('/tasks', methods=['POST'])
def create_task():
    new_task=request.get_json() # Get JSON from request body
    new_task['id']=len(tasks)+1  # Simple ID
    new_task['done']=False  # Default
    tasks.append(new_task) # save it the tasks
    return jsonify(new_task),201 # Return it + status 201

if __name__ == '__main__':
    app.run(debug=True)