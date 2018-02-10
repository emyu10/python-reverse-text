file_path = input("Please enter the file path:\n")
file_name = input("Please enter the file name:\n")

if file_path[len(file_path) - 1] is '/':
    file_path = file_path
else:
    file_path = file_path + '/'


fr = open(file_path + file_name, 'r')
fw = open(file_path + 'reversed.txt', 'w')
line = ''
for c in fr.read():
    if c is '\n':
        reversed_line = line[::-1]
        fw.write(reversed_line + '\n')
        line = ''
    else:
        line += c

fr.close()
fw.close()
