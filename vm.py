class VirtualMachine:
    
    def __init__(self):
        self.files = {}

    def run(self):

        while True:
            inp = input("> ").lower()
            if "touch" in inp:
                self.touch(inp)
            elif inp == "exit":
                break
            else:
                print("Unknown command.")

    def touch(self, inp):
        parts = inp.split()
        if parts[0] == "touch":
            filename = parts[1]
            self.files[filename] = ""
            print(f"File '{filename}' is created.")



if __name__ == "__main__":
    vm = VirtualMachine()
    vm.run()

