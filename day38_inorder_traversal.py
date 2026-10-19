
import time


class TreeNode:
    """A node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_sample_tree():
    """
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
    """
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root


def inorder_recursive(root):
    """Visit Left -> Root -> Right using recursion."""
    result = []

    def traverse(node):
        if node is None:
            return

        traverse(node.left)
        result.append(node.value)
        traverse(node.right)

    traverse(root)
    return result


def inorder_iterative(root):
    """Visit Left -> Root -> Right using an explicit stack."""
    result = []
    stack = []
    current = root

    while current is not None or stack:
        # Reach the leftmost node.
        while current is not None:
            stack.append(current)
            current = current.left

        # Visit the node at the top of the stack.
        current = stack.pop()
        result.append(current.value)

        # Process its right subtree.
        current = current.right

    return result


def visualize_tree():
    """Print a readable diagram of the sample tree."""
    print("\n=== ROYAL FAMILY TREE ===")
    print("              1")
    print("            /   \\")
    print("           2     3")
    print("          / \\   / \\")
    print("         4   5 6   7")


def visualize_inorder(root):
    """Print each node in the order it is visited."""
    print("\n=== INORDER TRAVERSAL STEPS ===")

    result = []

    def traverse(node):
        if node is None:
            return

        traverse(node.left)

        result.append(node.value)
        print(f"Visit node {node.value}: {result}")

        traverse(node.right)

    traverse(root)

    print("\nFinal traversal:", " -> ".join(map(str, result)))


def main():
    print("=" * 50)
    print("       THE ROYAL LINEAGE DECODER")
    print("=" * 50)

    root = build_sample_tree()
    visualize_tree()

    # Recursive traversal benchmark
    start = time.perf_counter()
    recursive_result = inorder_recursive(root)
    recursive_time = time.perf_counter() - start

    # Iterative traversal benchmark
    start = time.perf_counter()
    iterative_result = inorder_iterative(root)
    iterative_time = time.perf_counter() - start

    print("\n=== RESULTS ===")
    print("Recursive inorder:", recursive_result)
    print("Iterative inorder:", iterative_result)

    print("\n=== PERFORMANCE COMPARISON ===")
    print(f"Recursive time: {recursive_time:.8f} seconds")
    print(f"Iterative time: {iterative_time:.8f} seconds")
    print("Results match:", recursive_result == iterative_result)

    visualize_inorder(root)

    print("\n=== COMPLEXITY ===")
    print("Time: O(n) for both approaches")
    print("Auxiliary space: O(h) for both approaches")
    print("n = number of nodes, h = tree height")


if __name__ == "__main__":
    main()
