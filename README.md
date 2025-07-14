# python-calculator

Remake of my C# Data Structures Calculator Project — now written in Python with improved functionality, state management, and file persistence.

## Project Overview

This project is a terminal-based calculator rebuilt from my original **CSCI 2210 - Data Structures Project 7** (originally in C#/.NET). The goal was to demonstrate proficiency with Python fundamentals, including:

* Dictionaries (dispatch tables)
* OOP principles (separation of concerns)
* File I/O for persistent variable storage
* Stack operations for undo functionality

It offers a clean CLI interface for both technical and non-technical users, along with robust state handling and variable storage across sessions.

## Features

### Core Math Operations:

* Addition, Subtraction, Multiplication, Division
* Modulus, Squaring, Square Root, Exponentiation
* Factorials
* Fibonacci number calculation (based on current state)

### State Management:

* Previous Answer auto-saves between operations
* Undo functionality to revert last operation
* Clear State to reset current answer to zero

### Variable Handling:

* Create and store named variables (lowercase names only)
* Set current state to any previously stored variable
* Reference stored variables within calculations

### File Persistence:

* Save variables to a JSON file (`variables.json`)
* Load variables from file on program start

## Project Structure

```
python-calculator/
│
├── main.py            # Entry point with CLI menu loop
├── calculator.py      # Calculator logic and operations
├── file_manager.py    # File I/O operations for variable persistence
└── variables.json     # Persistent storage of variables
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-calculator.git
cd python-calculator
```

### 2. Install Python (3.11+ Recommended)

### 3. Run the Calculator

```bash
python main.py
```

## Educational Purpose

This project is a remake of my Data Structures final project, modernized in Python to reinforce:

* OOP design patterns
* File handling in Python
* Practical use of dispatch tables
* Clean separation of logic vs. interface

## Future Goals (Stretch Ideas):

* Reverse Polish Notation (RPN) parsing (future)
* Graphical User Interface (GUI) with Tkinter (in progress)
* Web App deployment (future consideration)

## Author

**Christopher Bragg**
Bachelor of Science in Computing, Concentration in Computer Science
East Tennessee State University (Magna Cum Laude, 2024)
