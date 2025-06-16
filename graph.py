from processes.process import Process

from utils import END,get_random_number,MAX_ATTEMPT

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

        retry_count = {}

        def dfs(process_name: str) -> int | None:
            if process_name not in self.processes:
                print(f"[Error] Process '{process_name}' not found.")
                return None
            elif process_name == END:
                return self.array

            process = self.processes[process_name]
            result = process.run(self.array)

            if result is not None:
                random_int = get_random_number()
                print(f"[GRAPH] random number added = {random_int}")
                self.array.append(random_int)
                print(f"[GRAPH] new list = {self.array}")

          

            retry_count[process_name] = retry_count.get(process_name, 1)
            
           

            for condition, next_process in self.edges.get(process_name, []):
                if retry_count[process_name] < MAX_ATTEMPT and condition(result):
                    if next_process == process_name:
                        retry_count[process_name] += 1
                    else :
                        return dfs(next_process)
                    # return dfs(next_process)
                elif retry_count[process_name] >= MAX_ATTEMPT:
                    print(f"[GRAPH] Max attempt reached for {process_name}.Moving to the next process")
                    continue
                else:
                    print("[GRAPH] Moving to next process")
                    continue
                
                return dfs(next_process)

            return result

        print("[GRAPH] started dfs")
        final_result = dfs(start_process)
        print("[GRAPH] ended dfs")
        print(f"[RESULT] = {final_result}")
