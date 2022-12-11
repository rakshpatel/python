from queue import PriorityQueue

class Node:
    def __init__(self, value, weight) -> None:
        self.value = value
        self.weight = weight
    
    def __lt__(self, node):
        return self.weight < node.weight

    def __str__(self):
        return 'Value: {}, Weight: {}'.format(self.value, self.weight)


q = PriorityQueue()

q.put(Node(2,3))
q.put(Node(1,2))
q.put(Node(6,-1))
q.put(Node(5,0))

while not q.empty():
    node = q.get()
    print(node)
    print(node.value, node.weight)