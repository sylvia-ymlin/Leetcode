# Simulate project directory management
# Input a series of commands
# Output result of the last command

# Command types:
# mkdir: Create a subdirectory, no nesting; do nothing if exists; no output
# cd: cd to subdirectory or cd .. to parent; do nothing if not exists; no output
# pwd: Show absolute path of current directory, root is /, separated by /

# Need data structure to store directory info

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subdirs = {}

    # Input name of directory to create
    def mkdir(self, name):
        # If not exists, add to subdirectories
        if name not in self.subdirs:
            self.subdirs[name] = Directory(name, self)

    # Input name of directory to enter
    def cd(self, name):
        # Return to parent
        if name == "..":
            # If no parent (root), stay
            return self.parent if self.parent else self
        return self.subdirs.get(name, self)

    # Output absolute path of current directory
    def pwd(self):
        path = ''
        current = self
        while current:
            path = current.name + '/' + path
            current = current.parent
        # Root directory is "/"
        return path 

root = Directory("")  # Root directory
current_dir = root

commands = []
# Read input: only EOF stops, skip empty lines
while True:
    try:
        line = input().strip()
        if not line:
            continue
        commands.append(line)
    except EOFError:
        break

result = ""

# Process commands
for command in commands:
    parts = command.split()
    cmd = parts[0]
    if cmd == "mkdir":
        current_dir.mkdir(parts[1])
    elif cmd == "cd":
        current_dir = current_dir.cd(parts[1])
    elif cmd == "pwd":
        result = current_dir.pwd()

print(result)