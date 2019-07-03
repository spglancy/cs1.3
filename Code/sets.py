from hashtable import HashTable
class Set(object):
  def __init__(self, elems=[]):
    self.size = 0
    self.table = HashTable()
    for i in elems:
      self.table.set(i, i)

  def __str__(self):
    return str(self.table.keys())
  
  def contains(self, item):
    return self.table.contains(item)

  def add(self, item):
    if self.contains(item):
      raise ValueError("item already in set")
    self.size += 1
    self.table.set(item, item)

  def remove(self, item):
    if not self.contains(item):
      raise ValueError("item not in set")
    self.size -= 1
    self.table.delete(item)

  def union(self, set2):
    new = Set()
    for i in self.table.keys():
      new.add(i)
    for val in set2.table.keys():
      if not new.contains(val):
        new.add(val)
    return new

  def difference(self, set2):
    new = Set()
    for i in self.table.keys():
      if not set2.contains(i):
        new.add(i)
    return new

  def intersection(self, set2):
    new = Set()
    for val in self.table.keys():
      if set2.contains(val):
        new.add(val)
    return new

  def is_subset(self, set2):
    for val in set2.table.keys():
      if not self.contains(val):
        return False
    return True
      