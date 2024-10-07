import tkinter as tk
from tkinter import messagebox, simpledialog

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

class BookBST:
    def __init__(self):
        self.root = None

    def insert(self, book):
        if not self.root:
            self.root = Node(book)
        else:
            self._insert_recursively(self.root, book)

    def _insert_recursively(self, node, book):
        if book.title < node.book.title:
            if node.left is None:
                node.left = Node(book)
            else:
                self._insert_recursively(node.left, book)
        else:
            if node.right is None:
                node.right = Node(book)
            else:
                self._insert_recursively(node.right, book)

    def search(self, title):
        return self._search_recursively(self.root, title)

    def _search_recursively(self, node, title):
        if node is None or node.book.title == title:
            return node
        if title < node.book.title:
            return self._search_recursively(node.left, title)
        return self._search_recursively(node.right, title)

    def display(self):
        return self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        result = []
        if node:
            result.extend(self._in_order_traversal(node.left))
            result.append(f"{node.book.title} by {node.book.author} ({node.book.year})")
            result.extend(self._in_order_traversal(node.right))
        return result

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Library Management System")
        self.library = BookBST()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Library Management System", font=("Arial", 16)).pack(pady=10)

        # Add Book Button
        tk.Button(self.root, text="Add Book", command=self.add_book).pack(pady=5)
        
        # Search Book Button
        tk.Button(self.root, text="Search Book", command=self.search_book).pack(pady=5)

        # Display Books Button
        tk.Button(self.root, text="Display Books", command=self.display_books).pack(pady=5)

    def add_book(self):
        title = simpledialog.askstring("Input", "Enter book title:")
        author = simpledialog.askstring("Input", "Enter author name:")
        year = simpledialog.askinteger("Input", "Enter publication year:")

        if title and author and year:
            new_book = Book(title, author, year)
            self.library.insert(new_book)
            messagebox.showinfo("Success", f"Added '{title}' by {author} ({year})")
        else:
            messagebox.showwarning("Warning", "All fields must be filled!")

    def search_book(self):
        title = simpledialog.askstring("Input", "Enter book title to search:")
        found = self.library.search(title)

        if found:
            messagebox.showinfo("Book Found", f"{found.book.title} by {found.book.author} ({found.book.year})")
        else:
            messagebox.showinfo("Not Found", f"'{title}' not found in the library.")

    def display_books(self):
        books = self.library.display()
        if books:
            books_list = "\n".join(books)
            messagebox.showinfo("Books in Library", books_list)
        else:
            messagebox.showinfo("Empty Library", "No books in the library.")

def main():
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
