# Chapter 06

- Terms enqueue and dequeue means push and pop.
- A queue follows the FIFO(First In First Out) rule, A stack follows the LIFO(Last In First Out) rule.
- BFS(Breadth-First Search) tells you if there's a path from A to B, else if find the shortest path.
- You must check people in the order they were added to the search list, so use queues is one solution, otherwise the shortest path can be wrong.
- When you check someone, make sure the next time you don't check them again, otherwise the procedure will step into a infinite loop.
- A tree is always a graph, with no edges point back.