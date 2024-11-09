import unittest
from booklover import BookLover as bl

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        """adds a book and tests if it is in `book_list`."""
        joe = bl("Joe", "joe@joejoe.com", "Fantasy")
        joe.add_book("Jane Eyre", 3)
        self.assertIn("Jane Eyre", joe.book_list['book_name'].values)

    def test_2_add_book(self):
        """adds the same book twice. Tests if it's in `book_list` only once."""
        joe = bl("Joe", "joe@joejoe.com", "Fantasy")
        joe.add_book("Jane Eyre", 3)
        joe.add_book("Jane Eyre", 4)
        self.assertCountEqual(["Jane Eyre"], joe.book_list['book_name'].values)

    def test_3_has_read(self): 
        """passes a book in the list and tests if the answer is `True`."""
        joe = bl("Joe", "joe@joejoe.com", "Fantasy")
        joe.add_book("Jane Eyre", 3)
        self.assertTrue(joe.has_read("Jane Eyre"))
        
    def test_4_has_read(self): 
        """passes a book NOT in the list and uses `assert False` to test the answer is `True`"""
        joe = bl("Joe", "joe@joejoe.com", "Fantasy")
        joe.add_book("Jane Eyre", 3)
        self.assertFalse(joe.has_read("Fight Club"))
        
    def test_5_num_books_read(self): 
        """adds some books to the list, and tests num_books matches expected."""
        joe = bl("Joe", "joe@joejoe.com", "Fantasy")
        joe.add_book("Jane Eyre", 3)
        joe.add_book("Fight Club", 4)
        joe.add_book("The Divine Comedy", 5)
        joe.add_book("The Popol Vuh", 2)
        self.assertEqual(4, joe.num_books_read())

    def test_6_fav_books(self):
        """adds some books with ratings to the list, with some of them have rating > 3. Checks that the returned books have rating > 3"""
        joe = bl("Joe", "joe@joejoe.com", "Fantasy")
        joe.add_book("Jane Eyre", 3)
        joe.add_book("Fight Club", 4)
        joe.add_book("The Divine Comedy", 5)
        joe.add_book("The Popol Vuh", 2)
        favorite_books = joe.fav_books()
        self.assertIn("Fight Club", favorite_books['book_name'].values) # this took me forever to figure out and I don't understand why I first had to create a new object and couldn't just use the method object, due to "not subscriptable" ???
        self.assertIn("The Divine Comedy", favorite_books['book_name'].values)
        self.assertNotIn("Jane Eyre", favorite_books['book_name'].values)

if __name__ == '__main__':
    
    unittest.main(verbosity=3)