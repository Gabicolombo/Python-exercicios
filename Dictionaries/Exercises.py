'''
1. Given the same dictionary, medals, now sort by the medal count. Save the three
countries with the highest medal count to the list, top_three.
'''
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three = []
aux =  sorted(medals.keys(), key=lambda k:medals[k], reverse=True)
for c in range(3):
    top_three.append(aux[c])
print(top_three)
# ['United States', 'China', 'Russia']

'''
2. Create a function called last_four that takes in an ID number and returns the last four digits. 
For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, 
ids, from lowest to highest. Save this sorted 
list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.
'''
def last_four(x):
    string = str(x)
    return string[4:]


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids, key = lambda four: last_four(four))
print(sorted_ids)
# [17570002, 17572342, 17572345, 17573005, 17579000, 17579329]

'''
3. Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. 
Save this sorted list in the variable sorted_id.
'''
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key = lambda four: str(four)[-4:])
print(sorted_id)
# [17570002, 17572342, 17572345, 17573005, 17579000, 17579329]

'''
4. Sort the following list by each element’s second letter a to z. 
Do so by using lambda. Assign the resulting value to the variable lambda_sort.
'''
print('---------- 4º exercise ---------')
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key = lambda k:str(k)[1])
print(lambda_sort)
# ['dance', 'zebra', 'hi', 'how are you', 'apple', 'bye']