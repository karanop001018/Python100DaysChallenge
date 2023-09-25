def greet(fx):
    def mfx(): # mfx(): means modified fx
        print('Good Morning')
        fx()
        print('Thanks for using this function')
    return mfx

@greet
def hello():
    print('Hello World')
hello()

print('\n')

def hello():
    print('Hello World')
greet(hello)()

# ----------------------------------------------------------------------

def greet(fx):
    def mfx(*args, **kwargs):
        # *args: method to take all arguments as a tuple
        # **kwargs: method to take arguments as a dictionary
        print('Good Morning')
        fx(*args, **kwargs)
        print('Thanks for using this function')
    return mfx


@greet
def add(a,b):
    print(a+b)
add(36,63)

print('\n')

def add(a,b):
    print(a+b)
greet(add)(96,112)
