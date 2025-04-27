import json

# Function to load books from the JSON file
def load_books():
    try:
        with open("library.txt", "r") as file:
            # Use try-except block to handle invalid JSON formatting
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error: Invalid JSON format. Starting with an empty library.")
                return []
    except FileNotFoundError:
        print("No existing library file found. Starting with an empty library.")
        return []

# Function to save books to the JSON file
def save_books(books):
    try:
        with open("library.txt", "w") as file:
            json.dump(books, file, indent=4)
    except Exception as e:
        print(f"Error saving to file: {e}")

# Function to add a book
def add_book(books):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    books.append({"Title": title, "Author": author, "Year": year, "Genre": genre, "Read": read_status})
    save_books(books)
    print("Book added successfully!✅\n")

# Function to remove a book
def remove(books):
    title = input("Enter the title of the book to remove: ")
    books = [book for book in books if book["Title"] != title]
    save_books(books)
    print("Book removed successfully!✔\n")
    return books

# Function to search for a book by title or author
def search_book(books):
    search_query = input("Enter book title or author to search: ").lower()
    results = [book for book in books if search_query in book["Title"].lower() or search_query in book["Author"].lower()]
    if results:
        for book in results:
            print(f"""
                  Title: {book['Title']} 
                  Author: {book['Author']}
                  Year: {book['Year']}
                  Genre: {book['Genre']}
                  Read: {'Read' if book['Read'] else 'Unread'}""")
    else:
        print("No books found.❌\n")

# Function to display all books
def display_books(books):
    if books:
        for book in books:
            print("----------------------------------------------------------------------------")
            print(f"{book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")
            print("----------------------------------------------------------------------------")
    else:
        print("No books added yet 🙅‍♂️‼.\n")

# Function to display statistics about the books
def display_statistics(books):
    total_books = len(books)
    read_books = len([book for book in books if book["Read"]])
    print(f"Total books: {total_books}")
    print(f"Books Read: {read_books}")
    print(f"Percentage Read: {read_books / total_books * 100:.2f}%" if total_books > 0 else "No books available to calculate statistics.\n")

# Main function to run the library manager
def main():
    books = load_books()  # Load the current list of books from the file
    while True:
        print("\n\tWelcome to your Personal Library Manager!📚\n")
        print("1.➕ Add a book")
        print("2.❌ Remove a book")
        print("3.🔍 Search for a book")
        print("4.📖 Display all books")
        print("5.📊 Display statistics")
        print("6.🚪 Exit")
        choice = input("👉 Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            books = remove(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            display_books(books)
        elif choice == "5":
            display_statistics(books)
        elif choice == "6":
            save_books(books)
            print("Library saved to file. Goodbye!😊👋")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.\n")

# Start the program if this script is executed directly
if __name__ == "__main__":
    main()
