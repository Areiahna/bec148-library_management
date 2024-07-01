from book import Book,books, books_menu
from user import User,users, user_menu
from author import Author, authors, authors_menu
from genre import Genre, genres, genre_menu

def main ():
    while True: 
        print('''
        Welcome to the Library Management System!

        Main Menu:
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Genres
        5. Quit
        ''')
        ans = input("What can we help you with today?: ")
        if ans == "1":
            books_menu() 
        elif ans == "2":
            user_menu()
        elif ans == "3":
            authors_menu()
        elif ans == "4":
            genre_menu()
        elif ans == "5":
            print("Happy Reading!")
            break

main()
