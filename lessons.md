## Array Sequences

- ### 3 main array sequences in python

  1. List
  2. Tuples
  3. Strings
     NB: they all support indexing

  ### How computer store information

  - ### Low-level computer architecture

    - Computer store data in bits. Every 8 bits make up a byte (just like how every 60s = 1 min ). Every byte have a unique address associated with it that enable the computer access the data on it. e.g byte #3028
      Computer hardware is designed to access any byte of the main memory efficiently by making the main memory perform as random access memory (RAM) thus any byte can be retrieved easily no matter the address in a order 1 time or constant time => O(1)

      - Programming language keep track of the association btn an identifier ant he memory address
        -We use single name for the group of related data and index number them to refer to specific element in the group.
      - An array is a group of related variable that can be stored one after another in a contiguous portion of the computer's memory.

      - Python internally represents each unicode character with 16bits (i.e 2 bytes) => 6 character (letter) string will be stored in 12 bytes of memory
      - Each location within an array is called a cell. This location is described using an integer index
      - Each cell must have the same number of byte enabling any cell to be accessed randomly in constant time.
      - Memory address of any data can be calculated using the formula: start + (cell size)(index)
        - start is the address of where the data start

  - ### Higher level abstraction

    - Is the basic abstraction for real-world discussion
    - Is more about indexing rather than cell size and bytes per elements

  - ### Referential Arrays

    - Say we want to store the names of 100 students in a class. In python we can just create a list of string names but each element wont have the same cell size. To solve this we can allocate spaces down for how long each element should be and if less will be filled with spaces but that will be waste of space. The solution is to make arrays using object references. We make each element to be the reference of the object. Now even tho the relative size of each element may vary, the number of bits used to store each is fixed.
    - List and tuples are referential structures.
    - A single list may contain multiple objects and vice versa.
    - When we declare the slice of a list we just referencing objects not create a new list
    - Reassignment jst make the element point to a different object reference.
    - Creating a new list by making a copy of an existing one will just make a shallow copy thus just reference same as above.
    - We use the deep copy function from the copy module of python
    - Referenced integers are immutable. counters[2]+= 1 wont change the original value of counters[2] but rather just use the same cell to reference a new value.
    - Extend copies all references of a particular element to a new list not the a copy of the elements itself.

  ### Dynamic Arrays

  - Dynamic arrays are arrays with the ability to take more elements without you having to increase the capacity of the array yourself
  - Python keeps increasing the memory allocated to an array in order to take more element but is done in chunks so as not to keep increasing the size one by one.

  - ### Implementing a dynamic array
    Allocate a new array B with larger capacity.
    Set B[i]=A[i], for i in range(n-1)
    Set A = B, that is we henceforth use B as the array supporting the list. (A's storage capacity will increase to B's capacity)
    Insert the new element in the new array. (Because it can now take more elements.)
    NB: The rule is to create the new array B to have twice the size of the old array A.

  ### Amortization

  - Amortized analysis analyze the cost (time) per operation
  - ### Amortized analysis for dynamic array
    - Amortized Cost = (n + 2n) / n

## Stacks Queues and Deques

All three uses array or list and its methods.
NB: For me, the front or first of the list is the index len(array) - 1, while the rear, back or last of the list is at index 0
Still just my thoughts:

- Prepend - add things to rear. We implemented it here using " .insert(0,item) "
- Append - add items to the front.

### Stacks

A stack is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end.
This end is commonly referred to as the top.
The end opposite to the top is the base.
It uses the last-in first-out principle => the most recently added is the first to be removed.
Push adds a new item while pop removes an item
E.g web browser history navigation using the back and forward buttons.
It has the ff methods:

1. push()
2. pop()
3. peek()
4. isEmpty()
5. size()

### Queue

Is an ordered collection of items where the addition of new items happens at one end, called the 'rear' and the removal of existing items occurs at the other end, commonly called the front.
This follows the "first-in first-out (FIFO)' principle aka first come first served
It has the ff methods:

1. enqueue(item)
2. dequeue()
3. isEmpty()
4. size()

### Deque

Aka double ended queue, is an ordered collection of items similar to the queue.
It has two ends, a front and a rear, and the items remain positioned in the collection.
Items can be added or moved from both front and rear.
Is a hybrid of principles used by stack and queue but it does not require LIFO nor FIFO orderings that are enforced by stack and queues. Is completely up to you to make consistent use of the addition and removal operations.
It has the following method:

1. isEmpty()
2. size()
3. addFront(item) ==> prepend
4. addRear(item) ==> append
5. removeFront()
6. removeRear()

