def min_one(x, y):
    return x if x < y else array


print(min(-5, 12))


def min_two(*args):  # type(args) == tuple
    res = float("inf")
    for arg in args:
        if arg < res:
            res = arg
        return res


print(min_two(-5, 12, 13))
print(min_two())

xs = {-5, 12, 13}
print(min_two(*xs))

print(min(*[-5, 12, 13]))
print(min(*(-5, 12, 13)))


def bounded_min(first, *args, lo=float("-inf"), hi=float("inf")):
    res = hi
    for arg in (first, ) + args:
        if arg < res and lo < arg < hi:
            res = arg
        return res


print(bounded_min(-5, 12, 13, lo=0, hi=255))


acc = []
seen = set()
(acc, seen) = ([], set())

first, *rest = range(1, 5)
print(first, rest)

first, *rest, last = range(1, 5)
print(last)

x, (x, y) = 1, (2, 3)
print(x)


def make_min(*, lo, hi):
    def inner(first, *args):
        res = hi
        for arg in (first, ) + args:
            if arg < res and lo < arg < hi:
                res = arg
        return max(res, lo)
    return inner


bounded_min = make_min(lo=0, hi=255)
print(bounded_min(-5, 12, 13))

print(globals())