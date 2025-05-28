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

def maxDepth(root: TreeNode) -> int:
    
    pila = [root]
    av = set()
    appo = root
    counter = 1
    if appo.left:
        appo = appo.left
    elif appo.right:
        appo = appo.right
    else:
        return counter
    if root.right:
            pila.append(root.right)
    pila.append(appo)
    maxx = 0               
    while pila:
        if appo.left and appo.left not in av:   
            pila.append(appo)
            if appo not in av:
                counter += 1
                av.add(appo)
            av.add(appo)
            appo = appo.left
        elif appo.right and appo.right not in av:
            pila.append(appo)
            if appo not in av:
                counter += 1
                av.add(appo)
            appo = appo.right
        else:
            counter += 1
            if counter > maxx:
                maxx = counter
            counter -= 1
            av.add(appo)
            appo = pila.pop()
        
    return maxx

values = [1,2,3,4,None,None,5]
tree_root = build_tree(values)
counter = maxDepth(tree_root)
print(counter)
print_tree_level_order(tree_root)