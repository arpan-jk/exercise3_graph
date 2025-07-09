from processes.process import Process

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