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