import author

class Book:
    def __init__(self, book_name, author):
        self.name = book_name
        self.author = author

    def get_info(self):
        return "Book name: " + self.name + ". " + self.author.get_info()
