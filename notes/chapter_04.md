# Chapter 04

- The basic idea of D&C(Divide-and-Conquer): Divide a complex problem into several simple sub-problems, then solve them to get the solution of the original problem.
- Recursion is one of the solutions about D&C, and usually it's the most common solution, because a lot of D&C problems can divide into several sub-problems which have a same structure as their original problem, just like the recursive problems.
- Recursion requires the latter problem returns before its previous problem, D&C have no concern about how problems return, it just focuses on the final return.
- When two algorithm both have the same Big O Notation expression, the constant matters. Otherwise the constant is insignificant, for instance, the simple search and the binary search.
- In a usual case, the quick sort is fast than the bubble sort, choose a random pivot in every recursion to applt the avg case(but it can't avoid the worst case perfectly, just in the maximum extent possibility).