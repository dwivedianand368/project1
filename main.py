class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}, Completed: {task.completed}")

    def complete_task(self, task_index):
        self.tasks[task_index].completed = True

    def update_task(self, task_index, description, due_date, priority):
        task = self.tasks[task_index]
        task.description = description
        task.due_date = due_date
        task.priority = priority

    def remove_task(self, task_index):
        del self.tasks[task_index]

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. Display Tasks\n3. Complete Task\n4. Update Task\n5. Remove Task\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority: ")
            todo_list.add_task(Task(description, due_date, priority))
            print("Task added successfully.")

        elif choice == '2':
            todo_list.display_tasks()

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.complete_task(task_index)
            print("Task marked as completed.")

        elif choice == '4':
            task_index = int(input("Enter the task number to update: ")) - 1
            description = input("Enter new description: ")
            due_date = input("Enter new due date: ")
            priority = input("Enter new priority: ")
            todo_list.update_task(task_index, description, due_date, priority)
            print("Task updated successfully.")

        elif choice == '5':
            task_index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(task_index)
            print("Task removed successfully.")

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
