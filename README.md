# Task Tracker CLI

A simple command-line interface (CLI) application to track and manage your tasks. This project was built to practice file system interactions and handling user inputs in Python without external libraries.

### Features
Create Tasks: Add new tasks with a description.

Update Tasks: Modify the description of existing tasks.

Delete Tasks: Remove tasks by their unique ID.

Status Management: Mark tasks as todo, in-progress, or done.

Filtered Listing: List all tasks or filter them by their current status.

Automatic Timestamps: Tracks when tasks are created and last updated.

### Requirements

Python 3.x

No external libraries are required (uses native `argparse`, `json`, and `os` modules).

### Installation
#### Clone this repository:

    git clone https://github.com/JoWillian/task-tracker-cli.git
#### Navigate to the project directory:

    cd task-tracker-cli
#### Usage

### The application uses positional arguments to accept user commands.

#### Adding a new task

    python main.py add "Buy groceries"
#### Updating and deleting tasks

    python main.py update 1 "Buy groceries and cook dinner"
    python main.py delete 1
#### Marking tasks

    python main.py mark-in-progress 1
    python main.py mark-done 1

#### Listing tasks

#### List all tasks

    python main.py list

#### List by status

    python main.py list done
    python main.py list todo
    python main.py list in-progress

## Project Structure

***main.py:*** Contains the CLI logic and argument parsing.

***storage.py:*** Handles reading and writing to the `tasks.json` file.

***tasks.json:*** The local database for storing task information.

### My Journey with this Project

To be honest, this is my first project since graduating from college. I decided to escape "tutorial hell" and build something on my own, which meant I had to learn almost everything while I was doing it.

### What I learned:

***Argparse:*** This was completely new to me. After struggling with it for a while, I learned how to use `subparsers` to create separate commands for adding, updating, and deleting tasks.

***Storage Logic:*** I moved the "magic" to `storage.py`. I wrote the `save_tasks` and `load_tasks` functions to handle the `json` list and ensure the file is created if it doesn't exist. I had to research the `json` and `os` libraries extensively to make this work.

***Technical Challenges:*** Moving back to `main.py`, I tackled several challenges that improved my skills, such as moving the save function outside of loops to make the app faster.

***Data & IDs:*** I learned that I shouldn't just use `len() + 1` for IDs. Instead, I used `max() + 1` to ensure every ID is unique, even after a task is deleted.

***JSON Constraints:*** I discovered that `json` doesn't support Python `datetime` objects naturally. I solved this by formatting timestamps into strings using `.strftime("%d/%m/%Y %H:%M:%S")` before saving.

I hope you appreciate my first project. Thank you!

### References:
Project Link: https://roadmap.sh/projects/task-tracker