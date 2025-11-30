class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False   # private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # It was not checked out


class Library:
    def __init__(self):
        self._books = []   # private list of Book objects

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # Book not found

    def return_book(self, title):
        """Return a previously checked-out book by title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # Book not found

    def list_available_books(self):
        """Print all books that are not checked out."""
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")