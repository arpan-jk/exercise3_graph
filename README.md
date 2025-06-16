
---

# 🧠 EXERCISE3\_GRAPH

This is a modular Python project that simulates a **process graph traversal** using **DFS (Depth-First Search)**. Each node in the graph represents a mathematical operation (like addition, multiplication, division), and transitions between them are based on **conditional logic** and **retry limits**.

---

## 📁 Project Structure

```
EXERCISE3_GRAPH/
│
├── processes/                  # Contains all process node definitions
│   ├── additon.py             # Addition process logic
│   ├── division.py            # Division process logic
│   ├── multiplication.py      # Multiplication process logic
│   └── process.py             # Base Process class
│
├── graph.py                   # Graph class that manages nodes and DFS traversal
├── input.py                   # User input handling
├── main.py                    # Entry point: builds the graph and runs the process flow
├── utils.py                   # Helper functions (e.g., random number generation)
└── README.md                  # Project overview and usage
```

---

## 🧩 Core Concepts

* **Process Nodes**: Defined as Python classes. Inherit from a base `Process` class and implement custom `run()` logic.
* **Graph Traversal**: Uses **DFS** to move from one node to another based on **lambda conditions**.
* **Self-loops with Retry Limit**: A process can retry itself up to a defined number of times before moving on.
* **Dynamic Conditions**: Each edge is conditional (e.g., result is even/odd).

---

## 🚀 How It Works

1. The user provides an initial list of integers.
2. The `Graph` is constructed with processes as nodes.
3. Conditional edges (like `is_even`, `is_odd`, etc.) are added between processes.
4. The graph is traversed starting from the `START` node using **depth-first search**.
5. After each process execution, a random number is added to the input to simulate dynamic behavior.
6. Processes like `ADD`, `MULT`, `DIV`, etc., compute results and print logs.

---

## 🛠 How to Run

run:

```bash
python3 main.py
```

---

## 📦 Dependencies

This project only uses standard Python libraries:

* `random`

---

## 🧪 Sample Execution

```
[GRAPH] started dfs
[START] started.
[START] result = None
[START] ended.
[GRAPH] random number added = 3
[GRAPH] new list = [10000, 2, 3, 4, 3]
[ADD] started.
[ADD] result = 10012
[ADD] ended.
...
[GRAPH] ended dfs
[RESULT] = 2503
```

---

## ✅ Features

* Modular design — clean separation of logic in files
* Easy to extend (e.g., add more process types)
* Retry-based control flow
* Custom input and branching logic



