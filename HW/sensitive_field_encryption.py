# Given a command string consisting of multiple command words
# Contains letters, numbers, underscores, even number of double quotes
# Double quotes can identify command words containing '_' or empty command words
# Command words are connected by single or multiple underscores
# Encrypt sensitive field at specified index, replace with ******, remove extra underscores around command words

# Output two lines
# First line, command string index? No, actually "First line determines sensitive field index k?"
# Original text: "First line input index k". "Output command string after processing".
# Wait, translation says "Output two lines...". This might be interpreting problem statement asking for output format?
# Sample output shows one line result.
# Actually, the file reads index then command_str.
# It outputs processed string or ERROR.
# The code prints `_`.join(commands).

# Output processed command string, or "ERROR" if index invalid

index = int(input().strip())
command_str = input().strip()

# Problem is using split('_') directly would split underscores inside quotes
# Split by '"' first, then process parts
parts = command_str.split('"')
# Parts with quotes -> odd indices (if split by quote)
# "a"_"b" -> ['', 'a', '_', 'b', ''] if split by quote?
# a_"b" -> ['a_', 'b', '']
commands = []
for i in range(len(parts)):
    if i % 2 == 0:
        sub_parts = parts[i].split('_')
        for sp in sub_parts:
            if sp != '':
                commands.append(sp)
    else:
        commands.append('"' + parts[i] + '"')

if index < 0 or index >= len(commands):
    print("ERROR")
else:
    commands[index] = '******'
    print('_'.join(commands))