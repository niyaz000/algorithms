class Node(object):
  def __init__(self, data, next = None):
    self._data = data
    self._next = next

  @property
  def next(self):
    return self._next

  @property
  def data(self):
    return self._data

  @data.setter
  def data(self, value):
    self._data = value

  @next.setter
  def next(self, value):
    self._next = value

node = Node(1, Node(2))
print node.next.data
