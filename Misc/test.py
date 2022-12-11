class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def max_path_sum(root):
    if not root:
      return float('-inf')
    
    maxVal = root.val
    
    if not root.left and not root.right:
      return maxVal
    
    
    childMax =  max(max_path_sum(root.left), max_path_sum(root.right))
    

    return max(maxVal, maxVal + childMax)


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(max_path_sum(a))