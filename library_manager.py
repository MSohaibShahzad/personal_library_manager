library = []

def add_book():
    title= input("Enter the book title: ")
    author= input("Enter the author name: ")
    year= input("Enter the publication year: ")
    genre= input("Enter the genre: ")
    read_input= input("Have you read this book? (yes/no): ").lower()
    if read_input == "yes":
        read = "read"
    else:
        read = "unread"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    print("book added successfully!")

def remove_book():
    removing = input("Enter the title of the book to remove:")
    for book in library:
        if removing == book["title"]:
            library.remove(book)
            print("book removed")
            return
    print("Book not found")

def search_book():
    print("search by:")
    print("1.Title")
    print("2.author")
    search = input("Enter your choice:")

    if search == "1":
        if len(library) == "0":
            print("Book not found, Library is empty")
        else:
            search_by_title = input("Enter the title: ").lower()
            for book in library:  
                if search_by_title in book["title"]:
                    print(f'{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {book["read"]}')
                    return
            print("no book found")
                
    elif search == "2":
        if len(library) == 0:
            print("Book not found, Library is empty")
        else:
            search_by_author = input("Enter the author name: ").lower()
            for book in library:
                if search_by_author in book["author"].lower() :
                    print(f'{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {book["read"]}')
                    return
            print("Book not found")
    else:
        print("Select how you want to search a book")
        search_book()

def display_book():
    if len(library) == 0:
        print("library is empty")
    else:    
        print("Your Library")
        for i, book in enumerate(library,start=1):
            print(f'{i}.{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {book["read"]} ')
        
    
def display_statistics():
    Total_book = len(library)
    if Total_book == 0 :
        print("No book found")
    else:
        read_count = sum(1 for book in library if book["read"] == "read")
        print(f"Total books:{Total_book}")
        percentage = read_count / Total_book * 100
        print(f"Percentage read: {percentage}")



def menu():
    while True:
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_book()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("Library saved to file. Goodbye!")
            break
        else:
            print("select (1-6)")    

menu()



