FILE_NAME = "library.txt"
books = []  

def load_books():
    
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 5:
                    continue
                books.append({
                    "id": parts[0],
                    "title": parts[1],
                    "author": parts[2],
                    "status": parts[3],
                    "issued_to": parts[4],
                })
    except FileNotFoundError:
        pass 


def save_books():
    
    with open(FILE_NAME, "w") as f:
        for b in books:
            f.write(f"{b['id']}|{b['title']}|{b['author']}|{b['status']}|{b['issued_to']}\n")



def generate_id():
    
    if not books:
        return "B101"
    last = max(int(b["id"][1:]) for b in books)
    return "B" + str(last + 1)


def find_book(book_id):
    for b in books:
        if b["id"].upper() == book_id.upper():
            return b
    return None


def show_line(b):
    return f"{b['id']} | {b['title']} | {b['author']} | {b['status']}"



def add_book():
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    if not title or not author:
        print("Title and author cannot be empty.")
        return
    book = {
        "id": generate_id(),
        "title": title,
        "author": author,
        "status": "Available",
        "issued_to": "-",
    }
    books.append(book)
    print("Book added. ID: " + show_line(book).replace(" | Available", "") + " | Available")


def issue_book():
    book_id = input("Book ID: ").strip()
    book = find_book(book_id)
    if book is None:
        print(f"Book ID {book_id} not found.")
        return
    if book["status"] == "Issued":
        print(f"Book {book['id']} is already issued to {book['issued_to']}.")
        return
    member = input("Member: ").strip()
    if not member:
        print("Member name cannot be empty.")
        return
    book["status"] = "Issued"
    book["issued_to"] = member
    available = sum(1 for b in books if b["status"] == "Available")
    print(f"Book {book['id']} issued to {member}. Status: Issued")
    print(f"Available books: {available}")


def return_book():
    book_id = input("Book ID: ").strip()
    book = find_book(book_id)
    if book is None:
        print(f"Book ID {book_id} not found.")
        return
    if book["status"] == "Available":
        print(f"Book {book['id']} is not issued.")
        return
    book["status"] = "Available"
    book["issued_to"] = "-"
    print(f"Book {book['id']} returned. Status: Available")


def search_book():
    keyword = input("Search (title/author): ").strip().lower()
    results = [b for b in books
               if keyword in b["title"].lower() or keyword in b["author"].lower()]
    if not keyword or not results:
        print("No books found.")
        return
    for b in results:
        print(show_line(b))


def display_all():
    if not books:
        print("Library is empty.")
        return
    for b in books:
        print(show_line(b))



def main():
    load_books()
    while True:
        print("\n--- Library Management System ---")
        print("1. Add book")
        print("2. Issue book")
        print("3. Return book")
        print("4. Search by title/author")
        print("5. View all books")
        print("6. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            display_all()
        elif choice == "6":
            save_books()
            print("Data saved to library.txt. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
