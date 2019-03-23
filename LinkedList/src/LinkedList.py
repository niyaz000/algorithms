from Node import Node

class LinkedList(object):
  def __init__(self, head = None):
    self.head = head

  def addToHead(self, data):
    self._head = Node(data, self.head)
