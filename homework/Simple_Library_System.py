class Book:
    def __init__(self, isbn, title, author, status = "available", borrower = None):
         self.isbn = isbn
         self.title = title
         self.author = author
         self.status = status
         self.borrower = borrower
    
    def borrow(self, borrow):
        if self.status == "available":
           self.status = "borrowed"
           self.borrower = "borrower"
           print(f'{self.title} has been borrowed by {borrower}')
        else: 
            print(f'{self.titel} is not available in the library')

    def return_book(self):
        if self.status == "borrowed":
            self.status = "available"
            self.borrower = None
            print(f'{self.title} has been returned')
        else:
            print(f'{self.title} is not borrowed in the library')

class Library:
    def __init__ (self):
        self.books = []
    def add_book(self, new_book):

        for book in self.books:
            if book.isbn == book.isbn:
                print(f'A book with ISBN {new_book.isbn} already exists in the library.')
                return
            
            self.book.append(new_book)
            print(f'{new_book.title} has been added to the library.')

    def get_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
    
    def list_books(self):
        for book in self.books:
            print(f'ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Status: {book.status}, Borrower: {book.borrower}')

library = Library()

library.add_book(Book(1111, "Python progmamming", "John Doe"))
library.add_book(Book(2222, "Learning AI", "Jane Smith"))

book = library.get_book(1111)
if book:
    book.borrow("Ivan")
    book.borrow("Stoyan")

library.list_books()




