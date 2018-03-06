# Chapter 03

- Recursion is a when a function calls itself.
- Recursive functions have two cases: the base case which terminates the recursion to prevent the stack overflow(so you should never forget add a base case inside your recursive function), and the recursive case which calls the function itself.
- All function calls go onto the call stack.
- Python interpreter stack has the maximum depth, default to 3000, function sys.getrecursionlimit() can get the limit, if you want to change it, try sys.setrecursionlimit(limit).