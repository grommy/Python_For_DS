def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        res = func()
        print("Something is happening after the function is called.")
        return res
    return wrapper


@my_decorator
def say_whee():
    print("Whee!")
    return "answer"


a = say_whee()
print(a)
