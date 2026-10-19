# Day 38 – The Royal Lineage Decoder

## Overview

This project implements **Binary Tree Inorder Traversal** using recursive and iterative approaches in Python.

It demonstrates binary tree construction, traversal order, stack operations, visualization, and algorithm complexity.

## Problem Statement

Given the root of a binary tree, return the inorder traversal of its nodes.

Inorder traversal follows:

**Left Subtree → Root → Right Subtree**

## Example

```text
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

**Output**
```text
[4, 2, 5, 1, 6, 3, 7]
```

## Approaches

### 1. Recursive Traversal

1. Traverse the left subtree.
2. Visit the current node.
3. Traverse the right subtree.

The function call stack manages the traversal.

### 2. Iterative Traversal

1. Push nodes onto an explicit stack while moving left.
2. Pop and visit the next node.
3. Move to its right subtree.
4. Repeat until the current node and stack are both empty.

## Complexity Analysis

For both approaches:

- **Time:** O(n)
- **Auxiliary space:** O(h)

Here, n is the number of nodes and h is the tree height.

## Features

- Binary tree construction
- Recursive inorder traversal
- Iterative inorder traversal using a stack
- Traversal sequence visualization
- Result verification
- Execution-time comparison

## How to Run

Requirements: Python 3.

```bash
python day38_inorder_traversal.py
```

## Real-World Applications

- File-system hierarchy traversal
- Database index structures
- Compiler syntax trees
- Document Object Model (DOM) processing
- Hierarchical data processing

## Learning Outcomes

- Understood binary tree structure.
- Implemented recursive and iterative algorithms.
- Practiced stack-based traversal.
- Compared algorithm complexity.
- Verified that two implementations produce the same result.

**Day 38 Status:** Completed – Trees.
