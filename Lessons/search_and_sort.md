# Search and Sort Algorithms

## Search Algorithms

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
NB: Python has a built in dictionary that serves as a hash table.

**Slots** => position of the hash table. Each slot is named by an integer value starting from 0

**Hash function** => (maps items to slot) the mapping between an item and the slot where that item belongs in the hash table.

**Perfect hash function** => one that maps each item into a unique slot.

**Hash functions**:
Our goal is to create a hash function that minimizes the number of collisions, easy to compute and evenly distributes the items in the hash table.

**Rehashing** => the process of looking for another slot after a collision.

**Mapping** => the idea of a dictionary as a hash table to get and retrieve items using keys.

#### Hash functions for integer elements

1. Remainder method

   - place the item at the mod(table size) -> e.g for a hash table of size 11, the item 54 will be; `54 % 11 = 10` `54` will be placed at slot `10`
   - **load factor** = number of items / table size
   - to search for an item, compute the slot name using the hash function and then check the hash table to see if it is present.
   - Collision may occur and we use collision resolution to solve it.

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

#### Hash functions for non-integer elements

We get the ordinal values of the string
Python has the inbuilt method `ord`
e.g "cat" => `ord("c")` = 99 `ord("a")`= 97 `ord("t")` = 116 => 312
312 % 11 = 4

#### Collision Resolution

Dealing with cases where 2 or more items will have the same slot. e.g 44 and 77 in a table of length 11 will both be in slot 1.

1. Open addressing
   -Uses rehashing
   - Looks into the hash table and tries to find the next open slot or address in the hash table to hold the item that caused the collision.
   - By systematically visiting each slot one at a time, we are performing an open addressing technique called linear **linear probing**.
   - Linear probing however cluster the items to the beginning of the hashtable.
   - Deal with clustering. One way to deal with clustering is to skip slots thereby more evenly distributing the items that have caused collisions.
   - A variation of the linear probing idea is called **quadratic probing**. Instead of using a constant "skip" value, wee use a rehash function that increments the hash value by 1,3,5,7,9 and so on. Thus if the first hash value is h, the successive values are h+1, h+4, h+9, h+16 and so on.
2. Chaining
   - Allows many items to exist at the same location in the hash table.
   - When collisions happen, the item is still placed in the proper slot of the hash table.
     <!-- FIXME: add image-->
     NB: When more and more items hash to the same location, the difficulty of searching for the item in the collection increases.

## Sort Algorithms

### Bubble Sort

The bubble sort loops through a list multiple times and compares adjacent items and exchanges those that are out of order . Each pass through the list places the next largest value in its proper place. In essence, each item "bubbles" up to the location where it belongs.
e.g
Sorting `[3,2,1,4]` in ascending gives:

1. 3 is swapped with 2 and 3 is again swapped with 1 => `[2,1,3,4]`
2. 2 is then swapped with 1 => `[1,2,3,4]`

[visualize bubble sort](https://visualgo.net/en/sorting)

### Selection sort

The selection sort improves on the bubble sort by making only one exchange for every pass through the list. It finds the largest (or smallest if ascending) value as it makes a pass and, after completing the pass, places it in the proper location. As with bubble sort, after the first pass, the largest item is in the correct place. After the second pass, the next largest is in place. This process continues and requires n-1 passes to sort n items, since the final item must be in place after the (n-1)st pass.
[visualize select sort](https://visualgo.net/en/sorting)

### Insertion sort

The insertion sort always maintains a sorted sub-list in the lower positions of the list.
Each new item is then "inserted" back into the previous sub-list such that sorted sub-list is one item larger
We begin by assuming that a list with one item (position 0) is already sorted.
On each pass, one for each item 1 through to n-1, the current item is checked against those in the already sorted sub-list.
As we look back into the already sorted sub-list, we shift those items that are greater to the right.
When we reach a smaller item or the end of the sub-list, the current item can be inserted.

[visualize insertion sort](https://visualgo.net/en/sorting)
