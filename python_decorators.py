# functions are objects

def say_hello(name="hamza"):
    """ function for greeting """
    print("hello {}".format(name))


#say_hello()

#print(say_hello,say_hello.__doc__,say_hello.__defaults__)


def outer():
    # Create a dummy variable
    my_var = 'Python'  # nonlocal variable to `inner`

    def inner():
        # Try to change the value of the dummy with nonlocal
        nonlocal my_var  # now can access the value of nonlocal vars
        my_var = 'Data Science'
        print(my_var)

    # Call the inner function which tries to modify `my_var`
    inner()
    # Check if successful
    print(my_var)


#outer()


# Closures in python

def foo():
    x = 42

    def bar():
        print(x,y)

    return bar


var=foo()
#print(var.__closure__[0].cell_contents)


# another example more trickier
var = 'dummy'


def parent(arg):
    def child():
        print(arg)

    return child


# Call it as is
my_func = parent(var)
#my_func()

# Call after changing var
var = 'new_dummy'
#my_func()

#print(my_func.__closure__[0].cell_contents)


# Decorators

""" Decorators are functions that modify another function.
 They can change the function’s inputs, 
 its output or even its behavior."""

# start with the simple decorator

def add_one(func):

    def wrapper(a):
        return func(a+1)
    return wrapper

def square(a):
    return a**2

square=add_one(square)
#print(square.__closure__[0].cell_contents)


# Real_wold examples with decorators
# create a timer decorator
import time


def timer(func):
    """
    A decorator to calculate how long a function runs.

    Parameters
    ----------
    func: callable
      The function being decorated.

    Returns
    -------
    func: callable
      The decorated function.
    """

    def wrapper(*args, **kwargs):
        # Start the timer
        start = time.time()
        # Call the `func`
        result = func(*args, **kwargs)
        # End the timer
        end = time.time()

        print(f"{func.__name__} took {round(end - start, 4)} "
              "seconds to run!")
        return result

    return wrapper


@timer
def sleep(n):
    """
    Sleep for n seconds

    Parameters
    ----------
    n: int or float
      The number of seconds to wait
    """
    time.sleep(n)


#sleep(5)


# The caching decorator.
#Caching decorators are great for computation-heavy functions,
# which you may call with the same arguments many times.

def cache(func):
    """
    A decorator to cache/memoize func's restults

    Parameters
    ----------
    func: callable
      The function being decorated

    Returns
      func: callable
        The decorated function
    """
    # Create a dictionary to store results
    cache = {}  # this will be stored in closure because it is nonlocal

    def wrapper(*args, **kwargs):
        # Unpack args and kwargs into a tuple to be used as dict keys
        keys = (tuple(args) + tuple(kwargs.keys()))
        # If not seen before
        if keys not in cache:
            # Store them in cache
            cache[keys] = func(*args, **kwargs)
        # Else return the recorded result
        return cache[keys]

    return wrapper


# let's test our function
@timer
@cache
def sleep(n):
    """
    Sleep for n seconds

    Parameters
    ----------
    n: int or float
      The number of seconds to wait
    """
    time.sleep(n)

#sleep(5)  # this one takes 5 seconds
#sleep(5)   # this one takes 0 seconds (very powerful)

# decorators that takes arguments

#Consider this decorator, which checks if the function’s result is of type str

def is_str(func):
    """
    decorator to check if func's result
    is a string
    """
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        return type(result)==str

    return wrapper

@is_str
def foo(arg):
  return arg

#print(foo(4),foo('python'))

#wouldn’t it be cool if we had a way
# to check the function’s return type for any data type?
def is_type(dtype):
    """
    Defines a decorator and returns it.
    """
    def decorator(func):
        """
        A decorator to check if func's result is of type `dtype`
        """
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return type(result) == dtype
        return wrapper
    return decorator

# test the decorator

@is_type(dict)
def foo(arg):
    return arg

print(foo({1: 'Python'}))

@is_type(int)
def square(num):
    return num ** 2

print(square(5))

#Preserving the Decorated Function’s Metadata
