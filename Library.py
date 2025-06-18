class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Initially available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added '{title}' by {author} to the library.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks in the library:")
            for book in self.books:
                print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.find_book(title)
        if book is None:
            print("Book not found.")
        elif not book.available:
            print(f"Sorry, '{title}' is currently borrowed.")
        else:
            book.available = False
            print(f"You have borrowed '{title}'.")

    def return_book(self, title):
        book = self.find_book(title)
        if book is None:
            print("Book not found.")
        else:
            if book.available:
                print(f"'{title}' is already available in the library.")
            else:
                book.available = True
                print(f"Thank you! You've returned '{title}'.")


def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author name: ")
            library.add_book(title, author)

        elif choice == '2':
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)

        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)

        elif choice == '4':
            library.view_books()

        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 5.")


if __name__ == "__main__":
    main()
