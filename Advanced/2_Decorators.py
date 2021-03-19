
def decorator(function, m):
    def wrapper():
        x = function(m)
        print("I'm a Decorators Function")
        print(f"x: {x}")
    return wrapper

@decorator
def call_wrapper(x=1):
    print("I'm a call wrapper function")
    return x


if __name__ == '__main__':
    # decorator(call_wrapper, 10)()
    pass
