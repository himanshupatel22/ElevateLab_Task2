"""
To-Do List Application
A simple console-based task manager with persistent storage
"""

import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file into a list"""
    tasks = []
    try:
        # Check if file exists
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                for line in file:
                    # Remove whitespace and newline characters
                    task = line.strip()
                    if task:  # Only add non-empty tasks
                        tasks.append(task)
    except Exception as e:
        print(f"Error loading tasks: {e}")
    return tasks

def save_tasks(tasks):
    """Save tasks list to file"""
    try:
        with open(TASKS_FILE, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
        print("✓ Tasks saved successfully!")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def view_tasks(tasks):
    """Display all tasks with numbering"""
    if not tasks:
        print("\n📋 Your to-do list is empty!")
    else:
        print("\n📋 Your To-Do List:")
        print("-" * 40)
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print("-" * 40)
        print(f"Total tasks: {len(tasks)}")

def add_task(tasks):
    """Add a new task to the list"""
    task = input("\nEnter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"✓ Task '{task}' added successfully!")
        save_tasks(tasks)
    else:
        print("✗ Task cannot be empty!")

def remove_task(tasks):
    """Remove a task from the list"""
    if not tasks:
        print("\n✗ No tasks to remove!")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"✓ Task '{removed_task}' removed successfully!")
            save_tasks(tasks)
        else:
            print("✗ Invalid task number!")
    except ValueError:
        print("✗ Please enter a valid number!")
    except Exception as e:
        print(f"✗ Error: {e}")

def update_task(tasks):
    """Update an existing task"""
    if not tasks:
        print("\n✗ No tasks to update!")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter new task description: ").strip()
            if new_task:
                old_task = tasks[task_num - 1]
                tasks[task_num - 1] = new_task
                print(f"✓ Task updated from '{old_task}' to '{new_task}'!")
                save_tasks(tasks)
            else:
                print("✗ Task cannot be empty!")
        else:
            print("✗ Invalid task number!")
    except ValueError:
        print("✗ Please enter a valid number!")
    except Exception as e:
        print(f"✗ Error: {e}")

def clear_all_tasks(tasks):
    """Clear all tasks after confirmation"""
    if not tasks:
        print("\n✗ No tasks to clear!")
        return
    
    confirm = input("\n⚠️  Are you sure you want to delete all tasks? (yes/no): ").lower()
    if confirm == 'yes':
        tasks.clear()
        save_tasks(tasks)
        print("✓ All tasks cleared!")
    else:
        print("✗ Operation cancelled!")

def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 40)
    print("     TO-DO LIST MANAGER")
    print("=" * 40)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Update Task")
    print("5. Clear All Tasks")
    print("6. Exit")
    print("=" * 40)

def main():
    """Main function to run the to-do list application"""
    print("\n🎯 Welcome to To-Do List Manager!")
    
    # Load existing tasks
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            update_task(tasks)
        elif choice == '5':
            clear_all_tasks(tasks)
        elif choice == '6':
            print("\n👋 Thank you for using To-Do List Manager!")
            print("Goodbye!")
            break
        else:
            print("\n✗ Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main()