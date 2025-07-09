# Exercise 3 graph redo

## Algorithmic approach
1. The user runs the main.py file and provides the input as per the requirement 
```bash
python3 main.py
```
2. The user provides an initial list of integers (as per the conditions)
3. The `Graph` is constructed with processes as nodes.
4. Conditional edges (like `is_even`, `is_odd`, etc.) are added between processes.
5. The graph is traversed starting from the `START` node using **depth-first search**.
6. After each process execution, a random number is added to the input to process further.
7. Processes like `ADD`, `MULT`, `DIV`, etc., compute results and print it.

