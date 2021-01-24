'''
Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.
'''
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

freq_words = {}
words = str1.split()
for c in words:
    if c not in freq_words:
        freq_words[c] = 0
    freq_words[c] = freq_words[c] +1

print(freq_words)
# {'I': 2, 'wish': 2, 'with': 2, 'all': 1, 'my': 1, 'heart': 1, 'to': 1, 'fly': 1, 'dragons': 1, 'in': 1, 'a': 1, 'land': 1, 'apart': 1}