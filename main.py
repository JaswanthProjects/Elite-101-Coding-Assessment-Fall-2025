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

