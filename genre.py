genres = []

def genre_menu():
    print(f'''
    Genre Operations:
    -----------------
    1. Add Genre
    2. Genre Details
    3. Display all Genres
    ''')
    ans = input("How can we help you today?: ")

    if ans == "1":
        add_genre()
    elif ans == "2":
        genre_search()
    elif ans == "3":
        view_genres()

class Genre:
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc

        
    def get_info():
        print(f''' 
        Genre : {self.name}
        Description : {self.description}
        ''')

fiction = Genre("Fiction","Created in the imagination of it's author")
genres.append(fiction)
non_fiction = Genre("Non-fiction","Based on facts")
genres.append(non_fiction)


def add_genre():
    name = input("Enter Genre name: ").title()
    desc = input("Enter Genre description: ")

    new_genre = Genre(name,desc)
    genres.append(new_genre)
    print(f"Genre {new_genre.name} has been added.")

def genre_search():
    ans = input("Which Genre are you searching for?: ")
    for genre in genres:
        if ans.title() == genre.name:
            genre.get_info()

def view_genres():
    for genre in genres:
        print(f"- {genre.name}")