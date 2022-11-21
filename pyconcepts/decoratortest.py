from functools import wraps

def decfunc(func):
    print("entering the decorator function")
    @wraps(func) # this allows the system to run the fn() as fn() itself. without making it look like wrapper()
    def wrapper(*args,**kwargs):
        """docstring for wrapper"""
        print("entering the wrapper function")
        wrapper.count += 1
        print(wrapper.count)
        # print("the function is going to run now!")
        func(*args,**kwargs)
        # print("The function has finished running!")  

    wrapper.count = 0  # this is defining variables for the wrapper function
    # whenever the fn() is called, it will come to this decorator function and to this place. and proceed. NO! The decorator runs only at the time the decorated function is defined
    return wrapper  # this is actually where the wrapper gets called

@decfunc
def fn():
    """docstring for fn"""
    print("entering the usual function")
    if fn.count % 2 == 0: print("Function ran only on Even")

if __name__ == '__main__':
    fn() # when I run this multiple times, wrapper.count doesn't get altered. only the wrapper() function gets modified.
    fn()
    print(fn.__name__)
    print(fn.__doc__)

"""
FLow:

Important note: The decorator runs only at the time the decorated function is defined, in order to modify the function definition. The function returned by the decorator (wrapper) is what gets executed each time the decorated function is called.

when fn() is called:
it goes to the decfunction() NO! The decorator runs only at the time the decorated function is defined
defines wrapper.count as 0
calls the wrapper function
increase the count to 1 
now runs the fn() with modified args and kwargs
cool stuff right?
"""



"""
Struncture:

def decfunction(func):
    def wrapping_function(*args, **kwargs):
        modifiers go here
        func()
        more modifiers
    
    declaration of variables for the wrapper function
    return wrapper


def usual_function():
    pass
"""

