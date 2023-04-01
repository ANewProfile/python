import time


def time_func(func):
    def wrapper():
        time1 = time.time()
        func()
        time2 = round(time.time() - time1, 10)
        print(f'Took {time2} seconds.')
    return wrapper
