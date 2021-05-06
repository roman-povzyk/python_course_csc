from collections import deque


class Counter:
    """I count. That is all."""
    def __init__(self, initial=0):
        self.value = initial

    def increment(self):
        self.value += 1

    def get(self):
        return self.value


c = Counter(42)
c.increment()
c.get()


class Noop:
    some_attribute = 42
    _internal_attribute = []


class Noop:
    __very_internal_attribute = []


class MemorizingDict(dict):
    history = deque(maxlen=10)

    def set(self, key, value):
        self.history.append(key)
        self[key] = value

    def get_history(self):
        return self.history


d = MemorizingDict({"foo", 42})
d.set("baz", 100500)
print(d.get_history())

d = MemorizingDict()
d.set("boo", 500100)
print(d.get_history())


class SomeClass:
    def do_something(self):
        print('Doing something.')



class Path:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return "Path({})".format(self.current)

    @property
    def parent(self):
        return Path(dirname(self.current))