'''
Create the dictionary characters that shows each character from the string sally and its frequency.
Then, find the most frequent letter based on the dictionary.
Assign this letter to the variable best_char.
'''
sally = "sally sells sea shells by the sea shore"

characters = {}
for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] = characters[c] + 1

print(characters)
array = list(characters.keys())
best_char = array[0]
for i in characters.keys():
    if characters[best_char] < characters[i]:
        best_char = i

print(f'best_char: {best_char}')
# {'s': 8, 'a': 3, 'l': 6, 'y': 2, ' ': 7, 'e': 6, 'h': 3, 'b': 1, 't': 1, 'o': 1, 'r': 1}
# best_char: s