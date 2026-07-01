class Book():
    def __init__(self, book_id, title, author, year, avaliable = True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.avaliable = avaliable
    def display_book(self):
        print(f'Book ID: {self.book_id}')
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Year Published: {self.year}')
        if self.avaliable == True:
            print('Status: Avaliable')
        else:
            print('Status: Borrowed') 
    def borrow(self):
        self.avaliable = False
    def return_book(self):
        self.avaliable = True