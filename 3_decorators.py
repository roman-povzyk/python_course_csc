# @trace
# def foo(x):
#     return 42
#
#
# def trace(func):
#     def inner(*args, **kwargs):
#         print(func.__name__, args, kwargs)
#         return func(*args, **kwargs)
#     return inner()
#
#
# @trace
# def identity(x):
#     "I do nothing useful"
#     return x
#
# identity(42)


def square(func):
    return lambda x: func(x * x)


def addsome(func):
    return lambda x: func(x + 42)


@addsome
@square
def identity(x):
    return x


print(identity(2))


