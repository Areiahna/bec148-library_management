
authors = [] 

def authors_menu():
    print(f'''
    Author Operations:
    ------------------
    1. Add a new author
    2. View author details
    3. Display all authors
    ''')
    ans = input("How can we help you today?: ")

    if ans == "1":
        add_author()
    elif ans == "2":
        author_details()
    elif ans == "3":
        view_authors()


class Author:
    def __init__(self,name,bio):
        self.name = name
        self.bio = bio
    
    def get_info(self):
        print(f'''
        --Author Info--
        Name: {self.name}
        Biography: 
            {self.bio}
        ''')
        
Luis = Author("Luis Sachaar","Author of famous Disney movie and best selling book 'Holes'!")
authors.append(Luis)

def add_author():
    name = input("Enter author's name: ")
    bio = input("Enter short biography: ")

    new_author = Author(name.title(),bio)
    authors.append(new_author)

def author_details():
    ans = input("Which author are you searching for?: ")
    for author in authors:
        if author.name == ans.title():
            author.get_info()

def view_authors():
    print(f"\nCurrent authors in library:")
    print("-" * 25)
    for author in authors:
        print(f"- {author.name}")