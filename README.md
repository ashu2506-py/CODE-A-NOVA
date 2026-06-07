# 📝 To-Do List CLI Application

A simple and interactive Command Line Interface (CLI) To-Do List application built with Python. This application helps users manage their daily tasks efficiently through a menu-driven interface directly from the terminal.

## 🚀 Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Simple and user-friendly CLI interface
- Lightweight and beginner-friendly Python project

## 📸 Demo

```text
========= To Do List =========

1. Add Task
2. View Task
3. Complete Task
4. Delete Task
5. Exit

Enter your choice: 1

Enter your task: Learn Python
Task Added Successfully
```

## 🛠️ Built With

- Python 3
- Lists
- Dictionaries
- Loops
- Conditional Statements

## 📂 Project Structure

```text
todo-app/
│
├── todo.py
└── README.md
```

## ⚙️ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/ashu2506-py/CODE-A-NOVA/tree/main/ToDoList
```

### 2. Navigate to the Project Directory

```bash
cd todo-app
```

### 3. Run the Application

```bash
python todo.py
```

or

```bash
python3 todo.py
```

## 📖 How It Works

Each task is stored as a dictionary:

```python
{
    "task": "Learn Python",
    "completed": False
}
```

All tasks are maintained inside a list:

```python
tasks = []
```

### Add Task

Creates a new task and stores it in memory.

### View Tasks

Displays all tasks along with their completion status.

```text
1. [ ] Learn Python
2. [✓] Complete DSA Sheet
3. [ ] Build Portfolio
```

### Complete Task

Marks a selected task as completed.

### Delete Task

Removes a selected task from the task list.

## 🎯 Learning Objectives

This project demonstrates the use of:

- Variables and Data Types
- Lists and Dictionaries
- Loops (`while`, `for`)
- Conditional Statements (`if-elif-else`)
- User Input Handling
- Basic CRUD Operations
- CLI Application Development

## 🔮 Future Enhancements

- Persistent task storage using JSON
- Edit existing tasks
- Task priorities
- Due dates and reminders
- Search and filter tasks
- Colored terminal output
- Object-Oriented Programming (OOP) version
- Export tasks to CSV

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to fork the repository and submit a pull request.

## 👨‍💻 Author

**Ashutosh Singh**

Python Developer | Problem Solver | Technology Enthusiast

---

If you found this project helpful, consider giving it a ⭐ on GitHub!