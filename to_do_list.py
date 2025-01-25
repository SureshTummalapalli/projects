class TodoList:
    def __init__(self):  # Initialize an empty task list
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: '{task}'")

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print(f"Removed task: '{task}'")
                return
        print(f"Task '{task}' not found.")

    def mark_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print(f"Marked task '{task}' as completed.")
                return
        print(f"Task '{task}' not found.")

    def display_tasks(self):
        if self.tasks:
            print("Task List:")
            for i, t in enumerate(self.tasks, start=1):
                status = "Done" if t["completed"] else "Pending"
                print(f"{i}. {t['task']} - {status}")
        else:
            print("No tasks to show.")

def main():
    todo = TodoList()
    menu = """
TODO LIST MENU:
1. Add a task
2. Remove a task
3. Mark a task as completed
4. Display tasks
5. Exit
"""
    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            task = input("Enter task to add: ").strip()
            todo.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ").strip()
            todo.remove_task(task)
        elif choice == '3':
            task = input("Enter task to mark as completed: ").strip()
            todo.mark_completed(task)
        elif choice == '4':
            todo.display_tasks()
        elif choice == '5':
            print("Ok,bye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()