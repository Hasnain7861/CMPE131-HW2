import time

def timestamp(hi):
    def inner():
        localTime = time.ctime()
        print(localTime)
        hi()
    return inner

