class OddCounter:
  def __init__(self, end=0):
    self.start = -1
    self.end = end
  
  def __iter__(self):
    return self

  def __next__(self):
    if self.start < self.end - 1:
      self.start += 2
      return self.start
    else:
      raise StopIteration


for c in OddCounter(100):
  print(c)

  