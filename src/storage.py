import json
import os

# Load existing tasks or return an empty list
DATA_FILE = os.path.join("..", "data", "tasks.json")

def load_tasks():
    # Safety Check: If the file doesn't exist, return an empty list
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # If the file is empty or corrupted, return an empty list
            return []

def save_tasks(tasks):
    # Ensure the 'data' directory exists
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
