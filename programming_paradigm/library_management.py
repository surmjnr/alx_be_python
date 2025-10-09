class Book:
    """A class representing a book in the library system."""
    
    def __init__(self, title, author):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Check out the book (mark as unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Return the book (mark as available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book objects can be added to the library")
    
    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(book)
