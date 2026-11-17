class Library:
    
    def __init__(self):
      self.books = []

    #add a method to add a book to the library
    def add_book(self, book):
      self.books.append(book)    

    def display_books(self):
      for book in self.books:
        print(book)

    #add a method to find a book by title
    def find_book_by_title(self, title):
      for book in self.books:
        if book.title.lower() == title.lower():
          return (f"You have the book: {book.title} by {book.author}, Genre: {book.genre}, Status: {book.status}")
      return ("Book not found")

    def search_books(self, keyword):
      results = []
      for book in self.books:
        if (keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()):
          results.append(book)
      return results
    #find a method to filter books by genre
    def filter_by_genre(self, genre):
      results = []
      for book in self.books:
        if book.genre.lower() == genre.lower():
          results.append(book)
      return results
