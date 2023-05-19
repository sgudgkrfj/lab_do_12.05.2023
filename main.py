import time

def gggggg(func):
    def wrapper(n):
        start_time=time.time()
        for i in range(n):
            print("ddd")
        end_time=time.time()
        tiime=end_time-start_time
        print(tiime)
    return wrapper
@gggggg
def ddd(n):
    n=n
    return n
ddd(520)