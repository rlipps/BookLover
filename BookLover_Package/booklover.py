import pandas as pd

class BookLover:
    '''
    A person who loves books. Has data on the person, 
    
    a collection of books you can add books to,

    whether or not they have read the books,

    their favorite books in a pandas dataframe
    '''

    def __init__(self, name: str, email: str, fav_genre: str, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name                                                # name string
        self.email = email                                              # email string
        self.fav_genre = fav_genre                                      # favorite genre string
        self.num_books = num_books                                      # number of books read
        self.book_list = book_list.astype({'book_rating': 'int'})       # book collection dataframe

    def add_book(self, book_name: str, book_rating: int):
        '''
        Adds book to collection. Does not add book if already in collection.

        Calls self.has_read() to check if book is already in collection.
        '''
        if self.has_read(book_name):
            print('Book already exists in book list')
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
                })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
    
    def has_read(self, book_name: str):
        '''
        Checks to see if book is already in collection
        '''
        if book_name in list(self.book_list['book_name']):
            return True
        else: return False

    def num_books_read(self):
        '''
        Computes and returns num_books based on length of book_list
        '''
        return self.num_books
    
    def fav_books(self):
        '''
        Return books from book_list where book_rating > 3
        '''
        return self.book_list.query('book_rating > 3')