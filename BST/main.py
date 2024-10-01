class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if node is not None:
            return [node.val] + self._preorder(node.left) + self._preorder(node.right)
        else:
            return []

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            return self._inorder(node.left) + [node.val] + self._inorder(node.right)
        else:
            return []

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        if node is not None:
            return self._postorder(node.left) + self._postorder(node.right) + [node.val]
        else:
            return []

# 允許使用者自行輸入數據
input_data = input("請輸入一系列的數字，以逗號或空格分隔: ")
if ',' in input_data:
    data = list(map(int, input_data.split(',')))
else:
    data = list(map(int, input_data.split()))

bst = BinarySearchTree()
for item in data:
    bst.insert(item)

print("Pre-order traversal:", bst.preorder())
print("In-order traversal:", bst.inorder())
print("Post-order traversal:", bst.postorder())
