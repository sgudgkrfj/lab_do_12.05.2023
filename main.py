def cache(func):
    memo = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in memo:
            return memo[key]
        else:
            result = func(*args, **kwargs)
            memo[key] = result
            return result

    return wrapper