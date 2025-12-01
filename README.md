    
# 🐍 Python Development Portfolio

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQL](https://img.shields.io/badge/sql-database-blue?style=for-the-badge&logo=postgresql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Development-success?style=for-the-badge)

> A structured collection of Python backend systems, focusing on Object-Oriented Programming (OOP) and SQL Database integration.

## 📂 Project Structure

This repository is organized into modules based on complexity and concept:

| Folder | Contents | Description |
| :--- | :--- | :--- |
| **📂 01_Basic_Scripts** | `randomness` | Logic puzzles, probability simulations, and algorithms. |
| **📂 02_OOP_Systems** | `rpg-store`, `OOP-Project` | Virtual shop systems using classes, inheritance, and SOLID principles. |
| **📂 03_Database_SQL** | `shop-sql`, `py-mssql` | Full CRUD applications integrating Python with MSSQL & SQLite. |
| **🧪 Prototypes** | `idea` | Experimental scripts and scratchpad code for testing new concepts. |

## 💻 Code Showcase: SQL Integration

*Example of how I handle database connections safely:*

```python
import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def fetch_users(self):
        query = "SELECT * FROM users WHERE active = 1"
        self.cursor.execute(query)
        return self.cursor.fetchall()
        
    def close(self):
        self.conn.close()

  

🛠️ Tech Stack

    Languages: Python 3.10+

    Databases: MSSQL, SQLite

    Concepts: OOP, CRUD Operations, API Logic

    Libraries: pymssql, random, datetime

🚀 How to Run

    Clone the repository:
    code Bash

    
git clone https://github.com/Mascris/Python-Portfolio.git

  

(Note: If you haven't renamed the repo yet, use Python-Practice.git instead)

Navigate to a module (e.g., the RPG Store):
code Bash

        
    cd 02_OOP_Systems/rpg-store
    python main.py

      

<p align="center">
<b>Constantly refactoring and improving code quality.</b>
</p>
```
