# -*- coding: utf-8 -*-
"""
 To Do List App
"""

import os

file_name = "tasks.txt"


def load_tasks():
    # If the file doesn't exist yet, just return an empty list
    if not os.path.exists(file_name):
        return []
    with open(file_name, "r") as f:
        tasks = [line.strip() for line in f if line.strip()]
    return tasks


def save_tasks(tasks):
    with open(file_name, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def view_tasks(tasks):
    if not tasks:
        print("\nno tasks yet")
        return
    print("\nyour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"  {i}. {task}")


def add_task(tasks):
    task = input("\nenter task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("task added!")
    else:
        print("you didnt type anything")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\nwhich task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"deleted: {removed}")
        else:
            print("that number doesnt exist")
    except ValueError:
        print("type a number please")


def clear_all(tasks):
    confirm = input("\nsure you want to clear everything? (yes/no): ").strip().lower()
    if confirm in ("yes", "y"):
        tasks.clear()
        save_tasks(tasks)
        print("all cleared")
    else:
        print("cancelled")


def main():
    print("=== To-Do List ===")
    tasks = load_tasks()

    while True:
        print("\n1. view tasks")
        print("2. add task")
        print("3. delete task")
        print("4. clear all")
        print("5. quit")

        choice = input("\nchoice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            clear_all(tasks)
        elif choice == "5":
            print("bye!")
            break
        else:
            print("invalid, pick 1-5")


main()