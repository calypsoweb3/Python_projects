from book import Book
from validators import integer_validator, string_validator
class LibraryManager():
    def __init__(self):
        self.books = { }
    def add_book(self):
        while True:
            book_id = integer_validator('Enter a book ID: ', 100, 1000)
            if book_id in self.books:
                    print('A book with this ID already exists')
                    continue
            title = string_validator('Enter the book title: ')
            author = string_validator("Enter the author's name: ")
            year = integer_validator('Enter the year of publication: ', 1600, 2026)
            book = Book(book_id, title, author, year, avaliable = True)
            self.books[book_id] = book
            print(f'{title} by {author} added successfully')
            break
    def view_book(self):
        if self.books == { }:
            print('No books in the library')
            return
        for item in self.books.values():
            item.display_book()
    def search_book(self):
        book_id = integer_validator('Enter a book ID you wish to look for: ', 100, 1000)
        if book_id in self.books:
            book = self.books[book_id]
            book.display_book()
        else:
            print('Book not found')
    def borrow_book(self):
        book_id = integer_validator('Enter the book ID you wish to borrow: ', 100, 1000)
        if book_id not in self.books:
            print('Book not found')
            return
        book = self.books[book_id]
        if book.avaliable == False:
            print('This book has already been borrowed')
            return
        book.display_book()
        borrow = string_validator('Do you want to borrow this book? (Yes/No): ').lower()
        if borrow == 'yes':
            book.borrow()
            print(f'{book.title} by {book.author} has been borrowed successfully')
        elif borrow == 'no':
            print('Borrow cancelled')
        else:
            print('Invalid choice')
    def return_book(self):
        book_id = integer_validator('Enter the book ID you wish to return: ', 100, 1000)
        if book_id not in self.books:
            print('Book not found')
            return
        book = self.books[book_id]
        if book.avaliable == True:
            print('This book has not been borrowed')
            return
        book.display_book()
        return_b = string_validator('Do you want to return this book? (Yes/No): ').lower()
        if return_b == 'yes':
            book.return_book()
            print(f'{book.title} by {book.author} has been returned successfully')
        elif return_b == 'no':
            print('Return cancelled')
        else:
            print('Invalid choice')
    def delete_book(self):
        book_id = integer_validator('Enter the book ID you wish to delete: ', 100, 1000)
        if book_id not in self.books:
            print('Book not found')
            return
        book = self.books[book_id]
        if book.avaliable == False:
            print('This book is currently borrowed and cannot be deleted')
            return
        book.display_book()
        delete = string_validator('Do you want to delete this book? (Yes/No): ').lower()
        if delete == 'yes':
            self.books.pop(book_id)
            print(f'{book.title} by {book.author} has been deleted successfully')
        elif delete == 'no':
            print('Delete cancelled')
        else:
            print('Invalid choice')
    def menu(self):
        print('-----------------------------------')
        print("Welcome to Christopher's library ")
        print('-----------------------------------')
        while True:
            print('1. Add book')
            print('2. View book')
            print('3. Search book')
            print('4. Borrow book')
            print('5. Return book')
            print('6. Delete book')
            print('7. Exit')
            choice = integer_validator('What do you want to do: ',1, 7)
            if choice == 1:
                self.add_book()
                print()
            elif choice == 2:
                self.view_book()
                print()
            elif choice == 3:
                self.search_book()
                print()
            elif choice == 4:
                self.borrow_book()
                print()
            elif choice == 5:
                self.return_book()
                print()
            elif choice == 6:
                self.delete_book()
                print()
            elif choice == 7:
                print()
                print('Goodbye')
                print('See you next time')
                break
            else:
                print('Invalid choice, Try again')