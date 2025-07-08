import time
from itertools import count


def decorater_func(func):
    def wrapper():
        print(f"Funksiya chaqirildi: {func.__name__}")
        start=time.time()
        sec=func()
        end=time.time()
        # print(f"{end-start} sekund")
        print("Abdulaziz")

    return wrapper

@decorater_func
def nums():
    count = 0
    for i in range(1, 100_000_000):
        count+=1

nums()