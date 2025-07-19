"""num = 8947125
sum = 0
while num:
 sum += num % 10
 num //= 10
 if(num>6):
   continue
print(sum)"""
"""val = "python"
print(val[::2])"""
"""for i in range(1,13,2):
    if(i==10):
        break
print(i + (i%2))
"""
"""x = "Hello"
y = x
x = x.lower()
print(x, y)
"""
"""n=int(input("Enter a number: "))
sum = 0
while n >0:
    sum += n % 10
    n //= 10
print(sum)
"""
# n = int(input("Enter a number: "))
# count = 0
# str1 = str(n)
# for i in str1:
#     if int(i)%2 == 0:
#         count += 1 
# print(count)

# n1= int(input("Enter a number: "))
# org=n1
# fact = 1
# sum1=0
# while n1>0:
#     last_digit= n1 % 10
#     for i in range(1,last_digit+1):
#         fact *= i
#     sum1 += fact
#     n1 = n1 // 10
# if org == sum1:
#     print("Strong Number")
# else:
#     print("Not a strong number")

"""str1="python"
dict1={}
for i in range(100,100 + len(str1)):
    dict1[i] = str1[i - 100]
print(dict1)"""

# str = "python"
# dict = {}
# i = 0  
# j = 0  
# while j < len(str):
#     dict[i+100] = str[j]
#     i += 1
#     j += 1
# print(dict)

# x=["a","h","a","k","j","a","b"]
# dict1={}
# for items in x:
#     if items in dict1:
#         dict1[items] += 1
#     else:
#         dict1[items] = 1
# print(dict1)

# str1="banana"
# dict2={}
# for i in str1:
#     if i in dict2:
#         dict2[i] += 1
#     else:
#         dict2[i] = 1
# print(dict2)

# Input = ["cat", "dog", "cat", "mouse"]
# dict3={}
# for i in Input:
#     if i in dict3:
#         dict3[i] += 1
#     else:
#         dict3[i] = 1
# print(dict3)
    
# In1 = {"a": 1, "b": 2}
# op1={}
# for key,value in In1.items():
#     op1[value] = key
# print(op1) 

# data = {"x": 10, "y": 20}
# for key, value in data.items():
#     print(f"Key: {key}, Value: {value}")

# my_dict = {"name": "Deepthi", "age": 22}
# search = "name"

# for keys in my_dict:
#     if search == keys:
#         print("yes")
#         break
# else:
#     print("No")

"""dict1 = {"a": 1}
dict2 = {"b": 2}
dict1.update(dict2)
print(dict1)"""
# n = int(input("Enter number "))
# sq={}
# for i in range(1,n+1):
#     sq[i] = i*i
# print(sq)
# keys = ["name", "age"]
# values = ["Swathi", 22]
# op={}
# for i in range(len(values)):
#     op[keys[i]] = values[i]
# print(op)

# dict1={"emp1":25000, "emp2":29500,"emp3":31500}
# total=0
# for i in dict1:
#     total += dict1[i]
# print(total)

# dict1={"stu1":"kiran","stu2":"lakshmi","stu3":"naveen","stu4":"naresh"}
# search="lakshmi"
# found= False
# for i in dict1:
#     if dict[i] == search:
#         found=True
#         break
# if found:
#     print("True")
# else:
#     print("not exist")

"""dict1={"a":10,"b":15,"c":25,"d":15}
dict2={"a":15,"c":15,"x":15,"y":10}
merged={}
for x in dict1:
    merged[x] = dict1[x]
for x in dict2:
    if x in merged:
        merged[x] += dict2[x]
    else:
        merged[x] = dict2[x]
print(merged)
"""
# dict1={"x":2,"y":4,"z":6,"a":10}
# dict2={}
# for i in dict1:
#     value=dict1[i]
#     dict2[value]=i
# print(dict2)

