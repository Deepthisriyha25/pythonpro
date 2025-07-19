"""nums=471289936
con=str(nums)
max=con[0]
for i in con:
    if(i>max):
        max=i
print(max)"""

"""str1="some"
dict1={}
for i in range(0,len(str1),1):
    dict1[i]=str1[i]
print(dict1)"""

"""num = 145
temp = num
sum = 0
while num > 0:
    digit = num % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum += fact
    num = num // 10
if sum == temp:
    print("Strong Number")
else:
    print("Not a Strong Number")"""

"""a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator: ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")

"""

"""def calic(num1,num2,sym):
    if sym=="+":
        print(f"addition of {num1} + {num2} is {num1+num2}")
    elif sym=="-":
        print(f"subraction of {num1} - {num2} is {num1-num2}")
    elif sym=="*":
        print(f"multiplication of {num1} * {num2} is {num1*num2}")
    elif sym=="/":
        print(f"division of {num1} / {num2} is {num1/num2}")
calic(2,34,"+")
"""

"""rows = 5
for i in range(1, rows + 1):
    print("* " * i)"""

# l1=[1,2,3,[4,5,6],[3,4,6,10]] 
# l2=[]
# for i in l1:
#     l2.append(i)
# print(l2)

# lst = ["apple", "banana", "orange", "banana", "apple", "grape", "orange"]
# d1={}

# for i in lst:
#     if i in d1:
#         d1[i] += 1
#     else:
#         d1[i] = 1
# print(d1)
# #
# str1="Banana"
# d1={}
# for i in str1:
#     if i in d1:
#         d1[i] += 1
#     else:
#         d1[i] = 1
# print(d1)

# str = "Banana"
# l1=[]
# for i in str:
#     l1 += i
# print(l1)  





