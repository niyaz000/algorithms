import unittest
import sys
sys.path.append('../src')
from BinarySearch import BinarySearch

class TestIsPresent(unittest.TestCase):

  def test_isPresent_begin_index_is_negative_should_throw_exception(self):
    array = [1, 2, 3, 4, 5, 6, 7]
    search = BinarySearch(array)
    self.assertEqual(search.is_present(-1, 5), None)

  def test_isPresent_end_index_is_greater_than_array_length_should_throw_exception(self):
    array = [1, 2, 3, 4, 5, 6, 7]
    search = BinarySearch(array)
    self.assertEqual(search.is_present(0, 10), None)

if __name__ == '__main__':
    unittest.main()
