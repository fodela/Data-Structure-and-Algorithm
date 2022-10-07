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
