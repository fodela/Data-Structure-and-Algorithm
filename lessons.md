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

      - Python internally represents each unicode character with 16bits (i.e 2 bytes) => 6 xter (letter) string will be stored in 12 bytes of memory
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
