def f():
    yield 10
    return 20

g = f()
print(next(g))
