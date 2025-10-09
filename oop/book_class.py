class Book:
    """
    A Book class that models a book with title, author, and publication year.
    Implements various magic methods for enhanced functionality.
    """
    
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor that prints a message when the Book instance is deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String representation of the Book instance for end users.
        
        Returns:
            str: A user-friendly string representation
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official string representation of the Book instance.
        Should return a string that could recreate the instance.
        
        Returns:
            str: A string that would recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
