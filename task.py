class TaskManager:
    """A class to manage tasks, including adding, removing, viewing, and modifying tasks."""
   
    def __init__(self):
        self.tasks = []

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
