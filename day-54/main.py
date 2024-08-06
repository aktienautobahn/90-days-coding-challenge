import time


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        runtime = end_time-start_time
        print(f'{function.__name__} runtime is {runtime}')
    return wrapper_function


# def speed_calc_decorator_2(function):
#         start_time = time.time()
#         function()
#         end_time = time.time()
#         runtime = end_time-start_time
#         print(f'{function.__name__} runtime is {runtime}')



    
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()