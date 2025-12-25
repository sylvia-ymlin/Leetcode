# 模拟项目目录管理
# 输入一系列命令
# 输出最后一条命令的运行结果

# 命令类型
# mkdir 创建一个子目录，不能嵌套；已存在的目录不处理；无输出
# cd: 包括 cd 进入子目录 和 cd .. 返回上级目录；不存在的目录不处理；无输出
# pwd：显示当前目录的绝对路径，根目录为 /，各级目录间以 / 分隔

# 需要设计数据结构，保存所有目录信息

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subdirs = {}

    # 输入要创建的目录名
    def mkdir(self, name):
        # 目录不存在，添加到子目录中
        if name not in self.subdirs:
            self.subdirs[name] = Directory(name, self)

    # 输入要进入的目录名
    def cd(self, name):
        # 返回上级目录，即返回 parent
        if name == "..":
            # 如果没有上级目录，返回自己
            return self.parent if self.parent else self
        return self.subdirs.get(name, self)

    # 输出当前目录的绝对路径
    def pwd(self):
        path = ''
        current = self
        while current:
            path = current.name + '/' + path
            current = current.parent
        # 根目录“/”
        return path 

root = Directory("")  # 根目录
current_dir = root

commands = []
# 读取输入：只认 EOF，跳过空行
while True:
    try:
        line = input().strip()
        if not line:
            continue
        commands.append(line)
    except EOFError:
        break

result = ""

# 处理命令
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