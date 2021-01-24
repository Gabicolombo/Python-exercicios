file = open("nomes.txt", "r")
lines = file.readlines()

title = lines[0]
names = title.strip().split(",")
print(names)
for i in lines[1:]:
    aux = i.strip().split(",")
    print('{}{:>5}{:>8}'.format(aux[0], aux[1], aux[2]))