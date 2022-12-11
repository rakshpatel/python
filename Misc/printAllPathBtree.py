def paths(root):
    if not root:
        return []
    ans = []
    paths_util(root, [], ans)
    return ans

def paths_util(root, path, ans):
    path.append(root.data)

    if root.left:
        paths_util(root.left, path, ans)
    if root.right:
        paths_util(root.right, path, ans)

    if not root.left and not root.right:
        ans.append(path[:])
        
    path.pop()
    


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)
    root.right.right.right = Node(9)
    
    roots = paths(root)
    print(roots)