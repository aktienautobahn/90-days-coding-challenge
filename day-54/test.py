def my_decorator(some_fun):
    print("before some_function() is called.")
    some_fun()
    print("after some_function() is called.")

@my_decorator
def just_some_fun():
    print("some fun")