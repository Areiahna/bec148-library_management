import random

users = []

def user_menu():
    print(f'''
    User Operations:
    -----------------
    1. Add a new user
    2. View user details
    3. Display all users
    ''')
    ans = input("How can we help you today?: ")
    if ans == "1":
        add_user()
    elif ans == "2":
        user_info()
    elif ans == "3":
        view_users()

class User:
    def __init__(self,name,email,address):
        self.name = name
        self.email = email
        self.address = address
        self.id = random.randint(1,200)
        self.borrowed = []
    
    
    def get_info(self):
        print(f'''
        Library_id# {self.id} 
        Name: {self.name}
        Email: {self.email}
        Address: {self.address}
        ''')
        print("Borrowed Books:")
        for book in self.borrowed:
            print(f'''
        -{book}''')
        
Jess= User("Jessica","hotgirl72@gmail.com","123 Sesame St")
users.append(Jess)
Pat = User("Patrick","starfish91@gmail.com","274 Bikini St")
users.append(Pat)



def add_user():
    name = input("What's your name?: ")
    email = input("What's your email?: ")
    address = input("What's your address?: ")
    
    new_user = User(name,email,address)
    users.append(new_user)
    print(f"\nWelcome {new_user.name}!")



def user_info():
    ans = input("Which user are you searching for?: ")
    for user in users:
        if user.name == ans:
            user.get_info()


def view_users():
    for user in users:
        print(f"- {user.name}")