class Book:
    """A class representing a book with title, author, and publication year."""
    
    def __init__(self, title, author, year):
        """
        Constructor: Initialize a Book instance.
        
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
        Destructor: Print a message when the book object is deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String representation: User-friendly string representation of the book.
        
        Returns:
            str: Formatted string showing title, author, and year
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official representation: Developer-friendly representation that can recreate the object.
        
        Returns:
            str: String that would recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
