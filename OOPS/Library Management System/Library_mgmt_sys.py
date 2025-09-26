class Book:
    def __init__(self,title,author,isbn,available=True):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=available
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Not Available'}"
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,Book):
        self.books.append(Book)
    def remove_book(self,isbn):
        self.books.remove(isbn)
    def find_book(self,title):
        for book in self.books:
            if title in book.title:
                return book
        return "Book not found"
    def display_books(self):
        for book in self.books:
            print(book)
        print("\n")    
class Member:
    def __init__(self,name,memeber_id,borrowed_books=None):
        self.name=name
        self.member_id=memeber_id
        self.borrowed_books=borrowed_books if borrowed_books is not None else []
    def borrow_book(self,Book):
        if Book.available:
            self.borrowed_books.append(Book)
            Book.available=False
            return f"{Book.title} borrowed successfully"
        else:
            return "Book not available"
    def return_book(self,Book):
        if Book in self.borrowed_books:
            self.borrowed_books.remove(Book)
            Book.available=True
            return f"{Book.title} returned successfully"
        else:
            return "Book not borrowed by member"
        
book1=Book("1984","George Orwell","1234567890")
book2=Book("To Kill a Mockingbird","Harper Lee","0987654321")
book3=Book("The Great Gatsby","F. Scott Fitzgerald","1122334455")
book4=Book("Python Programming","John Zelle","2233445566")
book5=Book("The Catcher in the Rye","J.D. Salinger","3344556677")  
library=Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
memeber1=Member("Shalini","1")
memeber1.borrow_book(book5)
library.display_books()
memeber1.return_book(book5)
library.display_books()