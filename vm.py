from program import Program

class VirtualMachine:
    
    def __init__(self):
        self.files = {}
        self.program = Program(self)

    def run(self):

        while True:
            inp = input("> ").lower()
            if inp.startswith("touch"):
                self.program.touch(inp)
            elif inp.startswith("list"):
                self.program.list(inp)
            elif inp.startswith("cat"):
                self.program.cat(inp)
            elif inp.startswith("echo"):
                self.program.cat(inp)
            elif inp == "exit":
                break
            else:
                print("Unknown command.")


if __name__ == "__main__":
    vm = VirtualMachine()
    vm.run()

