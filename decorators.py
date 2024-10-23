# Python Decorator Example

def deco(func):
    def wrapper():
        print("+ Process before function call")
        func()
        print("- Process after function call")
    return wrapper

@deco
def hello():
    print("Hello World! from Mawuli")

hello()