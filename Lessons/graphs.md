## Graphs

Are more general structure than trees. We can think of a tree as a special kind of graph.

Can be used to represent many real world things such as systems of roads, airline flights from city to city, how the internet is connected, etc.

Can be used to solve very difficult problems.

### Terminologies

**Vertex** (**Node**) => fundamental part of a graph.

- It can have a name (key).
- Can have additional information (payload)

**Edge**
An edge connects two vertices to show that there is a relationship between them.
Edges may be one-way or two-way. If the edges in a graph are all one-way, we say the graph is a **directed graph**, or a **digraph**.

**Weight**
Edges may be weighted to show that there is a cost to go from one vertex to another. For example in a graph of roads that connect one city to another, the weight on the edge might represent the distance between the two cities.

#### Graph

A graph can be represented by **G** where **G** = (V,E). For the graph **G**, **V** is a set of vertices and E is a set of edges. Each edge is a tuple (**v,w**) where **v,w** is a subset of **V**. We can add a third component to the edge tuple to represent a weight.
A subgraph **s** is a set of edges **e** and vertices **v** such that e is an subset of **E** and **v** is a subset of **V**
[]images

#### Path

A path in a graph is a sequence of vertices that are connected by edges. Formally we would define a path as **w1,w2,...,wn** such that (**wi, wi+1**) is a subset of **E** for all 1 <= i <= n-1

#### Cycle

A cycle in a directed graph is a path that starts and ends at the same vertex. A graph with no cycles is called an acyclic graph. A directed graph with no cycles is called a directed acyclic graph or DAG. We

### Adjacency Matrix

One of the easiest ways to implement a graph is to use a two-dimensional matrix.
In this matrix implementation, each of the rows and columns represent a vertex in the graph.
The value that is stored in the cell at the intersection of row **v** and column **w** indicates if there is an edge from vertex **v** to vertex **w**.

When two vertices are connected by an edge, we say that they are **adjacent**.

The **advantage** is that the adjacency matrix is simple, and for small graphs it is easy to see which nodes are connected to other nodes.
However, most of the cells in the matrix are empty. Because most of the cells are empty we say that this matrix is "sparse". A matrix is not a very efficient way to store sparse data.
The adjacency matrix is a good implementation for a graph when the number of edges is large.
Since there is one row and one column for every vertex in the graph, the number of edges required to fill the matrix is **$|V|^2$**.
A matrix is full when every vertex is connected to every other vertex.

### Adjacency List

A more space-efficient way to implement a sparsely connected graph is to use an adjacency list.
In an adjacency list implementation we keep a master list of all the vertices in the Graph object and then each vertex object in the graph maintains a list of the other vertices that it is connected to.
In our implementation of the Vertex class we will use a dictionary rather than a list where the dictionary keys are the vertices, and the values are the weights `{vertex : weight}`.
The advantage of the adjacency list implementation is that it allows us to compactly represent a sparse graph.
The adjacency list also allows us to easily find all the links that are directly connected to a particular vertex.

### Search

#### Breath First Search (BFS) algorithms

Given a graph **G** and a starting vertex **s**, a breadth first search proceeds by exploring edges in the graph to find all the vertices in **G** for which there is a path from **S**.
The remarkable thing about a breadth first search is that it finds all the vertices that are a distance **k** from **s** before it finds any vertices that are a distance **k + 1**.
One good way to visualize what the breadth first search algorithm does is to imagine that it is building a tree, one level of the tree at a time. A breadth first search adds all children of the starting vertex before it begins to discover any of the grandchildren.
To keep track of its progress, BFS colors each of the vertices white, gray, or black.
All the vertices are initialized to white when they are constructed.

- A white vertex is an undiscovered vertex.
- When a vertex is initially discovered it is colored gray, and when BFS has completely explored a vertex it is colored black.
- This means that once a vertex is colored black, it has no white vertices adjacent to it.
- A gray node, on the other hand, may have some white vertices adjacent to it, indicating that there are still additional vertices to explore.
- BFS begins at the starting vertex s and colors start gray to show that it is currently being explored.
- Two other values, the distance and the predecessor, are initialized to 0 and None respectively for the starting vertex. Finally start is placed on Queue. The next step is to begin to systematically explore vertices at the front of the queue.
- We explore each new node at the front of the queue by iterating over its adjacency list. As each node on the adjacency list is examined it color is checked.
- It it is white, the vertex is unexplored, and four things happen:
  1. The new, unexplored vertex **neighbor (nbr)**, is colored gray.
  2. the predecessor of **nbr**, is set to the current node **current_vert**
  3. The distance to **nbr** is set to the distance to **current_vert + 1**.
  4. nbr is added to the end of a queue. Adding **nbr** to the end of the queue effectively schedules this node for further exploration, but not until all the other vertices on the adjacency list of the **current_vert** have been explored.
