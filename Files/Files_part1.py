file = open("Olympics.txt", "r")
contents = file.read()
# contest reads all file
print(f'Contests: {contents}')
print(f'How many characters? {len(contents)}')

lines = file.readline()
print(f'How many lines? {len(lines)}')
file.close()