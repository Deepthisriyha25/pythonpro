# str="Python"
# rev=""
# for i in range(len(str)-1,-1,-1):
#     rev += str[i]
# print(rev)

# str="MOM"
# rev=""
# for i in range(len(str)-1,-1,-1):
#     rev += str[i]
# if str == rev :
#     print("String is a Palindrome")
# else:
#     print("String is not a Plaindrome")

# str="kskdowenmxaowersndiew"
# v=0
# c=0
# for i in str:
#     if i in "aeiou":
#         v += 1
#     else:
#         c += 1
# print(v)
# print(c)

# str = "pythonpyon"
# uni = ""
# for i in str:
#     if i not in uni:
#         uni += i
# print(uni)

# str="mississippi"
# f={}
# for i in str:
#     if i in f:
#         f[i] += 1
#     else:
#         f[i] = 1
# print(f)
# max_c=0
# freq = ""
# for i,count in f.items():
#     if count > max_c:
#         max_c = count
#         freq = i
# print(freq,":",max_c)

# str="an apple keeps doctor away"
# w=str.split()
# wor=[]
# for i in w:
#     words = i[0].upper() + i[1:].lower()
#     wor.append(words)
# text = " ".join(wor)
# print(text)

# str1="mon"
# str2="dad"
# if sorted(str1) == sorted(str2):
#     print("Anagream")
# else:
#     print("Not an Anagram")

# s="Hello world from Python"
# count=0
# for i in range(len(s)):
#     if s[i] != ' ' and (i==0 or s[i-1] == ' '):
#         count += 1
# print(count)

# str="rgfs ijfjewsi wkejjfi"
# a=str.split()
# b="".join(a)
# print(b)

# s="banana"
# str1=s.replace("a","o")
# print(str1)

# s="banana"
# f={}
# for i in s:
#     if i in f:
#         f[i] += 1
#     else:
#         f[i] = 1
# print(f)
# first = None
# for i in s:
#     if f[i] == 1:
#         first = char
#         break
# if first:
#     print(first)
# else:
#     print("Not found")

# import string
# s="I love programming in Python"
# s = s.translate(str.maketrans('','',string.punctuation))
# words = s.split()
# longest = max(words, key=len)
# print(longest)

# s="I love programming in Python"
# w=s.split()
# r=w[::-1]
# n=" ".join(r)
# print(n)

#********************************************************************************************************#

# n=23
# isprime = True
# for i in range(2,n):
#     if n % i == 0:
#         isprime =False
#         break
# if isprime:
#     print("NUM IS PRIME")
# else:
#     print("Not a prime")

# r=10
# for n in range(2,r):
#     isprime =True
#     for i in range(2,n):
#         if n % i == 0:
#             isprime = False
#             break
# if isprime:
#     print(n)

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))   

# n= 5
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

# 0,1,0+1=2,2+1=3,3+2=5

# n= 5
# a=0
# b=1
# for i in range(n):
#     print(a,end="")
#     a,b = b,a+b

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# n=10
# for i in range(n):
#     print(fib(i), end=" ")

# n=153
# l=len(str(n))
# sum=0
# for i in str(n):
#     sum += int(i) ** l
# if sum == n:
#     print("arm")
# else:
#     print("no arm")

# a=30
# b=70
# maxi = max(a,b)
# while True:
#     if maxi % a == 0 and maxi % b == 0:
#         print(maxi)
#         break
#     maxi += 1

# n=123
# rev = 0
# while n>0:
#     digit = n % 10
#     rev = rev * 10 + digit 
#     n = n // 10
# print(rev)

# n = 1235688954
# c = 0
# while n > 0:
#     n = n // 10
#     c += 1
# print(c)

# n = 12345
# sum= 0
# while n > 0:
#     digit = n % 10
#     sum = sum + digit
#     n = n// 10
# print(sum)

# n = 6
# div = 0
# for i in range(1,n):
#     if n % i == 0:
#         div += i
# if div == n:
#     print("Yes")
# else:
#     print("No")

# l1=[2,11,4,66,8,55,8,44]
# max1=l1[0]
# for i in l1:
#     if max1<i:
#         max1=i
# print(max1)

# l1=[9,4,22,6,88,3,6,22]
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)

# l1=[1,2,3,4,56,7,8]
# n=3
# n=n%len(l1)
# rotated = l1[-n:] + l1[:-n]
# print(rotated)

# a=[1,23,44]
# b=[5,6,7]
# m=sorted(a+b)
# print(m)

# l1=[2,55,3,6,78,9,3]
# target = 6
# pairs = []
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i] + l1[j] == target :
#             pairs.append((l1[i], l1[j]))
# print(pairs)

# l1 =  [-2, -3, 4, -1, -2, 1, 5, -3]
# maxi=sumi=l1[0]
# for i in l1:
#     sumi = max(i,sumi+i)
#     maxi = max(maxi,sumi)
# print(maxi)


# l1=[0,1,0,3,12]
# j=0
# for i in range(len(l1)):
#     if l1[i] !=0 :
#         l1[j]=l1[i]
#         j += 1
# for k in range(j,len(l1)):
#     l1[k] = 0
# print(l1)

# def flatten(lst):
#     flat = []
#     for i in lst:
#         if isinstance(i,list):
#             flat.extend(flatten(i))
#         else:
#             flat.append(i)
#     return flat
# n=[1, [2, 3], [4, [5, 6]], 7]
# print(flatten(n))

# l1=[1,2,3,4,5]
# l2=[2,4,3,2,88]
# for i in l1:
#     if i in l2:
#         print(i)

# l1=[1,2,3,4,5]
# l2=[2,4,3,2,88]
# u=list(set(l1+l2))
# print(union)

#DICT

# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}

# merged = {**d1, **d2}
# print(merged)

# d = {'a': 1, 'b': 2, 'c': 3}
# for i,j in d.items():
#     print(i,j)


# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# uni = {}
# for key, value in d.items():
#     if value not in uni.values():
#         uni[key] = value
# print(uni)

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# d = dict(zip(keys, values))
# print(d)

