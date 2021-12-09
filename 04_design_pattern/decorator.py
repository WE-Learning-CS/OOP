def my_decorator(func):
    def runs_func():
        print("hi")
        func()
    return runs_func

@my_decorator
def my_func():
    print("my_func1 run!")