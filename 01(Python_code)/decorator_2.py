
def my_deco(function):
    def wrapper(*args, **kwargs):
        print("I'm here")
        function(*args, **kwargs)

    return wrapper


@my_deco
def say(smth):
    return smth

print(say('hello'))

