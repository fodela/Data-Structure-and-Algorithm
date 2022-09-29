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

#### Hash functions for integer elements

1. Remainder method

   - place the item at the mod(table size) -> e.g for a hash table of size 11, the item 54 will be; `54 % 11 = 10` `54` will be placed at slot `10`
   - **load factor** = number of items / table size
   - to search for an item, compute the slot name using the hash function and then check the hash table to see if it is present.
   - **Collision** => two or more items that may result in the same location.

2. Folding methods
   1. Divide the items into equal size pieces (the last piece may not be of equal size)
   2. These pieces are then added together to give the resulting hash value
   3. e.g:
      - if item is a phone number `436-555-46011`
      - we take the digits and divide them into - groups of 2 (43,65,55,46,01)
      - add the numbers => 210
      - assuming our hash table has 11 slots, 210 % 11 = 1
      - the phone number `436-555-46011` is stored in slot 1
3. Mid Square Method
   1. Square the item
   2. extract some portion of the resulting digits
   3. e.g
      - item = `44`
      - `44**2` = `1936`
      - extract the middle 2 digits `93`
      - assume table length is 11, `93 % 11 = 5`
