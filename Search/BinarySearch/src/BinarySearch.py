class BinarySearch(object):
  def __init__(self, array):
    self.array = array

  def throw_exception_if_indexes_invalid(self, begin, end):
    if begin < 0:
      raise ValueError("begin should be greater than or equal to zero, given value {}".format(begin))
    if end >= len(self.array):
      raise ValueError("end should be less than array length, given value {}, array length {}".format(end, len(self.array)))

  def _is_present(self, begin, end):
    pass

  def is_present(self, begin = 0, end = -1):
    try:
      self.throw_exception_if_indexes_invalid(begin, end)
    except Exception as error:
      print error
      return None
    end = len(self.array) if end == -1 else end
    return self._is_present(begin, end)
