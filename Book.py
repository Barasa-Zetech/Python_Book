# Python inheritance program of class named "Book" with the following attributes and methods: 


class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = False
    def borrow_book(self):
        self.borrowed = True
    def return_book(self):
        self.borrowed = False
    def display_info(self):
        print("Title:", self.title)
        print("\n Author:", self.author)
        print("\n Publication Year:", self.publication_year)
        print("\n Borrowed:", "Yes" if self.borrowed else "No")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
# Borrow the book
book1.borrow_book()
book1.display_info()
# Return the book
book1.return_book()
# Display updated book information
book1.display_info()
