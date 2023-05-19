def farfor(func):
    def wrapper(n):
        print(n+10)
    return wrapper
@farfor
def number(n):
    return n
number(50)
