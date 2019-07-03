from sets import Set

import unittest

def to_array(set, is_str=False):
  # Strip off brackets and split the string into an array by commas I.E. "[1, 2, 3, 4, 5]" => "1, 2, 3, 4, 5" => ["1","2","3","4","5","6"]     
  # Also makes sure its in sorted order because it is an unsorted data type
  s = sorted(str(set)[1:-1].split(', '))
  if s[0] and not is_str:
    # because I am using mostly ints in my tests it auto converts them back into ints.
    for i, item in enumerate(s):
      s[i] = int(item)
    return s
  # could be set of strings rather than ints, in this case we don't want to return an empty list
  if is_str:
    return s
  return []

class OppsOnSingleElementsTest(unittest.TestCase):

  def test_init(self):
    s = Set([1,5,6])
    assert s.contains(1)
    assert s.contains(5)
    assert s.contains(6)


  def test_contains(self):
    s = Set()
    assert s.contains(0) is False
    s.add(0)
    assert s.contains(0) is True
    s.remove(0)
    assert s.contains(0) is False

  def test_add(self):
    s = Set()
    assert s.size is 0
    s.add(1)
    assert s.contains(1)
    assert s.size is 1
    s.add(3)
    assert s.contains(3)
    assert s.size is 2
    s.add(2)
    assert s.contains(2)
    assert s.size is 3

  def test_remove(self):
    s = Set()
    s.add(1)
    s.add(3)
    s.add(2)
    s.remove(2)
    assert s.size is 2
    assert s.contains(2) is False
    s.remove(3)
    assert s.size is 1
    assert s.contains(3) is False
    s.remove(1)
    assert s.size is 0
    assert s.contains(1) is False

class OppsOnOtherSetsTest(unittest.TestCase):
  def test_union(self):
    s1 = Set([1,2,3,4])
    s2 = Set([3,4,5,6])
    
    assert to_array(s1.union(s2)) == [1,2,3,4,5,6]

    s1 = Set([1,2,3,4])
    s2 = Set([1,2,3,4])
    assert to_array(s1.union(s2)) == [1,2,3,4]

    s1 = Set([1,2,3,4])
    s2 = Set([5,6,7,8])
    assert to_array(s1.union(s2)) == [1,2,3,4,5,6,7,8]

    s1 = Set([])
    s2 = Set([])
    assert to_array(s1.union(s2)) == []

    s1 = Set([1,2,3,4])
    s2 = Set([])
    assert to_array(s1.union(s2)) == [1,2,3,4]
  
  def test_intersection(self):
    s1 = Set([1,2,3,4])
    s2 = Set([3,4,5,6])
    
    assert to_array(s1.intersection(s2)) == [3,4]

    s1 = Set([1,2,3,4])
    s2 = Set([1,2,3,4])
    assert to_array(s1.intersection(s2)) == [1,2,3,4]

    s1 = Set([1,2,3,4])
    s2 = Set([5,6,7,8])
    assert to_array(s1.intersection(s2)) == []

    s1 = Set([])
    s2 = Set([])
    assert to_array(s1.intersection(s2)) == []

    s1 = Set([1,2,3,4])
    s2 = Set([])
    assert to_array(s1.intersection(s2)) == []
  
  def test_difference(self):
    s1 = Set([1,2,3,4])
    s2 = Set([3,4,5,6])
    
    assert to_array(s1.difference(s2)) == [1,2]

    s1 = Set([1,2,3,4])
    s2 = Set([1,2,3,4])
    assert to_array(s1.difference(s2)) == []

    s1 = Set([1,2,3,4])
    s2 = Set([5,6,7,8])
    assert to_array(s1.difference(s2)) == [1,2,3,4]

    s1 = Set([])
    s2 = Set([])
    assert to_array(s1.difference(s2)) == []

    s1 = Set([1,2,3,4])
    s2 = Set([])
    assert to_array(s1.difference(s2)) == [1,2,3,4]

  def test_is_subset(self):
    s1 = Set([1,2,3,4])
    s2 = Set([2,3])
    
    assert s1.is_subset(s2) is True

    s1 = Set([1,2,3,4])
    s2 = Set([1,2,3,4])
    assert s1.is_subset(s2) is True

    s1 = Set([1,2,3,4])
    s2 = Set([5,6,7,8])
    assert s1.is_subset(s2) is False

    s1 = Set([])
    s2 = Set([])
    assert s1.is_subset(s2) is True

    s1 = Set([1,2,3,4])
    s2 = Set([1,2,3,4,5])
    assert s1.is_subset(s2) is False

    s1 = Set([1,2,3,4])
    s2 = Set([1,2,3,5])
    assert s1.is_subset(s2) is False

    s1 = Set([1,2,3,4])
    s2 = Set([2,3,4])
    assert s1.is_subset(s2) is True

    s1 = Set([1,2,3,4])
    s2 = Set([1,2,3])
    assert s1.is_subset(s2) is True