# time: O(N) with N is number of nodes in the tree
# space: O(N) recursive stack
def preorder_recursive(root):
    if not root:
        return
    print(root)
    preorder_recursive(root.left)
    preorder_recursive(root.right)

def preorder_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

def postorder_recursive(root):
    if not root:
        return
    postorder_recursive(root.left)
    postorder_recursive(root.right)
    print(root)

def postorder_iterative_1(root):
    if not root:
        return
    lst = []
    stack = [root]
    while stack:
        node = stack.pop()
        lst.append(node)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    for i in range(len(lst) - 1, -1, -1):
        print(lst[i].val)

def inorder_recursive(root):
    if not root:
        return
    postorder_recursive(root.left)
    print(root.val)
    postorder_recursive(root.right)

def inorder_iterative(root):
    if not root:
        return
    stack = []
    while stack or root is not None:
        while root:
            stack.append(root)
            root = root.left

        node = stack.pop()
        print(node.val)
        root = node.right










