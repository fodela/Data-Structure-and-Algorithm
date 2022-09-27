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
