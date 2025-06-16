from processes.process import Process

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