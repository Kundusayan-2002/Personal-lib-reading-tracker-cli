from src.models import Book
from src.library import Library

library = Library()

book1 = Book(
    "Python Crash Course",
    "Eric Matthes",
    "Programming",
    100,
    )

library.add_book(book1)


library.display_books()
print(len(library.books)) 

found_book = library.find_book_by_title("Python Crash Course")
print(found_book)


