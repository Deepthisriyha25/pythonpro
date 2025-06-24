#Grade Evalautor
def Evaluator(score):
    if(score > 90):
        print("Congrats Your Awareded with A Grade")
    elif(score>=80 and score<89):
        print("Congrats Your Awareded with B Grade")
    elif(score>=70 and score<79):
        print("Congrats Your Awareded with C Grade")
    elif(score>=60 and score<69):
        print("Congrats Your Awareded with D Grade")
    else:
        print("You Failed in exam Better Luck Next Time")
score=int(input("Enter Your Score"))
Evaluator(score)
#Even or Odd
def oddeven(num):
    if(num%2==0):
        print("Even Number")
    else:
        print("Odd Number")
num=int(input("Enter Number"))
oddeven(num)
#Temperature Converter
def temperature(t):
    if(t<15):
        print("Cold")
    elif(t>15 and t<=25):
        print("Moderate")
    else:
        print("Hot")
t=int(input("Enter temperature in celcius: "))
temperature(t)
#SIDES OF TRIANGLE
def triangle(a, b, c):
        if(a == b == c):
            print("Equilateral Triangle")
        elif(a == b or b == c or a == c):
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
a= int(input("Enter side1: "))
b=int(input("Enter SIde 2: "))
c=int(input("Enter Side3 : "))
triangle(a,b,c)
#LEAP YEAR
def leapyear(year):
    if(year % 4==0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
year=int(input("Enter a year"))
leapyear(year)
#AGE
def checkage(age):
    if (age<=12):
        print("Child")
    elif(age>=13 and age<=19):
        print("Teenager")
    elif(age>=20 and age<=60):
        print("Adult")
    else:
        print("Senior")
age=int(input("Enter Age"))
checkage(age)
#BASIC CALCULATOR
def calculator(a, b, operator):
    if operator == '+':
        print(a+b)
    elif operator == '-':
       print(a-b)
    elif operator == '*':
        print(a*b)
    elif operator == '/':
        print(a/b)
    else:
        print("It is not an operator")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
operator = input("Enter operator ")
calculator(a, b, operator)
#login
def login(email,password):
    if(email=="sriyha25@gmail.com" and password=="Deepthisriyha@25"):
        print("Acess granted")
    else:
        print("Acess Denied")
email=input("Enter your EMail: ")
password=input("Enter your password: ")
login(email,password)
#BMI CALCUlator
def bmicalculator(height,weight):
    bmicheck = (weight/height*height)
    if bmicheck < 18.5:
        print("Underweight")
    elif bmicheck>=18.5 and bmicheck <24.9:
        print("Normal Weight")
    elif bmicheck >=25 and bmicheck <=29.9 :
        print("Overweight")
    else:
        print("Obese weight")
height=int(input("Enter Height in meters: "))
weight=int(input("Enter Weight in kg "))
bmicalculator(height,weight)