# n=25
# flage=False
# for i in range(1,n+1):
#     if(i*i == n):
#         flage=True
#         break
# if flage:
#     print("Perfect")
# else:
#     print("Not")

# n=6
# sum=0
# for x in range(1,n):
#     if(n%x==0):
#         sum += x
# print(sum)
# if sum == n:
#     print("Perfect number")
# else:
#     print("NOt")

# x, y, z, *res, la1, la2, la3 = [
#     "apple", "banana",
#     "grapes", "lemon",
#     "pineapple", "guava",
#     "mango", "kiwi",
#     "orange", "strawberry", "blueberry"
# ]

# print( x)
# print( y)
# print(z)
# print(res)
# print(la1)
# print(la2)
# print(la3)

# n=int(input("Enter number: "))
# sq=1
# for i in range(1,n+1):
#     sq = i*i
#     print(sq)

# n= int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     if n%i == 0:
#         sum += i
# if sum == n:
#     print(n)

# count = 0
# num = 2

# while count < 6:
#     sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum += i
#     if sum == num:
#         print(num)
#         count += 1
#     num += 1


# n = int(input("Enter a number: "))
# x = n + 1
# i = 1
# found = False
# while i * i <= x:
#     if i * i == x:
#         found = True
#         break
#     i += 1
# if found:
#     print(f"{n} is a Sunny Number")
# else:
#     print(f"{n} is NOT a Sunny Number")

# s="welcome to 10000Coders welcome to python full stack"
# a=s.split(" ")
# print(a)
# print(len(a))
# unique=set(a)
# print(len(unique))
# dict1={}
# for i in a:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
# print(dict1)

# l1=[1,"deepthi","sriyha"]
# l2=[2,"india"]
# l3=[3,4,5]
# op=[*l1,*l2,*l3]
# print(op)

# dict1={"name":"deepthi",}
# dict2={"age":35}
# op1={**dict1,**dict2}
# print(op1)

# op=[x * x for x in range(1,5) ]
# print(op)

# a=[1,4,6,8,93]
# op1=[i*2 for i in a ]
# print(op1)

# b=["deepthi","sriyha","milky","python","html","css"]
# op2=[len(i) for i in b]
# print(op2)

# str1=["html","css","python","java"]
# op1=[i[::-1] for i in str1]
# print(op1)

#factorial program suing list comprehension and function

# def factorial(num):
#     fact=1
#     for x in range(1,num+1):
#         fact = fact * x
#     return fact
# def perfect_num(num):
#     sum = 0
#     for i in range(1,num):
#         if (num%i == 0):
#             sum += i
#     return sum == num
# op={i:factorial(i) for i in range(1,7)}
# print(op)

# str9="moonsun"
# op3=[a[::-1] for a in str9]
# print(op3)

# n=int(input("Enter: "))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum += i
# if sum == n:
#     print("Perfect num")
# else:
#     print("Not a perfect num")

# def primeno(num):
#     if num==1:
#         print("Neither prime nor composite")
#     elif num<0:
#         print("Only postove numbers allowed")
#     else:
#         is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         return True
#     else:
#         return False

# def prime_range(s,e):
#     for x in range(s,e+1):
#         if(primeno(x)):
#             print(x)
# prime_range(10,30)

# ip=["welcome","some","hello","python"]
# for x in ip:
#     rev=""
#     for y in range(len(x)-1,-1,-1):
#        rev+=x[y]
#     print(rev)

# x=["ab","cd"]
# for i in x[0]:
#     for j in x[1]:
#         print(i+j)

def is_sunny(n):
    next_num = n + 1
    i = 1
    while i * i <= next_num:
        if i * i == next_num:
            return True
        i += 1
    return False


num = 8
print(is_sunny(num))

def is_neon(n):
    square = n * n
    digit_sum = 0
    while square > 0:
        digit_sum += square % 10
        square //= 10
    return digit_sum == n


num = 9
print( is_neon(num))

