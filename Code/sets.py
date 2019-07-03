from hashtable import HashTable
class Set(object):
  def __init__(self):
    self.size = 0
    self.table = HashTable()
  
  def contains(item):
    self.table.get(item)

  def add(item):
    self.table.set(item, item)

  def remove(item):
    self.table.delete(item)

  def union(set2):
    new = Set()
    for i in self.table.items():
      new.add(i[0])
    for val in set2.table.items():
      if not new.contains(val[0]):
        new.add(val[0])
    return new

  def difference():
    new = Set()
    for i in self.table.items():
      if not set2.contains(i[0]):
        new.add(i[0])
    return new

  def intersection():
    new = Set()
    for i in self.table.items():
      if set2.contains(val[0]):
        new.add(val[0])
    return new

  def is_subset():
    if self.size > set2.size:
      group1 = self
      group2 = set2.table.items()
    else:
      group2 = self.table.items()
      group1 = set2
    for val in group2:
      if not group1.contains(val[0]):
        return False
    return True
      