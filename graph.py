from processes.process import Process

from utils import END,get_random_number,MAX_ATTEMPT

class Graph:
    def __init__(self, input_array: list[int]):
        self.processes: dict[str, Process] = {}
        self.edges: dict[str, list[tuple[callable, str]]] = {} #can go to that node only when the callable function is satisfied
        self.array = input_array  

    def add_process(self, name: str, process: Process):
        self.processes[name] = process
        self.edges[name] = []

    def add_edge(self, from_process: str, to_process: str, condition: callable):
        self.edges[from_process].append((condition, to_process))

    def run(self, start_process: str):

        retry_count = {} #if > MAX_ATTEMPT, send to the next process

        def dfs(process_name: str) -> int | None:
            result = None
            if retry_count.get(process_name) is None:
                retry_count[process_name] = 1
         
            move_to_other = False
            if retry_count[process_name] > MAX_ATTEMPT:
                move_to_other = True


            if process_name not in self.processes:
                print(f"[Error] Process '{process_name}' not found.")
                return None
            elif process_name == END:
                return self.array

            if move_to_other == False:
                process = self.processes[process_name]
                result = process.run(self.array)


            if result is not None:
                random_int = get_random_number()
                print(f"[GRAPH] random number added = {random_int}")
                self.array.append(random_int)
                print(f"[GRAPH] new list = {self.array}")



            for condition, next_process in self.edges.get(process_name, []):
                if move_to_other == True and next_process != process_name:
                    dfs(next_process)
                elif move_to_other == True and next_process == process_name:
                    print("[GRAPH] Max attempt reached. Moving to next process.")
                    continue
                elif move_to_other == False and condition(result):
                    if next_process == process_name:
                        retry_count[process_name] += 1
                    dfs(next_process)
                else:
                    continue
                     
                      
               


            return result

        print("[GRAPH] started dfs")
        dfs(start_process)
        print("[GRAPH] ended dfs")
        print(f"[RESULT] = {self.array}")
