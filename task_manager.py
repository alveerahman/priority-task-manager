# ---------------------------------------------------------
# Project: Priority-Based Task Manager
# Author: Alvee Rahman (Final Year CSE Student)
# Goal: Demonstrating Sorting Algorithms & Problem Solving
# ---------------------------------------------------------

class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority  # 1 for High, 2 for Medium, 3 for Low

    def __repr__(self):
        p_map = {1: "🔴 High", 2: "🟡 Medium", 3: "🟢 Low"}
        return f"[{p_map[self.priority]}] {self.title}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority):
        if priority not in [1, 2, 3]:
            print("❌ Invalid Priority! Use 1, 2, or 3.")
            return
        new_task = Task(title, priority)
        self.tasks.append(new_task)
        # DSA concept: Sorting the list based on priority value
        self.tasks.sort(key=lambda x: x.priority)
        print(f"✔️ Task '{title}' added and sorted by priority.")

    def show_tasks(self):
        if not self.tasks:
            print("\n📭 Task list is empty.")
            return
        print("\n--- Your Tasks (Sorted by Priority) ---")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def complete_task(self, index):
        try:
            removed = self.tasks.pop(index - 1)
            print(f"✅ Completed: {removed.title}")
        except IndexError:
            print("❌ Invalid task number!")

def main():
    manager = TaskManager()
    
    while True:
        print("\n--- Priority Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task (Delete)")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            t = input("Task Title: ")
            p = int(input("Priority (1-High, 2-Med, 3-Low): "))
            manager.add_task(t, p)
        elif choice == '2':
            manager.show_tasks()
        elif choice == '3':
            manager.show_tasks()
            idx = int(input("Enter task number to complete: "))
            manager.complete_task(idx)
        elif choice == '4':
            print("Keep crushing your goals! Goodbye.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()