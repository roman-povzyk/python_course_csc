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

list = [0] * 3
print(list)

xs = [1, 2, 3]
xs.append(42)
print(xs)

print(xs.index(42))
xs.insert(0, 4)
print(xs)

xs = []
xs += 'abcd'
print(xs)

xs, ys, zs = {1, 2}, {2, 3}, {3, 4}

a = set.union(xs, ys, zs)
b = set.intersection(xs, ys, zs)
c = set.difference(xs, ys, zs)

print(a)
print(b)
print(c)









