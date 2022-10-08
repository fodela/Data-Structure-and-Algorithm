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
