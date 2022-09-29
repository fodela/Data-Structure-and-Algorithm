## Search and Sort Algorithms

### Sequential Search

**Analysis**

#### Unordered List

Searches through until it find the element

|    Situation    | Best case | Worse case | Average |
| :-------------: | :-------: | :--------: | :-----: |
| item is present |     1     |     n      |   n/2   |
|   item absent   |     n     |     n      |    n    |

#### Ordered List

Searches through until it find the element or an element greater than the element

|    Situation    | Best case | Worse case | Average |
| :-------------: | :-------: | :--------: | :-----: |
| item is present |     1     |     n      |   n/2   |
|   item absent   |     1     |     n      |   n/2   |

[View implementation](search_and_sort.md)

---

### Binary Search

NB: Uses **Divide and Conquer**

We order the list and start searching from the middle. If the value of the middle element is less than the searched element we discard all the element on the right and vice versa. We repeat this until we find the element we are searching for.

**Analysis**
n/2\*\*i

---

### Hashing

#### Definitions

**Hashing** => building a data structure that can be searched in O(1).

**Hash table** => a collection of item that is stored in such a way as to make it easy to find them later. Can be implemented using list or arrays.

**Slots** => position of the hash table. Each slot is named by an integer value starting from 0

**Hash function** => (maps items to slot) the mapping between an item and the slot where that item belongs in the hash table.

**Perfect hash function** => one that maps each item into a unique slot.

**Hash functions**:
Our goal is to create a hash function that minimizes the number of collisions, easy to compute and evenly distributes the items in the hash table.
