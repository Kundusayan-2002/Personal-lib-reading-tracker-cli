
"""Storage module for the Personal Library & Reading Tracker."""

import os
import json

from src.models import Book

FILENAME = "data.json"

def write_data(books: list[Book]) -> None:
    """Convert Book objects into dictionaries and save them."""

    serialized_books = [book.to_dict() for book in books]

    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(serialized_books, file, indent=4)

def ensure_file_exists() -> None:
    """Create the JSON file if it does not exist."""

    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def read_data() -> list[Book]:
    """Read books from JSON and convert them into Book objects."""

    ensure_file_exists()

    with open(FILENAME, "r", encoding="utf-8") as file:
        try:
            books = json.load(file)
        except json.JSONDecodeError:
            raise ValueError("data.json contains invalid or empty JSON.")

    return [Book.from_dict(book) for book in books]



