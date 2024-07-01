# ---- Book Operations
# should take in the class Author

from author import Author, authors
from user import User, users

books = []


#-- UI for book operations
def books_menu():
    print(f'''
    Book Operations:
    -----------------
    1. Add a new book
    2. Borrow a book
    3. Return a book
    4. Search for a book
    5. Display all books
    ''')
    ans = input("What can we help you with today?: ")
    if ans == "1":
        add_book()
    elif ans == "2":
        library_borrow()
    elif ans == "3":
        library_return()
    elif ans == "4":
        libray_search()
    elif ans == "5":
        view_library()




#-- Class Book with attributes for readers to get info, borrow & return books   
class Book:
    def __init__(self,title,author,genre,pub_date, available = True):
        self.title = title
        self.author = author
        self.genre = genre
        self.pub_date = pub_date
        self.available = available
    
    #-- Displaying book info
    def get_info(self):
        print(f''' 
        Title: {self.title}
        Author: {self.author}
        Genre: {self.genre}
        Publication Date : {self.pub_date}
        Availabile: {self.available}
        ''')

     #-- Marking available attrubute as False once user borrows book.   
    def availability(self):
        print("Checking System for book availability...")
        if self.available != False:
            print("This book is available!")
            current_user = input("What is your librayId#? :")
            for user in users:
                if user.id == int(current_user):
                    user.borrowed.append(self.title)
                    print(f"You have borrowed the book: {self.title} by {self.author}")
                    self.available = False    
        else:
            print("Sorry, this book has been borrowed")
    
    #-- Marking available attribute as True once user returns book
    def return_book(self): 
        if self.available != True:
            print("Thanks for returning this book!")
            self.available = True
        else:
            print("Sorry, our system shows that you did not borrow this book from us.")

            
Holes = Book("Holes","Luis Sachar","Novel","8/18/1996")
MeB4u = Book("Me Before You","Jojo Moyes","Romance","2012")
David = Book("No David!","David Sharron","Children picture novel","9/1/1998")
# Appending books to the 'books' array
books.append(Holes)
books.append(MeB4u)
books.append(David)   

#-- Book function for creating a new book object
def add_book ():
    found = False
    title = input("Enter Title: ").title()
    author = input("Enter author: ").title()
    genre = input("Enter genre: ").title()
    pub_date = input("Enter publication date: ")

    new_book = Book(title,author,genre,pub_date)
    new_book.get_info()
    books.append(new_book)

    for old_author in authors:
        if old_author.name == author:
            found = True
        if found == False:
            desc = input(f"Tell us a little more about {author}: ")
            new_author = Author(author, desc)
            authors.append(new_author)



def library_borrow():
    view_library()
    user_book = input(f"\nWhich book would you like to borrow?: ")
    for book in books:
        if user_book.title() == book.title:
            book.availability()

            
def library_return():
    user_book = input(f"\nWhich book are you returning: ")
    for book in books:
        if user_book.title() == book.title:
            book.return_book()
        
            

def libray_search():
    search = input("Which book are you searching for?: ")
    for book in books:
        if search.title() == book.title:
            book.get_info()

def view_library():
    print(f"\n Current Library")
    print("-"*25)
    for book in books:
        print(f"- {book.title} by {book.author}")
