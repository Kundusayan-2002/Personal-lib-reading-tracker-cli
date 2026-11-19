
"""Book model for the Personal Library & Reading Tracker."""

from datetime import datetime


class Book:
    """Represent an individual book."""

    def __init__(
        self,
        title: str,
        author: str,
        genre: str,
        total_pages: int
    ) -> None:

        self.title = title
        self.author = author
        self.genre = genre

        if total_pages <= 0:
            raise ValueError("Total pages must be greater than 0")

        self.total_pages = total_pages
        self.current_page = 0
        self.status = "to-read"
        self.finish_date = None

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    def update_progress(self, new_page: int) -> None:
        """Update the current reading page and status."""

        if not 0 <= new_page <= self.total_pages:
            raise ValueError("Invalid page number")

        self.current_page = new_page

        if self.current_page == 0:
            self.status = "to-read"
            self.finish_date = None

        elif 0 < self.current_page < self.total_pages:
            self.status = "reading"
            self.finish_date = None

        elif self.current_page == self.total_pages:
            self.status = "finished"

            if self.finish_date is None:
                self.finish_date = datetime.now().isoformat()

    def to_dict(self) -> dict:
        """Convert the Book object into a dictionary."""

        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "total_pages": self.total_pages,
            "current_page": self.current_page,
            "status": self.status,
            "finish_date": self.finish_date
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        """Create a Book object from a dictionary."""

        book = cls(
            data["title"],
            data["author"],
            data["genre"],
            data["total_pages"]
        )

        book.current_page = data["current_page"]
        book.status = data["status"]
        book.finish_date = data["finish_date"]

        return book
