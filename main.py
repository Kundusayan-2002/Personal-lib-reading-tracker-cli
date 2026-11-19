


"""Application entry point."""

from src.library import Library
from src.cli import LibraryCLI
from src.storage import read_data, write_data


def run_cli() -> None:
    """Run the main CLI application."""

    library = Library()

    # Load previous saved books
    library.books = read_data()

    app = LibraryCLI(library)

    while True:
        app.display_menu()

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                app.add_book()

            case "2":
                app.view_all_books()

            case "3":
                app.search_books()

            case "4":
                app.filter_books()

            case "5":
                app.update_reading_progress()

            case "6":
                app.mark_book_finished()

            case "7":
                app.remove_book()

            case "8":
                app.view_statistics()

            case "0":
                write_data(library.books)
                print("Thank you for using Personal Library Tracker!")
                break

            case _:
                print("Invalid choice! Please select between 0 and 8.")

        # Save changes after every menu operation
        write_data(library.books)


if __name__ == "__main__":
    run_cli()
