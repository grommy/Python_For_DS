
def my_deco(function):
    def wrapper(*args, **kwargs):
        print("I'm here")
        res = function(*args, **kwargs)
        print("there")
        return res

    return wrapper


@my_deco
def say(smth):
    print(smth)
    return smth


a = say('hello')
print(a)



