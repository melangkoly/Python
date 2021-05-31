def calc(a, b, func):
    if (callable(func)):
        return func(a, b)

print(calc(3, 4, lambda x, y: x * y))