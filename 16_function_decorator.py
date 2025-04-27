def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")  # First, print this
        return func(*args, **kwargs)  # Then, run the original function
    return wrapper

@log_function_call
def say_hello():
    print('hello how are you')

say_hello()  # This will first print "Function is being called", then "hello how are you"
