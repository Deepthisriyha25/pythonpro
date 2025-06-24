x=10
def show():
    x=5
    print(x)
show()
print(x)
#x = 5 is inside the function show(), so it is a local variable, and 5 is printed first.
#x = 10 is a global variable, so it is printed outside the function.
def outer():
    x=10
    def inner():
        print(x)
    inner()
outer()
#x = 10 is inside outer() function, and inner() is also inside outer() function.
# inner() function doesn't have any x value, it uses x value from outer() funtion, so it prints 10.
x="global"
def outer():
    x = "outer"
    def inner():
        x = "inner"
    inner()
    print("outer:",x)
outer()
print("global:",x)
#x = "global" is a global variable.
#inside outer() function, x = "outer" is a local variable to outer().
#inside inner() function , x = "inner" is a local variable to inner() only. It will not change the x value in outer().
#when print("outer:", x) runs, it prints "outer" because x in outer() remains unchanged.
#Outside, print("global:", x) prints "global" from the global variable

def fun1(angle):
    if("rightangel"==90 and "cute"==60):
        print("Right angled")
    else:
        print("Not at all")
fun1(90)







