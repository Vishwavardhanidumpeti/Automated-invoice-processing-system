class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.issued = False

    def __str__(self):
        status = "Issued" if self.issued else "Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Book added: {title}")

    def issue_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.issued:
                    book.issued = True
                    print(f"Book issued: {book.title}")
                    return
                else:
                    print("Book already issued.")
                    return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.issued:
                    book.issued = False
                    print(f"Book returned: {book.title}")
                    return
                else:
                    print("Book was not issued.")
                    return
        print("Book not found.")

    def show_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\n--- Library Books ---")
        for book in self.books:
            print(book)
        print()


def main():
    library = Library()
    while True:
        print("----- Library Management System -----")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Show All Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)
        elif choice == '2':
            isbn = input("Enter ISBN of book to issue: ")
            library.issue_book(isbn)
        elif choice == '3':
            isbn = input("Enter ISBN of book to return: ")
            library.return_book(isbn)
        elif choice == '4':
            library.show_books()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

        print("\n")


if __name__ == "__main__":
    main()
