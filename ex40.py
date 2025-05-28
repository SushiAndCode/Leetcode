from collections import deque

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

def print_tree_level_order(root):
    if not root:
        print("Empty tree")
        return

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Trim trailing Nones
    while result and result[-1] is None:
        result.pop()

    print(result)

def pathSum(root: TreeNode, targetSum: int) -> int:
    
    pila = []
    appo = root
    tupl = (appo, [])
    pila.append(tupl)
    counter = 0

    while pila:

        supp = pila.pop()
        vect = supp[1] 
        if supp[1]:
            vect = [x+supp[0].val for x in supp[1]]


        vect.append(supp[0].val)

        for i in targetSum:
            if i == targetSum:
                counter += 1

        if supp[0].left:
            pila.append((supp[0].left, vect))
        if supp[0].right:
            pila.append((supp[0].right, vect))

    return counter


values = [0,1,1]
tree_root = build_tree(values)
pathSum(tree_root, 1)