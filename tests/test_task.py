from task import TaskManager


def test_add_task():
    message = "This is a sample task"
    task_1 = TaskManager()
    task_1.add_task(message)
    assert message == task_1.tasks[-1]["Message"]

def test_remove_task():
    message = "This should be removed."
    task_1 = TaskManager()
    task_1.add_task(message)
    task_id = task_1.tasks[-1]["Task ID"]
    task_1.remove_task(task_id)
    for task in task_1.tasks: 
        assert task_id != task_1.tasks

def test_modify_task():
    message = "This is a sample task."
    task_1 = TaskManager()
    task_1.add_task(message)
    task_id = task_1.tasks[-1]["Task ID"]
    key = "Message"
    new_value = "This is the new sample task"
    task_1.modify_task(task_id = task_id, key = key, new_value = new_value)
    assert new_value == task_1.tasks[-1]["Message"]




