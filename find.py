import sys

open_file = open(sys.argv[1], "r", encoding="ISO-8859-1")
file_content = open_file.readlines()


buffer = {}
for row in file_content:
    if row not in buffer:
        buffer[row] = 1
    else:
        buffer[row] += 1


for i in buffer:
    if buffer[i] > 1:
        print(f"Occurrences: {buffer[i]}")
        print(i)



