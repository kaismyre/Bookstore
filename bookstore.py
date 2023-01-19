import sqlite3

# Create a connection to the ebookstore database
conn = sqlite3.connect('ebookstore.db')
c = conn.cursor()

# Create the books table with the specified structure
c.execute('''CREATE TABLE books
             (id INTEGER, Title TEXT, Author TEXT, Qty INTEGER)''')

# Populate the table with the specified values
books = [
    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
    (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
    (3004, "The Lord of the Rings", "J.R.R. Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Carroll", 12)
]
c.executemany("INSERT INTO books VALUES (?,?,?,?)", books)

# Commit the changes and close the connection
conn.commit()
conn.close()

# Main menu
while True:
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Enter a new book
        id = input("Enter the ID of the book: ")
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        qty = input("Enter the quantity of the book: ")

        conn = sqlite3.connect('ebookstore.db')
        c = conn.cursor()
        c.execute("INSERT INTO books VALUES (?,?,?,?)",
                  (id, title, author, qty))
        conn.commit()
        conn.close()

    elif choice == "2":
        # Update a book
        id = input("Enter the ID of the book: ")
        title = input("Enter the new title of the book: ")
        author = input("Enter the new author of the book: ")
        qty = input("Enter the new quantity of the book: ")

        conn = sqlite3.connect('ebookstore.db')
        c = conn.cursor()
        c.execute("UPDATE books SET Title = ?, Author = ?, Qty = ? WHERE id = ?",
                  (title, author, qty, id))
        conn.commit()
        conn.close()

    elif choice == "3":
        # Delete a book
        id = input("Enter the ID of the book: ")

        conn = sqlite3.connect('ebookstore.db')
        c = conn.cursor()
        c.execute("DELETE FROM books WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    elif choice == "4":
        # Search for a book
        title = input("Enter the title of the book: ")

        conn = sqlite3.connect('ebookstore.db')
        c = conn.cursor()
        c.execute("SELECT * FROM books WHERE Title = ?", (title,))
        result = c.fetchone()
        if result:
            print("ID:", result[0])
            print("Title:", result[1])
            print("Author:", result[2])
            print("Quantity:", result[3])
        else:
            print("Book not found.")
        conn.close()
    elif choice == "0":
        # Exit the program
        break
    else:
        print("Invalid choice. Please try again.")
