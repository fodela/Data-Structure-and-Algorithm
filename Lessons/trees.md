## Trees

#### Properties

1. A tree data structure like a real tree has root, branches and leaves
   The difference is that in CS a tree data structure has its root at the top and its leaves at the bottom. Think of it as an inverted tree

2. All of the children of one node are independent of the children of another node

3. Each leaf node is unique

Examples

1. file system, directory or folders
2. Webpage

#### Vocabularies

- **Node**

  - Is a fundamental part of a tree. It can have a name, which we call a "key".
  - May also have additional information called "payload"
    While the payload information is not central to many tree algorithms, it is often critical in applications that make use of trees.

- **Edge**

  - Another fundamental part of a tree.
  - It connects two nodes to show that there is a relationship between them
  - Every node (except the root) is connected by exactly one incoming edge from another node.
  - Each node may have several outgoing edges.

- **Path**

  - Is an ordered list of nodes that are connected by edges.
  - e.g Carnivora -> Felidae -> Felis ,is a path

- ** Children**

  - The set of nodes 'c' that have incoming edges from the same node are said to be the children of that node.

- **Parent**

  - A node is the parent of all the nodes it connects to with outgoing edges.

- **Sibling**

  - Children of the same parent

- **SubTree**

  - A set of nodes and edges comprised of a parent and all the descendants of that parent.

- **Leaf Node**

  - A node that has no children.

- **Level**

  - The number of edges on the path from the root node to n

- **Height**

  - The of a tree is equal to the maximum level of any node in the tree.

**Full Definition of a tree**

- A tree consists of a set of nodes and a set of edges that connect pairs of nodes. A tree has the ff properties:
  - One node of the tree is designated as the root node.
  - Every node n, except the root node, is connected by an edge from exactly one other node p, where p is the parent of n.
  - A unique path traverses from the root to each node.
  - If each node has a maximum of two children we call that tree a **binary tree**

**Recursive definition of a tree**

- A tree is either empty or consists of a root and zero or more subtrees, each of which is also a tree

- The root of each subtree is connected to the root of the parent tree by an edge.

#### Tree Traversal

There are three commonly used patterns to visit all the nodes in a tree.

1. Preorder
2. Inorder
3. Postorder

They can be implemented as function outside the BinaryTree (better way of doing it because is rarely used) or as methods in the BinaryTree

The difference between these patterns is the order in which each node is visited (a "traversal")

**Preorder**
In a preorder traversal, we visit the root node first, then recursively do a preorder traversal of the left subtree, followed by a recursive preorder traversal of the right subtree

root node => left subtree => right subtree

Example use:

1. Reading through a book

```python
def preorder(tree):
  if tree:
    # get the root
    print(tree.get_root_value())

    # recursively get the left children
    preorder(tree.get_right_child)

    # get the right children
    preorder(tree.get_left_child)
```

**Inorder**
We recursively do an inorder traversal on the left subtree, visit the root node, and finally do a recursive inorder traversal of the right subtree

left subtree => root node => right node

```python
def inorder(tree):
  if tree:
    inorder(tree.get_left_child)
    print(tree.get_root.val())
    inorder(tree.get_right_child)
```

**Postorder**
We recursively do an postorder traversal on the left subtree, and the right subtree followed by a
visit to the root node

left subtree => right node => root node

```python
def postorder(tree):
  if tree:
    postorder(tree.get_left_child)
    postorder(tree.get_right_child)
    print(tree.get_root.value())
```

#### Priority Queues with Binary Heaps

**Priority Queue**
Priority queue acts like a queue in that you dequeue an item by removing it from the front.
However, in a priority queue , the logical order of items inside a queue is determined by their priority.

The highest priority is at the front of the queue while the lowest is at the back.
When you enqueue an item on a priority queues, the new item may move all the way to the front depending on its priority.

**Binary Heap**
Binary Heap is a classic way to implement a priority queue. A binary heap will allow us both enqueue and dequeue items in O(logn).
Two main variations

1. Min heap => the smallest key is always at the front
2. Max heap => the largest key value is always at the front

#### Binary Search Trees (BST)

**BST property** => Keys that are less than the parent are found in the left subtree whilst those greater than the parent are found in the right subtree
NB BST property only refers to the direct parent not the entire tree.
Implementation is similar to linked list implementation
We need two classes, BinarySearchTree and TreeNode to enable us create and work with a binary search tree that is empty also.
The BinarySearchTree class has a reference to the TreeNode that is the root of the binary search tree. In most cases the external methods defined in the outer class simply check to see if the tree is empty.
If there are nodes in the tree, the request is just passed on to a private method defined in the BinarySearchTree class that takes the root as parameter.
In the case where the tree is empty or we want to delete the key at the root of the tree, wee must take special action.

**Deleting nodes of a BST**

1. Search tree for node to be deleted
   1. If the tree has more than one node use the "\_get" method to find the node
   2. If the tree has a single node then we are removing the root of the tree. But we still check if the key matches that of the root.
2. Remove the node

   - 3 possible cases

     1. Node to be deleted has no children (is a leaf)
        - remove the node (check whether right or left child and make the parent left or right child none)
     2. Node to be deleted has both children

        - Because the node has two children we cannot just promote one child by random but rather

        1. we search the tree for a node that can replace the node to be deleted (this node is called the successor(xtics of a successor... )) using find_min and find_successor methods.
           - find_successor method:
             - because the element on the right are larger than the parent, the successor is the smallest child in the right subtree
             - else if the node has no right child but is the left_child of its parent then the parent is the successor
           - find_min method:
             - the minimum value in a BST is the left most child of the tree (left_child without a a left_child).
             - ```python
               def find_min(self):
                 current = self
                 while current.has_left_child:
                   current = current.left_child
                 return current
               ```

        - The successor is guaranteed to have no more than one child. We remove the successor splice_out method.
        - Then we put this successor in place of the node to be deleted.
        -

     3. Node to be deleted has only one child (else -> not leaf and not has_both_children)
        - Find out which child it has (e.g has_left_child)
          - Find out which child the node to be deleted is to its parent(is_left_child) and make the above child a child of the parent of the node we are removing.
            - If the node to be deleted is not a child, then is a root and because the root has no parent we use replace_node_data method which replaces the data of the root to that of the child (the child is now the root)
