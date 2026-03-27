import random

# Define TreeNode class for Binary Search Tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper function to recursively insert values."""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def inorder_traversal(self, node, result=[]):
        """Perform inorder traversal of the BST."""
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

# Function to generate a random BST with specified number of nodes
def generate_random_bst(num_nodes=36, min_val=1, max_val=1000):
    """
    Generate a random Binary Search Tree with specified number of nodes.
    
    Args:
        num_nodes: Number of nodes (default: 36)
        min_val: Minimum value range
        max_val: Maximum value range
    
    Returns:
        BinarySearchTree object
    """
    bst = BinarySearchTree()
    for _ in range(num_nodes):
        bst.insert(random.randint(min_val, max_val))
    return bst

# Define GeneralTreeNode class for General Tree
class GeneralTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# Function to generate a random General Tree with specified number of nodes
def generate_random_general_tree(num_nodes=36, min_val=1, max_val=1000):
    """
    Generate a random General Tree (N-ary tree) with specified number of nodes.
    
    Args:
        num_nodes: Number of nodes (default: 36)
        min_val: Minimum value range
        max_val: Maximum value range
    
    Returns:
        Root node of the general tree
    """
    if num_nodes <= 0:
        return None
    
    # Create all nodes first
    nodes = [GeneralTreeNode(random.randint(min_val, max_val)) for _ in range(num_nodes)]
    root = nodes[0]
    
    # Randomly assign parent-child relationships
    for i in range(1, num_nodes):
        parent_index = random.randint(0, i - 1)
        nodes[parent_index].children.append(nodes[i])
    
    return root

# Function to print general tree (level-order traversal)
def print_general_tree(root):
    """Print general tree in level-order traversal."""
    if not root:
        return
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(f"Node: {node.value}, Children: {[child.value for child in node.children]}")
        queue.extend(node.children)

# Example usage
if __name__ == "__main__":
    # Generate random BST with 36 nodes
    bst = generate_random_bst(36, 1, 1000)
    print("Binary Search Tree (inorder traversal):")
    print(bst.inorder_traversal(bst.root))
    
    # Generate random General Tree with 36 nodes
    print("\nGeneral Tree (level-order traversal):")
    general_tree_root = generate_random_general_tree(36, 1, 1000)
    print_general_tree(general_tree_root)