## Linked lists

### Singly Linked list

A singly linked list is a collection of nodes that collectively form a linear sequence.
Each node stores a reference to an object that is an element of the sequence, as well as a reference to the next node of the list.
The list instance maintains a member name head that identifies the first node of the list
In some applications another member named tail that identifies the last node of the list

- Head => first node of the list. Nothing points to the head.
- Tail => last node and points to nothing. Identified as the node with 'None' as its reference.
- Traversing => going through the nodes and checking the linked list. Also known as link hopping or pointer hopping.

Each node is represented as a unique object, with that instance storing a reference to its element and reference to the next node (or None)

### Inserting an element at the head of singly linked list

An important property of a linked list is that it does not have a predetermined fixed size.
It uses space proportionally to its current number of elements

#### NB: check implementation files for how it is done

Procedure to insert a new element at the head of the list:

1. Create a new node
2. Set its element to the new element
3. Set its next link to refer to the current head
4. Then set the list's head to point to the new node.

### Inserting an element at the tail of a singly linked list

1. Create a new node
2. Assign its next reference to None
3. Set the next reference of the tail to point to this new node
4. Then update the tail reference itself to this new node

### Removing an element from the head of a singly linked list

- Point the head to the second node and remove it.

### Removing an element from a singly linked list

- We cannot easily delete the last node of a singly linked list
- Even if we maintain a tail reference directly to the last node of the list, we must be able to access the node before the last node in order to remove the last node.
- But we cannot reach the node before the tail by following next links from tail
- If we want to support such an operation efficiently, we will need to make our list doubly linked

### Doubly Linked List

We define a linked list in which each node keeps an explicit reference to the node before it and a reference to the node after it.
These lists allow a greater variety of O(1) time update operations, including insertions and deletions.

We continue to use the term "next" for the reference to the node that follows another.

We use the term "prev" for the reference to the node that precedes it.

We add special nodes at both ends (header and trailer nodes).
These "dummy" nodes are knowns as sentinels or guards

### Inserting an element into a doubly linked list

Every insertion into our doubly linked list representation will take place between a pair of existing nodes.
When a new element is inserted at the front of the sequence, we will simply add the new node between the header and the node that is currently after the header.
We change the next pointer and prev pointer to accommodate the new node.

### Inserting a node to Front

1. Header next points to the new node.
2. Previous front node prev points to the new node
3. New node's prev points to header and
4. New node's next points to the previous front node

### Deleting a node

The two neighbors of the node to be deleted are linked directly to each other
As a result, that node will no longer be considered part of the list and it can be reclaimed by the system.
Because of sentinels, the same implementation can be used when deleting the first or the last element of a sequence.

## Recursion

#### What is recursion?

- Two main instances of recursion
  1. Is a technique in which a function makes one or more calls to itself. More common and our major focus for now.
  2. When a data structure uses smaller instances of the exact same type of data structure when it represent itself.

#### Why use recursion?

- It provides a powerful alternative for performing repetitions os tasks in which a loop is not ideal.
- Most modern programming languages support recursion
- Recursion servers as a great tool for building out particular data structures

#### Examples

1. Factorial example =>
   n! = n x (n-1) x (n-2) ... 3 x 2 x 1
   n! = n x (n-1)!
   0! = 1

   Recursive case is: n! = n x (n-1)!
   Base case is: n = 0 because 0! = 1

   Whenever you are trying to develop a recursive solution it is very important to think about the base case, as your solution will need to return the base case once all the recursive cases have been worked through.

#### Memoization

Memoization effectively refers to remembering ('memoization' -> 'memorandum' -> to be remembered) results of method calls based on the method inputs and then returning the remembered result rather than computing the result again. You can think of it as a cache for method results. We'll use this in some of the interview problems as improved versions of a purely recursive solution.

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

The difference between these patterns is the order in which each node is visited (a "traversal")

**Preorder**
In a preorder traversal, we visit the root node first, then recursively do a preorder traversal of the left subtree, followed by a recursive preorder traversal of the right subtree

root node => left subtree => right subtree

**Inorder**
We recursively do an inorder traversal on the left subtree, visit the root node, and finally do a recursive inorder traversal of the right subtree

left subtree => root node => right node

**Postorder**
We recursively do an postorder traversal on the left subtree, and the right subtree followed by a
visit to the root node

left subtree => right node => root node

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
   1. If the tree has more than one node \_get method to find the node
   2. If the tree has a single node then we are removing the root of the tree. But we still check if the key matches that of the root.
