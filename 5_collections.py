date = "October", 5

person = ('George', 'Carlin', 'May', 12, 1937)
name, birthday = person[:2], person[2:]

print(name)
print(birthday)

print((1, 2, 3)[::-1])

print(reversed(range(11)))

from collections import namedtuple
Person = namedtuple('Person', ['name', 'age'])
p = Person('George', age=77)
print(p._fields)
print(p.name, p.age)


