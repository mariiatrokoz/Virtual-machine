class Program:

    def __init__(self, virt_machine):
        self.virt_machine = virt_machine

    def touch(self, inp):
        parts = inp.split()
        if parts[0] == "touch":
            filename = parts[1]
            self.virt_machine.files[filename] = ""
            print(f"File '{filename}' is created.")

    def list(self, inp):
        if inp == "list":
            if self.virt_machine.files:
                for filename in self.virt_machine.files:
                    print(filename)
            else:
                print("no files found")
    
    def cat(self, inp):
        parts = inp.split()
        if len(parts) > 1:
            filename = parts[1]
            if filename in self.virt_machine.files:
                print(self.virt_machine.files[filename], end="")
            else:
                print(f"{filename}, no such file.")

    def echo(self,inp):
        parts = inp.split(">",1)
        if len(parts)==2:
            text_part = parts[0].replace("echo","",1).strip() 
            file_part = parts[1].strip()
            
            append_mode = False
            if file_part.startswith(">"):
                append_mode = True
                file_part = file_part[1:].strip()
            
            if append_mode:
                self.virt_machine.files[file_part] = self.virt_machine.files.get(file_part, "") + text_part + "\n"

            else: 
                self.virt_machine.files[file_part] = text_part + "\n"





















    
