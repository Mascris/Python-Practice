class Task:
    def __init__(self,description: str, due_date: str, is_completed=False) -> None:
        self.description = description
        self.due_date = due_date
        self.is_completed = is_completed

    def mark_as_completed(self):
        self.is_completed = True

    def display_task(self):
        status = "✔ Completed" if self.is_completed else "⏳ Pending"
        print(f"Task: {self.description} | Due: {self.due_date} | Status: {status}")

class TaskManager:
    def __init__(self) -> None:
        self.task = []
    def add_tasks(self,description,due_date):
        task = Task(description,due_date)
        self.task.append(task)

    def view_all_tasks(self):
        for task in self.task:
            task.display_task()

    def view_pending_task(self):
        for task in self.task:
            if not task.is_completed:
                task.display_task()

    def mark_as_completed(self,description):
        for task in self.task:
            if task.description == description:
                task.mark_as_completed()
                print(f"task '{description}' marked as completed")
                return
        print(f"task '{description}' not found")

    def delete_task(self,description):
        for task in self.task:
            if task.description == description:
                self.task.remove(task)
                print(f"'{description}' deleted")
                return
        print(f"task {description} found")

if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Add task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. Complete a task")
        print("5. Delete a task")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            desc = input("task description:")
            date = input("due date (YYYY-MM-DD)")

        elif choice == "2":
            manager.view_all_tasks()

        elif choice == "3":
            manager.view_pending_task()

        elif choice == "4":
            manager.mark_as_completed()

        elif choice=="5":
            desc = input("task description to delete:")
            manager.delete_task(desc)

        elif choice == "6":
            print("GoodBye")
            break

        else:
            print("invalid option try again!")
                
