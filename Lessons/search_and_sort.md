## Search and Sort Algorithms

### Sequential Search Analysis

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
