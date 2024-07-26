from storage import Storage

class TaskManager(Storage):
    """A class to manage tasks, including adding, removing, viewing, and modifying tasks."""
   
    def __init__(self, file = 'task.json'):
        super().__init__(file)
        self.tasks = []
        if self.path.exists():
            self.tasks = super().load()

    def add_task(self, 
                 message: str, 
                 date: str = "not specified", 
                 important: bool = False, 
                 tag: list = None, 
                 completed: bool = False):
        """
        Adds a new task to the task list.
        
        Args:
            message (str): The task description.
            date (str, optional): The due date of the task. Defaults to "not specified".
            important (bool, optional): Marks the task as important. Defaults to False.
            tag (list, optional): A list of tags associated with the task. Defaults to an empty list.
            completed (bool, optional): Marks the task as completed. Defaults to False.
        """
        num = len(self.tasks) + 1
        self.tasks.append({
            "Task ID": f"Task {num}",
            "Message": message,
            "Due": date,
            "Important": important,
            "Tag": tag,
            "Completed": completed
        })
        super().save(self.tasks)

    def remove_task(self, task_id: str):
        """
        Removes a task from the task list.
        
        Args:
            task_id (str): The identifier of the task to be removed.
        """
        try:
            num = int(task_id.split(" ")[-1]) - 1
            self.tasks.pop(num)
            super().save(self.tasks)
        except (IndexError, ValueError) as e:
            print(f"Error removing task: {e}")

    def view_tasks(self, filter: str = ""):
        """
        Lists tasks based on the specified filter.
        
        Args:
            filter (str, optional): The filter for viewing tasks. Can be empty for active tasks or "Completed" for completed tasks. Defaults to an empty string.
        """
        temp_list = []
        if filter == "":
            temp_list = [task for task in self.tasks if not task["Completed"]]
        elif filter == "Completed":
            temp_list = [task for task in self.tasks if task["Completed"]]
        
        for task in temp_list:
            for key, value in task.items():
                print(f"{key}: {value}")
            print("-" * 20)

    def modify_task(self, task_id: str, key: str, new_value: any):
        """
        Modifies a specified task's attribute.
        
        Args:
            task_id (str): The identifier of the task to be modified.
            key (str): The key of the task attribute to modify.
            new_value (any): The new value for the specified key.
        """
        try:
            num = int(task_id.split(" ")[-1]) - 1
            if key in self.tasks[num]:
                self.tasks[num][key] = new_value
                super().save(self.tasks)
            else:
                print(f"Invalid key: {key}")
        except (IndexError, ValueError) as e:
            print(f"Error modifying task: {e}")
