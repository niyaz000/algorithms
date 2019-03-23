import unittest
import sys
sys.path.append('../src')
from LinkedList import LinkedList

class TestAddToHead(unittest.TestCase):

  def test_addToHead_should_add_a_new_node_to_the_linkedlist(self):
    linkedlist = LinkedList()
    linkedlist.addToHead(1)
    self.assertEqual(linkedlist.head.data, 1, "First node should have value 1")
    self.assertEqual(linkedlist.head.next, None, "next node of head should point to null")

  def test_addToHead_should_add_a_new_nodes_to_the_linkedlist(self):
    linkedlist = LinkedList()
    linkedlist.addToHead(4)
    linkedlist.addToHead(3)
    linkedlist.addToHead(2)
    linkedlist.addToHead(1)
    self.assertEqual(linkedlist.head.data, 1, "First node should have value 1")
    self.assertEqual(linkedlist.head.next.data, 2, "Second node should have value 2")
    self.assertEqual(linkedlist.head.next.next.data, 3, "Third node should have value 3")
    self.assertEqual(linkedlist.head.next.next.next.data, 4, "Fourth node should have value 4")
    self.assertEqual(linkedlist.head.next.next.next.next, None, "Fourth nodes's next should point to None")

if __name__ == '__main__':
  unittest.main()
