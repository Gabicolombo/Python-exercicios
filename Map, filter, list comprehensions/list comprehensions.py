print('Funcionando como map')
things = [2, 5, 9]
yourlist = [value * 2 for value in things]
print(yourlist)
# [4, 10,18]

print('Funcionando como filter')
def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))
# [4, 6, 0]

'''
1. The for loop below produces a list of numbers greater than 10. Below the given code, use list comprehension to accomplish the same thing. 
Assign it the the variable lst2. Only one line of code is needed. 
'''

L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(f'Primeira maneira é: {lst}')

lst2 = [x for x in L if x > 10]
print(f'Segunda maneira é: {lst2}')

'''
2. Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the dictionary tester. 
Do this using a list comprehension.
'''

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

inner = tester['info']
compri = [d['name'] for d in inner]
print(compri)

'''
3. Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. 
Using list comprehension, create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater).
'''
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = [x1 for x1, x2 in students if x2 >= 70]
print(passed)

'''
4. Use list comprehension to create a list called lst2 that doubles each element in the list, lst.
'''

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2 = [2*x for x in lst]
print(lst2)

'''
5. Below, we have provided a list of tuples that contain the names of Game of Thrones characters. 
Using list comprehension, create a list of strings called first_names that contains only the first names of everyone in the original list.
'''

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names = [x2 for x1, x2 in list(people)]

print(first_names)
