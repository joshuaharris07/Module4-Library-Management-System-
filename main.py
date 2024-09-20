class BookOperations:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability = True
        

class UserOperations:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = [] #maybe a dict?

class AuthorOperations:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

print("Welcome to the Library Management System!")

while True:
    menu_action = input("""Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit""")
    if menu_action == "1":
        menu_action = input("Book Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
        if menu_action == "1": 
            pass #add new book
        elif menu_action == "2":
            pass #borrow
        elif menu_action == "3":
            pass #return book
        elif menu_action == "4":
            pass #search for a book
        elif menu_action == "5":
            pass #display all books
    elif menu_action == "2":
        menu_action = input("User Operations:\n1. Add a new user\n2. View user detais\n3. Display all users")
        if menu_action == "1": 
            pass #add new user
        elif menu_action == "2":
            pass #view user details
        elif menu_action == "3":
            pass #display all users
    elif menu_action == "3":
        menu_action = input("Author Operations:\n1. Add a new author\n2. View author detais\n3. Display all authors")
        if menu_action == "1": 
            pass #add new author
        elif menu_action == "2":
            pass #view author details
        elif menu_action == "3":
            pass #display all authors
    elif menu_action == "4":
        print("Thank you for using the library management system. Have a good day!")
        break
    else:
        print("Please make a selection by entering an integer.")