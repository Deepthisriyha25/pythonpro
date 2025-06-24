def add_numbers(a,b):
    return a + b
print(add_numbers(76,43))

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(20))

def greet(name):
    return f"Hello, {name}"
print(greet("Deepthi"))

def area(lenght,width):
    return lenght * width
print(area(23,56))

def check_age(Age):
    if Age >18:
        return True
    else:
        return False
print(check_age(16))
print(check_age(61))

def greet(name="Guest"):
    return f"Hello,{name}"
print(greet("sriyha"))
print(greet())
def power(base,expo=2):
    return base ** expo
print(power(4,3))

def make_sandwich(bread="white", filling="cheese"):
    return f"sandwhich ingrdiants are {bread} and {filling}"
print(make_sandwich())

def sum_all(*num):
    total = 0
    for i in num:
        total += i
    return total
print(sum_all(2,3,5,7))

def describe_person(**details):
    return f"{details['name']} is {details['age']}"
print(describe_person(name="sup",age=21))

def shop(*shoping):
     print(f"Shopping items are {shoping}")
shop("Ac","Cooler","Dresses")
