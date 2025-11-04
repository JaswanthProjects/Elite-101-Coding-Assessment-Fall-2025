from datetime import datetime, timedelta
from library_books import library_books

# -------- Level 1 --------
def view_available_books():
    print("\nOkay, here are the books that you can check out right now:")
    found_books = False
    # loop through all the books
    for book in library_books:
        if book["available"] == True:
            print(book["id"] + " - " + book["title"] + " by " + book["author"])
            found_books = True
    if found_books == False:
        print("Hmm... looks like no books are available at the moment.")
    print()


# -------- Level 2 --------
def search_books():
    search = input("Type an author or genre to search: ")
    search = search.lower()
    found_anything = False
    for book in library_books:
        # make everything lowercase so the search works better
        author = book["author"].lower()
        genre = book["genre"].lower()
        if search == author or search == genre or search in author or search in genre:
            print(book["id"] + " - " + book["title"] + " by " + book["author"] + " (" + book["genre"] + ")")
            found_anything = True
    if found_anything == False:
        print("Sorry, I couldn't find any books that match what you typed.")
    print()


# -------- Level 3 --------
def checkout_book():
    book_id = input("Enter the ID of the book you want to checkout: ")
    found = False
    for book in library_books:
        if book["id"] == book_id:
            found = True
            # check if someone already has it
            if book["available"] == False:
                print("Oops! That book is already checked out. Try another one maybe?")
            else:
                book["available"] = False
                # calculate due date (14 days from now)
                due_date = datetime.now() + timedelta(days=14)
                book["due_date"] = due_date.strftime("%Y-%m-%d")
                book["checkouts"] = book["checkouts"] + 1
                print("Yay! You checked out '" + book["title"] + "'.")
                print("Make sure to return it by " + book["due_date"] + " or you'll be late.")
            break
    if found == False:
        print("Hmm, I can't find that book ID. Check if you typed it right.")
    print()


# -------- Level 4 --------
def return_book():
    book_id = input("Enter the ID of the book you are returning: ")
    found = False
    for book in library_books:
        if book["id"] == book_id:
            found = True
            if book["available"] == True:
                print("Wait a sec, this book wasn't checked out.")
            else:
                # mark it as available again
                book["available"] = True
                book["due_date"] = None
                print("Thanks! '" + book["title"] + "' has been returned.")
            break
    if found == False:
        print("I couldn't find that book ID. Maybe you typed it wrong?")
    print()


def view_overdue_books():
    print("\nLet's see if there are any overdue books...")
    today = datetime.now().date()
    found_overdue = False
    for book in library_books:
        if book["available"] == False:
            if book["due_date"] != None:
                # convert the due date string to an actual date
                due = datetime.strptime(book["due_date"], "%Y-%m-%d").date()
                # see if today is past the due date
                if today > due:
                    print(book["id"] + " - " + book["title"] + " (Due: " + book["due_date"] + ")")
                    found_overdue = True
    if found_overdue == False:
        print("No overdue books right now. Good job everyone!")
    print()


# -------- Menu --------
def menu():
    print("Hello! Welcome to our Library System :)")
    while True:
        print("-------------------------------")
        print("1. See available books")
        print("2. Search for a book")
        print("3. Checkout a book")
        print("4. Return a book")
        print("5. See overdue books")
        print("q. Quit")
        print("-------------------------------")

        choice = input("What would you like to do? ")

        # check what the user picked
        if choice == "1":
            view_available_books()
        elif choice == "2":
            search_books()
        elif choice == "3":
            checkout_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_overdue_books()
        elif choice.lower() == "q":
            print("Okay, bye! Have a nice day :)")
            break
        else:
            print("Hmm, I don't understand that choice. Try again please.")
        print()


menu()