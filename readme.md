# 📚 Personal Library & Reading Tracker

A Python-based command-line application that helps users manage their personal book collection, track reading progress, and view reading statistics.

## 🚀 Features

- **Add Books:** Add books with title, author, genre, and total pages.
- **View Books:** Display all books in your library.
- **Search Books:** Search books by title or author.
- **Filter Books:** Filter books by genre or reading status.
- **Reading Progress:** Update the current page of a book.
- **Mark as Finished:** Mark books as completed and automatically record the finish date.
- **Remove Books:** Remove books from your collection.
- **Reading Statistics:** View total books, books finished this year, average pages per finished book, and favorite genre.
- **JSON Persistence:** Save and load book information using a JSON file, so your data remains available after restarting the application.

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON
- Python Standard Library

## 📂 Project Structure

```text
Personal-lib-reading-tracker-cli/
│
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── library.py
│   ├── storage.py
│   └── cli.py
│
├── data.json
├── main.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd Personal-lib-reading-tracker-cli
```

### 3. Run the Application

```bash
python main.py
```

**Requirement:** Python 3.10 or later.

No external Python packages are required.

## 💻 Application Menu

```text
========== PERSONAL LIBRARY TRACKER ==========

1. Add a Book
2. View All Books
3. Search Books
4. Filter Books
5. Update Reading Progress
6. Mark Book as Finished
7. Remove a Book
8. View Statistics
0. Exit

==============================================
```

## 📖 Reading Status

Books can have three reading statuses:

| Status | Description |
|---|---|
| `to-read` | Book has not been started |
| `reading` | Book is currently being read |
| `finished` | Book has been completed |

## 💾 Data Storage

The application uses JSON for persistent data storage.

- `write_data()` converts Book objects into dictionaries and saves them.
- `read_data()` loads saved JSON data and reconstructs Book objects.
- `ensure_file_exists()` creates the JSON file if it does not exist.
- `to_dict()` and `from_dict()` handle conversion between Book objects and dictionaries.

Example JSON data:

```json
[
    {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "genre": "Programming",
        "total_pages": 500,
        "current_page": 150,
        "status": "reading",
        "finish_date": null
    }
]
```

## 🧠 Concepts Practiced

This project demonstrates practical use of:

- Classes and Objects
- Constructors (`__init__`)
- Instance methods and `self`
- Class methods (`@classmethod`)
- Type hints
- List comprehensions
- Exception handling (`try-except`)
- Match-case statements
- File handling
- JSON serialization and deserialization
- Date and time handling
- Modular Python programming

## 🎯 Project Objective

The objective of this project is to apply Python programming and Object-Oriented Programming concepts to build a practical application that manages a personal book collection and tracks reading progress.

## 👨‍💻 Author

**Sayan Kundu**

Personal Library & Reading Tracker — Python CLI Project.
