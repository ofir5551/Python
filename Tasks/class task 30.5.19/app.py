import book
import author
import date

arr_books = []

author1 = author.Author("Jeremy", date.Date(15, 8, 97))  # Author 1 = Jeremy
author2 = author.Author("Ofir", date.Date(14, 6, 95))  # Author 2 = Ofir


book1 = book.Book("book1", author1)
book2 = book.Book("book2", author1)
book3 = book.Book("book3", author2)
book4 = book.Book("book4", author1)
book5 = book.Book("book5", author1)
book6 = book.Book("book6", author2)
book7 = book.Book("book7", author1)
book8 = book.Book("book8", author1)
book9 = book.Book("book9", author2)
book10 = book.Book("book10", author1)

arr = (book1, book2, book3, book4, book5, book6, book7, book8, book9, book10)

arr_books.extend(arr)

x = input("Enter author: ")

for i in range(0, 10):
    if arr_books[i].author.name == x:
        print(arr_books[i].name)