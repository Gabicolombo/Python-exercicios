'''
1. Below, we have provided a list of strings called abbrevs. Use map to produce a new list called
abbrevs_upper that contains all the same strings in upper case.
'''
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper = list(map(lambda st: st.upper(), abbrevs))
print(abbrevs_upper)

# Saída: ['USA', 'ESP', 'CHN', 'JPN', 'MEX', 'CAN', 'RUS', 'RSA', 'JAM']


'''
2. Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst
'''

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

def double(list):
    return 2*list

greeting_doubled = list(map(double, lst))
print(greeting_doubled)


# Saída: [['hi', 'bye', 'hi', 'bye'], 'hellohello', 'goodbyegoodbye', [9, 2, 9, 2], 8]


'''
3. Write code to assign to the variable map_testing all the elements in lst_check while adding the string 
“Fruit: ” to the beginning of each element using mapping.
'''

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = map(lambda x: 'Fruit: '+x, lst_check)
print(list(map_testing))
# Saída: ['Fruit: plums', 'Fruit: watermelon', 'Fruit: kiwi', 'Fruit: strawberries', 'Fruit: blueberries', 'Fruit: peaches', 'Fruit: apples', 'Fruit: mangos', 'Fruit: papaya']