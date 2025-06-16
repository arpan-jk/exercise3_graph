class Process:
    def __init__(self, name):
        self.name = name

    def start(self):
        print("========================")
        print(f"[{self.name}] started.")

    def end(self):
        print(f"[{self.name}] ended.")
        print("========================")

    def print_result(self, result):
        print(f"[{self.name}] result = {result}")

    def run(self, inputs: list[int]) -> int | None:
        """ Default placeholder process that just logs. """
        self.start()
        self.print_result(inputs)
        self.end()
        return None


class ProcessAdd(Process):
    def run(self, inputs: list[int]) -> int | None:
        self.start()
        if not inputs:
            print("No input provided")
            return None
        result = sum(inputs)
        self.print_result(result)
        self.end()
        return result


class ProcessMult(Process):
    def run(self, inputs: list[int]) -> int | None:
        self.start()
        if not inputs:
            print("No input provided")
            return None
        result = 1
        for num in inputs:
            result *= num
        self.print_result(result)
        self.end()
        return result


class ProcessDiv(Process):
    def run(self, inputs: list[int]) -> int | None:
        self.start()
        if not inputs or inputs[-1] == 0:
            print("Invalid input or divide by zero")
            return None
        result = inputs[0] // inputs[-1]
        self.print_result(result)
        self.end()
        return result


class Graph:
    def __init__(self, input_array: list[int]):
        self.processes: dict[str, Process] = {}
        self.edges: dict[str, list[tuple[callable, str]]] = {}
        self.array = input_array.copy()  # to avoid side effects

    def add_process(self, name: str, process: Process):
        self.processes[name] = process
        self.edges[name] = []

    def add_edge(self, from_process: str, to_process: str, condition: callable):
        self.edges[from_process].append((condition, to_process))

    def run(self, start_process: str):

        def dfs(process_name: str) -> int | None:
            if process_name not in self.processes:
                print(f"[Error] Process '{process_name}' not found.")
                return None
            elif process_name == END:
                return self.array

            process = self.processes[process_name]
            result = process.run(self.array)

            if result is not None:
                self.array.append(result)

            for condition, next_process in self.edges.get(process_name, []):
                if condition(result):
                    return dfs(next_process)

            return result

        print("[GRAPH] started dfs")
        final_result = dfs(start_process)
        print("[GRAPH] ended dfs")
        print(f"[RESULT] = {final_result}")


# Conditions
is_even = lambda x: x is not None and x % 2 == 0
is_odd = lambda x: x is not None and x % 2 == 1
move_direct = lambda x: True

# Process names
ADD, MULT, DIV, START, END = "ADD", "MULT", "DIV", "START", "END"

# Processes
graph = Graph([2, 2, 3, 4])

p_start = Process(START)

graph.add_process(START, p_start)
graph.add_process(END, Process(END))
graph.add_process(ADD, ProcessAdd(ADD))
graph.add_process(MULT, ProcessMult(MULT))
graph.add_process(DIV, ProcessDiv(DIV))

# Edges
graph.add_edge(START, ADD, move_direct)  # start ---> add
graph.add_edge(ADD, ADD, is_odd)
graph.add_edge(ADD, MULT, is_even)
graph.add_edge(MULT, MULT, is_odd)
graph.add_edge(MULT, DIV, is_even)
graph.add_edge(DIV, END, move_direct)

# Run
graph.run(START)
