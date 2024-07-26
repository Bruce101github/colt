from pathlib import Path
import json

# task_manager = TaskManager()
# path = Path('task.json')
#
# if path.exists():
#     contents = path.read_text()
#     task_manager.tasks = json.loads(contents)
#
# else:
#     contents = json.dumps(task_manager.tasks)
#     path.write_text(contents)


class Storage:
    """A classs to handle storage and persisitence"""

    def __init__(self, file = 'task.json'):
        self.file = file
        self.path = Path(file)


    def save(self, tasks: list):
        """Code to save tasks to a file (e.g., JSON format)"""
        contents = json.dumps(tasks)
        self.path.write_text(contents)

    def load(self, tasks: list):
        """Code to load tasks from a file"""
        try:
            contents = self.path.read_text()
        except FileNotFoundError:
            print(f"Failed to load storage.{self.file} does not exist")
        else:
            tasks = json.loads(contents)

    # def update(self, tasks: list):
    #     """Code to update a specific task""


