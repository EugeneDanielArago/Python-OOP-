class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"

class Library:
    def __init__(self):
        self.books = []
    
    def add(self, title, author):
        new_book = Book (title, author)
        self.books.append(new_book)
        print(f"Added '{title}' by {author} to the library.")
    
    def bookTitle(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow(self, title):
        book = self.bookTitle(title)
        if book is None:
            print("Book not found.")
        elif not book.available:
            print(f"Sorry, '{title}' is currently borrowed.")
        else:
            book.available = False
            print(f"You have borrowed '{title}'.")

    def return_book(self, title):
        book = self.bookTitle(title)
        if book is None:
            print("Book not found.")
        else:
            if book.available:
                print(f"'{title}' is already available in the library.")
            else:
                book.available = True
                print(f"Thank you! You've returned '{title}'.")
    
    def view(self):
        if self.books:
            print("\nThe Books in the library:")
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")
            
library = Library()

while True:

    print("\n-----------------------------")
    print("  Library Management System")
    print("------------------------------")
    print("1. Add Books")
    print("2. Borrow Books")
    print("3. Return Books")
    print("4. View all Books")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        title = input("Enter the book title: ")
        author = input("Enter the author name: ")
        library.add(title, author)

    elif choice == 2:
        title = input("Enter the title of the book to borrow: ")
        library.borrow(title)

    elif choice == 3:
        title = input("Enter the title of the book to return: ")
        library.return_book(title)

    elif choice == 4:
        library.view()

    elif choice == 5:
        print("Exiting the Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 5.")
