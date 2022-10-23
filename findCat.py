from cat import Cat

c1 = Cat('Sam', 'male', 2)
cats = [c1]
print('Cat: ')

for i in cats:
    print(i())
