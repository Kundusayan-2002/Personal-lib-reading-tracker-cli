
"""Library management module."""

from datetime import datetime
from src.models import Book


class Library:
    """Manage a collection of books."""

    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        """Add a book to the library."""
        self.books.append(book)

    def display_books(self) -> None:
        """Display all books."""
        for book in self.books:
            print(book)

    def find_book_by_title(self, title: str) -> Book | None:
        """Find a book by its title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book

        return None

    def search_books(self, keyword: str) -> list[Book]:
        """Search books by title or author."""
        results = []

        for book in self.books:
            if (
                keyword.lower() in book.title.lower()
                or keyword.lower() in book.author.lower()
            ):
                results.append(book)

        return results

    def filter_by_genre(self, genre: str) -> list[Book]:
        """Filter books by genre."""
        results = []

        for book in self.books:
            if book.genre.lower() == genre.lower():
                results.append(book)

        return results

    def filter_by_status(self, status: str) -> list[Book]:
        """Filter books by reading status."""
        results = []

        for book in self.books:
            if book.status.lower() == status.lower():
                results.append(book)

        return results

    def remove_book(self, title: str) -> bool:
        """Remove a book by title."""
        book = self.find_book_by_title(title)

        if book is not None:
            self.books.remove(book)
            return True

        return False

    def mark_book_finished(self, title: str) -> bool:
        """Mark a book as finished."""
        book = self.find_book_by_title(title)

        if book is not None:
            book.update_progress(book.total_pages)
            return True

        return False

    def update_reading_progress(
        self, title: str, new_page: int
    ) -> bool:
        """Update the reading progress of a book."""

        try:
            book = self.find_book_by_title(title)

            if book is None:
                return False

            book.update_progress(new_page)
            return True

        except ValueError as error:
            print(f"Error: {error}")
            return False

    # ================= Statistics =================

    def total_books(self) -> int:
        """Return the total number of books."""
        return len(self.books)

    def books_finished_this_year(self) -> int:
        """Count books finished in the current year."""

        current_year = datetime.now().year
        count = 0

        for book in self.books:
            if book.status == "finished" and book.finish_date is not None:
                finish_year = datetime.fromisoformat(
                    book.finish_date
                ).year

                if finish_year == current_year:
                    count += 1

        return count

    def average_pages_per_finished_book(self) -> float:
        """Calculate average pages per finished book."""

        total_pages = 0
        finished_books = 0

        for book in self.books:
            if book.status == "finished":
                total_pages += book.current_page
                finished_books += 1

        if finished_books == 0:
            return 0.0

        return total_pages / finished_books

    def favorite_genre(self) -> str | None:
        """Return the most common finished-book genre."""

        genre_count = {}

        for book in self.books:
            if book.status == "finished":
                genre = book.genre

                if genre in genre_count:
                    genre_count[genre] += 1
                else:
                    genre_count[genre] = 1

        if not genre_count:
            return None

        return max(genre_count, key=genre_count.get)
