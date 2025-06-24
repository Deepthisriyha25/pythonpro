#Arbitatry,Keyword,lamda
def example(*args):
    print(args)
example(1,2,6,7,9)
def sumofall(*add):
    print(sum(add))
sumofall(23,45,67,98,23,88)
def sample(favfood,favplace,age,name):
    print(favfood,favplace,age,name)
sample("Dosa","Manali",34,"Pant")
def same(name,age,location="Nellore"):
    print(name,age,location)
same("shreyas",35,"Punjab")#If we give a value for default argument it will override presnt value
def employee(**employee_info):
    print(employee_info)
employee(name="Priya",age=26,location="Hyderabad",gender="Female")
def courses(**course_info):
    print(course_info)
courses(name="sriyha",age=22,course="Python Full Stack",institute="10000 Coders")
anoy1= lambda x: 23**x
anoy2=lambda y: 12//y 
print(anoy1(2))
print(anoy2(6))
#SCOPES
x=45 #GLOBAL SCOPE
def func1():
    a=67     #ENCLOSED SCOPE
    def func2():
        b =22#LOCAL SCOPE 
        print(a+b)
    func2()
func1()
name = "Ram" #GLOBAL SCOPE
def greet():
    greeting = "Hello"  # ENCLOSED SCOPE
    def display():
        Message = "Good Morning"  # LOCAL SCOPE
        print(greeting, name + Message) 
    display()
greet()
pi = 3.14
def radius():
    radius = 56
    def areasemi():
        area = (pi*radius**2)/2
        units = "cm^2"
        print(f"Area : {area} {units}")
    areasemi()
radius()
p = 150000
def time():
    t = 45
    def rate():
        r = 2
        def simpleinterest():
            simpleinterest= (p*t*r)/100
            units="Rs"
            print(f"Simple Interst:{simpleinterest}{units}")
        simpleinterest()
    rate()
time()




