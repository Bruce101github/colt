from storage import Storage
from utils import TerminalColor


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
        if temp_list == []:
            print("No tasks available")
        else:
            for task in temp_list:
                date = task["Due"] 
                tags = task["Tag"]
                important = task["Important"]
                output = f"{TerminalColor.RED}{TerminalColor.BOLD}{task["Task ID"]}{TerminalColor.RESET}: {TerminalColor.BRIGHT_WHITE}{task["Message"]}{TerminalColor.RESET}"

                print("-" * 30)
                if important:
                    output += f"{TerminalColor.YELLOW}!!!{TerminalColor.RESET}"
                if date != "not specified":
                    output += f"\n{TerminalColor.BRIGHT_BLACK}{date}  "
                if tags != None:
                    if date == "not specified":
                        output += f"\n"
                    for tag in tags:
                        output += f"{TerminalColor.BRIGHT_CYAN}#{tag}{TerminalColor.RESET} "
                print(output)
            print("-" * 30)

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

    def search_task(self, keyword: any, key: str = "Message"):
        temp_list = self.tasks[:]
        if key == "Important":
            found = [task for task in temp_list if task[key] is True]
            result = len(found)
            
            print(f"\nFound {TerminalColor.BRIGHT_GREEN}{result}{TerminalColor.RESET} matching results.")

            for task in found:
                date = task["Due"] 
                tags = task["Tag"]
                important = task["Important"]
                output = f"{TerminalColor.RED}{TerminalColor.BOLD}{task["Task ID"]}{TerminalColor.RESET}: {TerminalColor.BRIGHT_WHITE}{task["Message"]}{TerminalColor.RESET}"
        
                #print(f"\nFound {TerminalColor.BRIGHT_GREEN}{result}{TerminalColor.RESET} matching results.")
                print("-" * 30)
                if important:
                    output += f"{TerminalColor.YELLOW}!!!{TerminalColor.RESET}"
                if date != "not specified":
                    output += f"\n{TerminalColor.BRIGHT_BLACK}{date}  "
                if tags != None:
                    if date == "not specified":
                        output += f"\n"
                    for tag in tags:
                        output += f"{TerminalColor.BRIGHT_CYAN}#{tag}{TerminalColor.RESET} "
                print(output)
            print("-" * 30 + "\n")

        elif key == "Tag":
            found = []
            for task in temp_list:
                check = True
                for i in keyword:
                    if i not in task["Tag"]:
                        check = False
                if check == True:
                    found.append(task)
            result = len(found)
            
            print(f"\nFound {TerminalColor.BRIGHT_GREEN}{result}{TerminalColor.RESET} matching results.")

            for task in found:
                date = task["Due"] 
                tags = task["Tag"]
                important = task["Important"]
                output = f"{TerminalColor.RED}{TerminalColor.BOLD}{task["Task ID"]}{TerminalColor.RESET}: {TerminalColor.BRIGHT_WHITE}{task["Message"]}{TerminalColor.RESET}"
        
                #print(f"\nFound {TerminalColor.BRIGHT_GREEN}{result}{TerminalColor.RESET} matching results.")
                print("-" * 30)
                if important:
                    output += f"{TerminalColor.YELLOW}!!!{TerminalColor.RESET}"
                if date != "not specified":
                    output += f"\n{TerminalColor.BRIGHT_BLACK}{date}  "
                if tags != None:
                    if date == "not specified":
                        output += f"\n"
                    for tag in tags:
                        output += f"{TerminalColor.BRIGHT_CYAN}#{tag}{TerminalColor.RESET} "
                print(output)
            print("-" * 30 + "\n")




        else:
            found = [task for task in temp_list if keyword in task[key]]
            result = len(found)
            
            print(f"\nFound {TerminalColor.BRIGHT_GREEN}{result}{TerminalColor.RESET} matching results.")

            for task in found:
                task[key] = task[key].replace(keyword, f"{TerminalColor.BRIGHT_GREEN}{keyword}{TerminalColor.RESET}")
                date = task["Due"] 
                tags = task["Tag"]
                important = task["Important"]
                output = f"{TerminalColor.RED}{TerminalColor.BOLD}{task["Task ID"]}{TerminalColor.RESET}: {TerminalColor.BRIGHT_WHITE}{task["Message"]}{TerminalColor.RESET}"
        
                #print(f"\nFound {TerminalColor.BRIGHT_GREEN}{result}{TerminalColor.RESET} matching results.")
                print("-" * 30)
                if important:
                    output += f"{TerminalColor.YELLOW}!!!{TerminalColor.RESET}"
                if date != "not specified":
                    output += f"\n{TerminalColor.BRIGHT_BLACK}{date}  "
                if tags != None:
                    if date == "not specified":
                        output += f"\n"
                    for tag in tags:
                        output += f"{TerminalColor.BRIGHT_CYAN}#{tag}{TerminalColor.RESET} "
                print(output)
                task[key] = task[key].replace(keyword, f"{TerminalColor.BRIGHT_WHITE}{keyword}")
            print("-" * 30 + "\n")





