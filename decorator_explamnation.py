def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


def calculate(cal_func, n1, n2):
    return cal_func(n1, n2)


# print(calculate(multiply, 9, 18))
# print(calculate(divide, 9, 18))
# print(calculate(subtract, 9, 18))
# print(calculate(add, 9, 18))


# def outer_function():
#     print("I am outer")

#     def nested_function():
#         print("I am inner")
#     nested_function()

def delay_decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function

@delay_decorator_function
def say_hello():
    print("Hello")

def say_bye():
    print("Bye")


