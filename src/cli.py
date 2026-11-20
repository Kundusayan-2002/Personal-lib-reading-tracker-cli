

"""Command-line interface for the Personal Library & Reading Tracker."""

from src.models import Book
from src.library import Library


class LibraryCLI:
    """Handle user interaction with the personal library."""

    def __init__(self, library: Library) -> None:
        """Initialize the CLI with a Library object."""
        self.library = library

    def display_menu(self) -> None:
        """Display the main menu."""

        print("\n========== PERSONAL LIBRARY TRACKER ==========")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Search Books")
        print("4. Filter Books")
        print("5. Update Reading Progress")
        print("6. Mark Book as Finished")
        print("7. Remove a Book")
        print("8. View Statistics")
        print("0. Exit")
        print("==============================================")

    def display_book_details(self, book: Book) -> None:
        """Display the details of a single book."""

        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Genre: {book.genre}")
        print(f"Total Pages: {book.total_pages}")
        print(f"Current Page: {book.current_page}")
        print(f"Status: {book.status}")
        print(f"Finish Date: {book.finish_date}")

    def add_book(self) -> None:

      title = input("Enter book title: ").strip()
      author = input("Enter author name: ").strip()
      genre = input("Enter book genre: ").strip()

      try:
          if not title or title.isdigit():
              
            raise ValueError("Book title cannot be empty or only numbers.")

          if not author or author.isdigit():
            raise ValueError("Author name cannot be empty or only numbers.")

          if not genre or genre.isdigit():
            raise ValueError("Genre cannot be empty or only numbers.")

          total_pages = int(input("Enter total pages: "))

          book = Book(title, author, genre, total_pages)
          self.library.add_book(book)

          print("Book added successfully!")

      except ValueError as error:
        print(f"Error: {error}")

    def view_all_books(self) -> None:
        """Display all books in the library."""

        if not self.library.books:
            print("Your library is empty!")
            return

        print("\n========== ALL BOOKS ==========")

        for index, book in enumerate(self.library.books, start=1):
            print(f"\nBook {index}")
            self.display_book_details(book)

    def search_books(self) -> None:
        """Search books by title or author."""

        keyword = input("Enter book title or author: ").strip()

        results = self.library.search_books(keyword)

        if not results:
            print("No matching books found.")
            return

        print("\n========== SEARCH RESULTS ==========")

        for index, book in enumerate(results, start=1):
            print(f"\nBook {index}")
            self.display_book_details(book)

    def filter_books(self) -> None:
        """Filter books by genre or reading status."""

        print("\n========== FILTER BOOKS ==========")
        print("1. Filter by Genre")
        print("2. Filter by Status")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                genre = input("Enter genre: ").strip()
                results = self.library.filter_by_genre(genre)

            case "2":
                print("\n1. To-Read")
                print("2. Currently Reading")
                print("3. Completed")

                status_choice = input("Choose status: ").strip()

                match status_choice:
                    case "1":
                        status = "to-read"
                    case "2":
                        status = "reading"
                    case "3":
                        status = "finished"
                    case _:
                        print("Invalid status choice!")
                        return

                results = self.library.filter_by_status(status)

            case _:
                print("Invalid choice!")
                return

        if not results:
            print("No matching books found.")
            return

        print("\n========== FILTER RESULTS ==========")

        for index, book in enumerate(results, start=1):
            print(f"\nBook {index}")
            self.display_book_details(book)

    def update_reading_progress(self) -> None:
        """Update the reading progress of a book."""

        title = input("Enter book title: ").strip()

        try:
            new_page = int(input("Enter current page: "))

            success = self.library.update_reading_progress(
                title, new_page
            )

            if success:
                print("Reading progress updated successfully!")
            else:
                print("Book not found.")

        except ValueError as error:
            print(f"Error: {error}")

    def mark_book_finished(self) -> None:
        """Mark a book as finished."""

        title = input("Enter book title: ").strip()

        success = self.library.mark_book_finished(title)

        if success:
            print("Book marked as finished!")
        else:
            print("Book not found.")

    def remove_book(self) -> None:
        """Remove a book from the library."""

        title = input("Enter book title to remove: ").strip()

        success = self.library.remove_book(title)

        if success:
            print("Book removed successfully!")
        else:
            print("Book not found.")

    def view_statistics(self) -> None:
        """Display library statistics."""

        print("\n========== LIBRARY STATISTICS ==========")

        print(f"Total Books: {self.library.total_books()}")

        print(
            f"Books Finished This Year: "
            f"{self.library.books_finished_this_year()}"
        )

        print(
            f"Average Pages Per Finished Book: "
            f"{self.library.average_pages_per_finished_book():.2f}"
        )

        favorite = self.library.favorite_genre()

        if favorite is not None:
            print(f"Favorite Genre: {favorite}")
        else:
            print("Favorite Genre: No finished books yet.")
