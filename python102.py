#libarary managment system
class library:
    def __init__(self):
        self.books = [ ]
        self.no_of_books = 0


    def add_book(self,book_name):
        self.books.append(book_name)
        self.no_of_books = len(self.books)



    def show_info(self):
        print(f"\nlibrary mein total books: {self.no_of_books}")
        print("books name:")
        for index, book in enumerate(self.books,start=1):
            print(f"{index}. {book}")



my_library = library()
my_library.add_book("python programmer by code with harry")
my_library.add_book("Data science managment")
my_library.add_book("Rich dad and poor dad")
my_library.show_info()
