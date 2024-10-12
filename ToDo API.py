from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
tasks = [
    {"id": 1, "task": "Learn Python APIs", "done": False},
    {"id": 2, "task": "Build a To-Do API", "done": False},
]

# Endpoint to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# Endpoint to add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json.get('task')
    if new_task:
        task = {
            "id": len(tasks) + 1,
            "task": new_task,
            "done": False
        }
        tasks.append(task)
        return jsonify({"message": "Task added", "task": task}), 201
    return jsonify({"message": "Task is required"}), 400

# Endpoint to delete a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        tasks.remove(task)
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"message": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
