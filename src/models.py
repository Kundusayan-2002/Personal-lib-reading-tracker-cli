from datetime import datetime

class LibraryItem:
    def __init__(self, title):
        self.title = title


class Book(LibraryItem):
    def __init__(self, title, author, genre, total_pages):
        super().__init__(title)
        self.author = author
        self.genre = genre
        
        if total_pages <= 0:
            raise ValueError("Total pages must be greater than 0")
        
        self.total_pages = total_pages
        self.current_page = 0
        self.status = "to-read"
        self.finish_date = None

    def __str__(self):
        return f"{self.title} by {self.author}"

    def update_progress(self, new_page):
        
        if not 0 <= new_page <= self.total_pages:
          raise ValueError("Invalid page number")

        self.current_page = new_page

        if self.current_page == 0:
          self.status = "to-read"

        elif 0 < self.current_page < self.total_pages:
          self.status = "reading"

        elif self.current_page == self.total_pages:
          self.status = "finished"
          self.finish_date = datetime.now().isoformat()