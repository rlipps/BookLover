import unittest
from booklover import BookLover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # Create book lover and add a book.
        test_bl1 = BookLover('Ryan', 'rhl8pk@virginia.edu', 'fiction')
        test_bl1.add_book('1Q84', 4)
        
        # Test if book is added to book_list
        expected = True
        self.assertTrue('1Q84' in test_bl1.book_list['book_name'].unique(), expected)

    def test_2_add_book(self):
        # Add the same book twice and test if book is in `book_list` only once.
        test_bl1 = BookLover('Ryan', 'rhl8pk@virginia.edu', 'fiction', num_books=1,\
                            book_list=pd.DataFrame({'book_name':['1Q84'], 'book_rating':[4]}))
        test_bl1.add_book('1Q84', 4)

        # Test if book added twice is in `book_list` only once.
        # Functional test here is looking to see if value_counts() match expectations
        expected = 1
        self.assertEqual(test_bl1.book_list.value_counts()[0], 1)

    def test_3_has_read(self): 
        # Pass a book in the list and test if the answer is `True`.
        test_bl1 = BookLover('Ryan', 'rhl8pk@virginia.edu', 'fiction')
        test_bl1.add_book('1Q84', 4)

        # Test if the answer for has_read() is `True`.
        expected = True
        self.assertTrue(test_bl1.has_read('1Q84'), expected)
        
    def test_4_has_read(self): 
        # Pass a book NOT in the list and use `assert False` test the answer is `True`
        test_bl1 = BookLover('Ryan', 'rhl8pk@virginia.edu', 'fiction')
        test_bl1.add_book('1Q84', 4)

        # Test is the answer is `False`
        expected = False
        self.assertFalse(test_bl1.has_read('Mason & Dixon'), expected)
        
    def test_5_num_books_read(self): 
        # Add some books to the list, and test num_books matches expected.
        test_bl1 = BookLover('Ryan', 'rhl8pk@virginia.edu', 'fiction')
        test_bl1.add_book('1Q84', 4)
        test_bl1.add_book('The Nix', 5)
        test_bl1.add_book('The Corrections', 2)

        # Test num_books matches expected.
        expected = 3
        self.assertEqual(test_bl1.num_books_read(), expected)

    def test_6_fav_books(self):
        # Add some books with ratings to the list, making sure some of them have rating greater than 3.
        # Your test should check that the returned books have rating greater than 3
        test_bl1 = BookLover('Ryan', 'rhl8pk@virginia.edu', 'fiction', num_books=1,\
                             book_list=pd.DataFrame({'book_name':['1Q84'], 'book_rating':[4]}))
        test_bl1.add_book('The Nix', 5)
        test_bl1.add_book('The Corrections', 2)
        test_bl1.add_book('Inherent Vice', 3)

        # Test that the returned books have rating greater than 3
        expected = True
        self.assertTrue(test_bl1.fav_books().book_rating.min() > 3, expected)
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)