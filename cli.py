from task import TaskManager


def main():
    task_manager = TaskManager()

    while True:
        command = input("Enter a command: ")
        if "task add" in command:
            if "--" in command:
                first_split = command.split("task add", 1)
                second_split = first_split[1].split("--")
                note = second_split.pop(0).strip()
                task_manager.add_task(message = note)
                task_id = task_manager.tasks[-1]["Task ID"]
                for com in second_split:
                    if "due" in com:
                        due = com.split("due")
                        due = due[1].strip()
                        task_manager.modify_task(task_id, "Due", due)
                    if "tag" in com:
                        tag = com.split("tag ", 1)
                        tag = tag[1].split(",")
                        task_manager.modify_task(task_id, "Tag", tag)
                    if "important" in com:
                        yes = True
                        task_manager.modify_task(task_id, "Important", yes)
                print("Task successfully created.")                
            else:
                message = command.split("task add", 1)
                todo = str(message[-1].strip())
                task_manager.add_task(message=todo)
                print("Task successfully created.")

        elif "task list completed"  in command:
            task_manager.view_tasks(filter = "Completed")
      
        elif "task list" in command:
            task_manager.view_tasks()
            
        elif "task delete" in command:
            message = command.split("task delete", 1)
            task_id = str(message[-1].strip())
            task_manager.remove_task(task_id)
            print(f"{task_id.title()} has been been deleted")
        elif command == "task purge":
            confirm = input("Are you sure you want do delete all task? Yes/No? ")
            if confirm.lower() == "yes":
                task_manager.tasks = []
                task_manager.save(task_manager.tasks)
                print("Purge was successful")

        elif "task update" in command:
            message = command.split(" ", 4)
            task_id = f"{message[2]} {message[3]}"
            key = "Message"
            new_value = message[4].strip()
            task_manager.modify_task(task_id, key, new_value)
            print(f"{key} has been successfully modified.")

        elif "task complete" in command:
            message = command.split("task complete", 1)
            task_id = message[-1].strip()
            key = "Completed"
            new_value = True
            task_manager.modify_task(task_id, key, new_value)
        
        elif command == "exit":
            break


if __name__ == '__main__':
    main()
