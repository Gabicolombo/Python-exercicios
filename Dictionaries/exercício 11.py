'''
Create a dictionary called d that keeps track of all the characters in the string placement
and notes how many times each character was seen. Then, find the key with the lowest value in
this dictionary and assign that key to min_value.
'''
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = {}
for key in placement:
    if key not in d:
        d[key] = 0
    d[key] = d[key] + 1
min_value = d[key]
for k in d.keys():
    if min_value > d[k]:
        min_value = k

print(min_value)


