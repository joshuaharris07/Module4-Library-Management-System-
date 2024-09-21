import random
import re

class BookOperations:
    def __init__(self):
        self.books = {
            "Lord of the Rings": {"title": "LOTR", "author": "Tolkien", "genre": "Fantasy", "publication year": 1954, "availability": True},
            "Mistborn": {"title": "Mistborn", "author": "Sanderson", "genre": "Fantasy", "publication year": 2006, "availability": False},
            "The Codex Alera": {"title": "The Codex Alera", "author": "Butcher", "genre": "Fantasy", "publication year": 2004, "availability": True}
            }
    
    def add_book(self, title, author, genre, publication_year):
        if title in self.books:
            print("That book is already in the library. Returning to the menu.")
        else:
            self.books[title] = {"title": title, "author": author, "genre": genre, "publication year": publication_year, "availability": True}

    def borrow_book(self, title):
        if title in self.books and self.books[title]["availability"]:
            print(f"You have checked {title} out. Returning to the menu")
            self.books[title]["availability"] = False
        elif title in self.books:
            print(f"{title} is already checked out and is not currently available.")
        else:
            print(f"{title} is not currently in our library system. Returning to the menu.")

    def return_book(self, title):
        if title in self.books and not self.books[title]["availability"]:
            self.books[title]["availability"] = True
            print(f"{title} has been successfully returned. Returning to the menu.")
        elif title in self.books:
            print(f"That book wasn't checked out yet! Returning to the menu.")
        else:
            print(f"{title} was not found in the library's system. Returning to the menu.")

    def search_book(self, title): #maybe author to see all titles by an author?
        if title in self.books:
            # availability = "Available" if {self.books["availability"]} else "Not available"
            print(f"{title}, Author {self.books[title]["author"]}, Genre {self.books[title]["genre"]}, Publication Year: {self.books[title]["publication year"]}")
        else:
            print(f"{title} is not currently in our library.")

    def display_all_books(self):
        for details in self.books.values():
            print(f"{details["title"]}, Author: {details["author"]}, Genre: {details["genre"]}, Publication Year: {details["publication year"]}")

class UserOperations:
    def __init__(self):
        self.users = {
            "1234567": {"library id": "1234567", "name": "John Doe", "borrowed books": []},
            "7777777": {"library id": "7777777", "name": "Moby Dog", "borrowed books": ["Mistborn"]}
        }   #library_id = key, books = list as the value. maybe delete this?
    
    def add_user(self, name):
        while True:   # This ensures the library ID isn't duplicated, preventing erasing of existing user information.
            library_id_generator = [str(random.randint(0, 9)) for _ in range(7)]
            library_id = "".join(library_id_generator)
            if library_id not in self.users: 
                break
        self.users[library_id] = {"library id": library_id, "name": name, "borrowed books": []} # TODO maybe remove borrowed books.
        print(f"New user: {name} has been assigned the following library ID: {library_id}")

    def view_user(self, library_id): #pass in variable that relates to the book object, so we can parse through that data mark books as borrowed here too.
        if library_id in self.users:
            print(f"Name: {self.users[library_id]["name"]}. Currently borrowing: {self.users[library_id]["borrowed books"]}") # use list comprehension to print out a non-list.

    def view_all_users(self):
        for details in self.users.values():
            print(f"Library ID: {details["library id"]}, Name: {details["name"]}, Borrowed Books: {details["borrowed books"]}") #work on this!

class AuthorOperations:
    def __init__(self):
        self.author_list = {
            "Tolkien": {"name": "Tolkien", "biography": "Wrote the Hobbit and the Lord of the Rings."},
            "Sanderson": {"name": "Sanderson", "biography": "Wrote the Mistborn trilogy."}
        } #TODO maybe add a category for books by them in the library

    def add_author(self, author_name, biography):
        if author_name in self.author_list:
            print("That author is already in the system. Returning to the menu.")
        else:
            self.author_list[author_name] = {"author name": author_name, "biography": biography}
            print(f"{author_name} has been added to the library system. Returning to the menu.")

    def view_author_details(self, author_name):
        if author_name in self.author_list:
            print(f"Name: {self.author_list[author_name]["name"]}\nBiography: {self.author_list[author_name]["biography"]}") 
        else:
            print(f"{author_name} is not in our library system. Returning to the menu.")

    def view_all_authors(self):
        for details in self.author_list.values():
            print(f"Author: {details["name"]}. Biography: {details["biography"]}")


print("Welcome to the Library Management System!")
book_operations = BookOperations() 
user_operations = UserOperations()
author_operations = AuthorOperations()

while True:
    menu_action = input("""\nMain Menu:\n
1. Book Operations
2. User Operations
3. Author Operations
4. Quit\n""")
    if menu_action == "1":
        menu_action = input("Book Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n")
        if menu_action == "1": 
            title = input("Enter the title of the book: ").title()
            author = input("Enter the author's last name: ").title()
            genre = input("Enter the genre of the book: ").title()
            publication_year = int(input("Enter the year the book was published: ")) # TODO need to add verification for adding a year.
            book_operations.add_book(title, author, genre, publication_year)
        elif menu_action == "2":
            title = input("Enter the title of the book you wish to check out: ").title()
            book_operations.borrow_book(title)
        elif menu_action == "3":
            title = input("Enter the title of the book you wish to return: ").title()
            book_operations.return_book(title)
        elif menu_action == "4":
            title = input("Enter the title of the book you wish to look for: ").title()
            book_operations.search_book(title)
        elif menu_action == "5":
            book_operations.display_all_books()
    elif menu_action == "2":
        menu_action = input("User Operations:\n1. Add a new user\n2. View user detais\n3. Display all users\n")
        if menu_action == "1": 
            name = input("Please put in your full name: ").title()
            user_operations.add_user(name)
        elif menu_action == "2":
            library_id = input("Please enter your library ID: ").strip()
            user_operations.view_user(library_id)
        elif menu_action == "3":
            user_operations.view_all_users()
    elif menu_action == "3":
        menu_action = input("Author Operations:\n1. Add a new author\n2. View author detais\n3. Display all authors\n")
        if menu_action == "1": 
            author_name = input("Please enter the author's name: ")
            author_biography = input("Please enter the biography or details you want to note about this author: ")
            author_operations.add_author(author_name, author_biography)
        elif menu_action == "2":
            author_name = input("Please enter the author's name to search for: ")
            author_operations.view_author_details(author_name)
        elif menu_action == "3":
            author_operations.view_all_authors()
    elif menu_action == "4":
        print("Thank you for using the library management system. Have a good day!")
        break
    else:
        print("Please make a selection by entering an integer.")