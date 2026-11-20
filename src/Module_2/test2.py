def decorator(func):
    def combine():
        print("beginning of testing decorator")
        func()
        print("after of testing decoratotr")
    return combine

@decorator
def mid():
    print("Inside mid function")

mid()

@decorator
def mid_2():
    print("Inside mid_2 function")

mid_2()