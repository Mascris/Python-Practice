# 🐍 Python Development Portfolio

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQL](https://img.shields.io/badge/sql-database-blue?style=for-the-badge&logo=postgresql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Development-success?style=for-the-badge)

> A structured collection of Python backend systems, focusing on Object-Oriented Programming (OOP) and SQL Database integration.

## 📂 Project Modules

This repository showcases my ability to build modular, scalable Python applications.

| Category | Module | Description |
| :--- | :--- | :--- |
| **⚔️ OOP Systems** | `rpg-store` | A virtual item shop using classes, inheritance, and inventory management. |
| **🗄️ Databases** | `shop-sql` | A full CRUD application integrating Python with MSSQL/SQLite. |
| **🧩 Algorithms** | `randomness` | Logic puzzles and probability simulations to sharpen problem-solving skills. |
| **🏗️ Architecture** | `OOP-Project` | Demonstration of SOLID principles and class structures in Python. |

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
