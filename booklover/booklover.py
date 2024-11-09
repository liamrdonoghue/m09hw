import pandas as pd

class BookLover:
    """This is a book lover"""
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    
    def add_book(self, book_name, book_rating: int):
        """Takes a book name and rating, tries to add the book to the book list only if it doesn't already exist. If it does exist, it tells the user."""
        if book_name in self.book_list['book_name'].values:
            print("Book already in book list")
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            

    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
    
    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]