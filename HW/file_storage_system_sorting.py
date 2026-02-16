# Sort files in the same folder by time
# Folders have hierarchy
# Fundamental problem is to read all files, get modification time of each file, then sort
# No duplicate times or filenames

# Problem requires sorting files under specified folder, so given file structure may contain other folders not needing sorting
# When reading target folder, get its hierarchy level, then read all files under this level -> until encountering folder of same level or finish reading

n = int(input())
file_list = []
# Target folder name
goal = input().strip()
start = False

for _ in range(n):
    # Need to judge if current is folder or file
    line = input().strip()
    # Last part is -1 means folder, otherwise file
    if line.endswith(' -1'):
        # Read folder name
        folder_name = line[:-3].strip().lstrip('-')
        if folder_name == goal:
            # Determine hierarchy level of current folder
            goal_level = (len(line) - len(line.lstrip('-'))) // 4
            start = True
        elif start:
            # Determine hierarchy level of current folder
            curr_level = (len(line) - len(line.lstrip('-'))) // 4
            if curr_level <= goal_level:
                # Reached same level folder, stop processing subsequent, but continue reading input
                start = False
    elif start: # Is file, and entered target folder
    # Is file, get filename and modification time, remove all leading "-"
        file_info = line.lstrip('-').split()
        file_name = file_info[0]
        mod_time = int(file_info[1])
        file_list.append((file_name, mod_time))

if not file_list:
    print("No file")
    exit()

# Sort by modification time
file_list.sort(key=lambda x: x[1])
# Recombine filename and modification time
for file_name, mod_time in file_list:
    print(f"{file_name} {mod_time}")

# 5
# Documents
# Documents -1
# ----file1.txt 1600000000
# ----file2.txt 1600000100
# ----SubFolder1 -1
# --------file3.txt 1600002000

# 5
# Video
# Video -1
# ----SubFolderO -1
# ----SubFolder1 -1
# ----SubFolder3 -1
# —-------SubFolder4 -1