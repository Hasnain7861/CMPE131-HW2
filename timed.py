import time

def timeme(func):
    def inner():
        begin = time.time()
        func()
        end = time.time()
        print("Total time" , end - begin)
    return inner

# @timeme
# def func():
#     time.sleep(2)    

# func()
