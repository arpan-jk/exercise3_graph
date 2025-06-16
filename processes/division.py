from processes.process import Process

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