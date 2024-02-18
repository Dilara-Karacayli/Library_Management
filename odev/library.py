#Library adında bir kütüphane oluşturduk.
class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()
#Dosyadaki kitapları listeler.

    def list_books(self):
        self.file.seek(0)
        books_list = self.file.read().splitlines()
        for book_info in books_list:
            title, author, release_date, num_pages = book_info.split(',')
            print(f"Title: {title}, Author: {author}")
#Kitap ekleme kod bloğu

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully!")

#Kitap silmek için kullanıcıdan kitap adını alan kod bloğu.

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        books_list = self.file.read().splitlines()

        found = False
        for book_info in books_list:
            current_title, _, _, _ = book_info.split(',')
            if current_title == title_to_remove:
                books_list.remove(book_info)
                found = True
                break

        if found:
            self.file.seek(0)
            self.file.truncate()
            for book_info in books_list:
                self.file.write(book_info + '\n')
            print("Book removed successfully.")
        else:
            print("Book not found.")

# Library adlı sınıftan bir nesne oluşturma işlemi.
lib = Library()

# Menü listesinin oluşturulması
#Kullanıcıdan yapmak istediği işlemi seçmesi istenir.
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option.")