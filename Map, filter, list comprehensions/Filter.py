def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))

# Saída [4, 6, 0]
'''
1. Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter.
'''
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = filter(lambda word: 'w' in word, lst_check)
print(list(filter_testing))
# Saída ['watermelon', 'kiwi', 'strawberries']

'''
2. Using filter, filter lst so that it only contains words containing the letter “o”. Assign to variable lst2. Do not hardcode this.
'''
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

lst2 = filter(lambda word: 'o' in word, lst)
print(lst2)

'''
3. Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that only contains the strings from countries that begin with B.
'''

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = filter(lambda c: c[0] == 'B', countries)
print(list(b_countries))
# ['Brazil', 'Botswana', 'Britain', 'Bangladesh', 'Belarus', 'Belgium']