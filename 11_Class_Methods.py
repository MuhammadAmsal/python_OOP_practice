class Book:
    total_books = 0  

    def __init__(self, title, author):
        self.title = title     
        self.author = author   
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")

print(f"Total books created: {Book.total_books}")
