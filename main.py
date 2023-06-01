def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Виклик функції {func.__name__} з аргументами {args}, {kwargs}. Результат: {result}")
        return result

    return wrapper


@logger
def add(a, b):
    return a + b

@logger
def multiply(a, b):
    return a * b

print(add(2, 3))
print(multiply(4, 5))