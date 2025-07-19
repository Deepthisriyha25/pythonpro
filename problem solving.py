# numbers = [12, 5, 8, 3, 10]
# print(numbers)
# numbers[2] = 34
# print(numbers)
# numbers.append(23)
# print(numbers)
# numbers.remove(34)
# print(numbers)
# numbers.remove(numbers[4])
# print(numbers)
# print(len(numbers))

# numbers = [12, 5, 8, 3, 10]
# for i in numbers:
#     if 12 in numbers:
#         print("Yes")
#         break
#     else:
#         print("NO")

numbers = [12, 5, 8, 3, 10, 10, 5, 12, 8]
# for i in numbers:
#     print(i)
# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)
# for i in range(len(numbers)-1,-1,-1):
#     print(numbers[i])
# print(numbers[::-1])

# import copy
# a=copy.deepcopy(numbers)
# print(a)

# import copy
# a=copy.copy(numbers)
# print(a)
# numbers.clear()
# print(numbers)
# a=numbers.count(12)
# print(a)
# a=[8,4,5,7]
# print(numbers+a)

# print(numbers*3)
# for i in range(0,len(numbers),2):
#     print(numbers[i])
# a=str(numbers)
# print(a)
# print(max(numbers))
# print(min(numbers))
# sum = 0
# for i in numbers:
#     sum += i
# print(sum)
# for i in numbers:
#     print(i**2)
# print(i)
# l1=[]
# for i in numbers:
#     if i not in l1:
#         l1.append(i)
# print(l1)
# a=[]
# if not a :
#     print("Claer")
# else:
#     print("Elemnts")

# print(numbers[-1])
# a="Deepthi Sriyha"
# print(list(a))

# nested = [[1, 2], [3, 4], [5]]
# empty=[]
# for i in nested:
#     empty+=i
# print(empty)

# a = ["in", "apple", "cow", "pecock", "banana"]
# n = len(a)
# for i in range(n):
#     for j in range(i + 1, n):
#         if len(a[i]) > len(a[j]):
#             a[i], a[j] = a[j], a[i]
# print(a)

# l1=[1,2,34,5,6]
# l2=[1,2,3,4,5,6]
# for i in l1:
#     for j in l2:
#         if i == j:
#             print(i)
# l1=[1,2,34,5,6]
# l2=[1,2,3,4,5,6]
# for i in l1:
#     if i not in l2:
#         print(i)

# l1=[1,2,34,5,6]
# l2=[1,2,3,4,5,6]
# l3=[]
# a=l1+l2
# for i in a:
#     if i not in l3:
#         l3.append(i)
# print(l3)

# a = [1, 2, 3, 4, 5, 6]
# l1=[]
# for i in range(0,len(a),2):
#     l1.append(a[i:i+2])
# print(l1)

# a=[1,77,99,2,3,44,66,33]
# a.sort()
# print(a[-2])

# a = [1, 2, 3, 4, 5]
# r = a[-2:] + a[:-2]
# print(r)
# a = [1, 2, 3, 4, 5]
# r = a[3:] + a[:3]
# print(r)

# l1 = [2, 3, 5, 6, 7, 9, 2, 2, 2]
# val = 2
# for i in range(len(l1)):
#     if l1[i] == val:
#         print(i)
# l1=[1,2,1]
# if l1 == l1[::-1]:
#     print("Palindrome")
# else:
#     print("No")

# n=int(input("Enter:"))
# l1=[]
# for i in range(1,n+1):
#     l1.append(i*i)
# print(l1)

# l1 = [9, 8, 7, 6]
# l2 = ""
# for i in l1:
#     l2 += str(i)
# print(l2)

# l1="srtipms"
# l2=[]
# for i in l1:
#     l2.append(i)
# print(l2)

# l1=["apple", "banana", "cherry"]
# l2=[]
# for i in range(len(l1)):
#     l2 += [l1[i],i]
# print(l2)

# l1 = [(1, 2), (3, 4), (4, 5)]
# l2 = []

# for i in l1:
#     l2.append(i[0] + i[1])

# print(l2)

#FUNCTIONS

# def sumoftwo(a,b):
#     return a+b
# print(sumoftwo(2,5))

# def sq(a):
#     return a*a
# print(sq(2))

# def fact(a):
#     return a*(a-1)
# print(fact(6))

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")

# def maximum(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# print(maximum(10, 25, 15))  

# def reverse(a):
#     rev = 0
#     while a > 0:
#         digit = a % 10
#         rev = rev * 10 + digit
#         a = a// 10
#     return rev
# print(reverse(100237))

# def counts(n):
#     count = 0
#     for digit in str(n):
#         count += 1
#     return count
# print(counts(123456))

# def celsiusfarhen(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# print(celsiusfarhen(270))

# def leap(year):
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         print("leap year")
#     else:
#         print("Not leap yers")
# print(leap(2008))

# a=(2,23,5,66,7,4,5,7,5,7,66,23,2,2)
# print(a)
# print(a[2])
# print(a[:3:])
# if 2 in a:
#     print("Yes")
# else:
#     print("No")
# print(a*3)
# print(len(b))

# print(tuple(b))
# count = 0
# b=a.count(2)
# print(b)

# b=(2,4,6,(4,87,2))
# print(b[3][2])
# s=0
# for i in a:
#     s=i
# print(s)

# merged=()
# for i in range(0,21,2):
#     merged+=i,
# print(merged)

# a={2,8,4,9,2}
# print(a)
# s = {1, 2, 3}
# s.add(4)
# print(s)

# for i in range(1,21):
#     print(i%2==0)

# sum= 0
# for i in range(1,101):
#     sum += i
#     print(sum)

# for i in range(1,10):
#     print(ss)

# for i in range(1,51):
#     if i % 3== 0:
#         print(i)
# fact = 1
# n = 6
# for i in range(1,n):
#     fact *= i
# print(fact)

# fact=1
# n=5
# for i in range(n):
#     fact *= i
# print(fact)

# n=12345
# num= str(n)
# for i in range(len(num)-1,-1,-1):
#     print()

# num = 987
# rev = ""

# for digit in str(num):
#     rev = digit + rev  # Prepend each digit
   
# print(int(rev))

# for i in range(1,11):
#     print(i*i)


# for i in range(1,11):
#     sq=i*i
#     print(sq)
# n=1
# while (n<=10):
#     print(n)
#     n += 1

# num = 987654
# count = 0
# while num != 0:
#     num //= 10   
#     count += 1
# print(count)

# num = 987654
# sum = 0
# while num != 0:
#     num //= 10   
#     sum += num
# print(sum)
# num = 987
# sum_digits = 0
# while num > 0:
#     digit = num % 10         
#     sum_digits += digit   
#     num //= 10               

# print(sum_digits)

# for i in range(1,11):
#     print(2**i)

# n = 9
# i = 1

# while i <= n:
#     if n % i == 0:
#         print(i)
#     i += 1

# for i in range(10,1,-1):
#     print(i)

# num = 593786
# smallest = 9 
# while num > 0:
#     digit = num % 10
#     if digit < smallest:
#         smallest = digit
#     num //= 10

# print(smallest)

# n= 234567891
# small = 6
# while n > 0:
#     digits = n % 10
#     if digits < small:
#         small = digits
#     n //= 10
# print(small)

# k=[10,2,5,7,8,9]
# for x in range(len(k)):
#     if k[x] % 2== 0:
#         k[x] = k[x]+2
# print(k)

# l=['python',32.2,1234,True]
# for i in l:
#     if type(i) ==  str:
#         for x in range(len(i)):
#             if x%2==0:
#                 print(i[x])

# l=[10,20,50,60,90]
# max=l[0]
# min=l[0]
# for i in l:
#     if i>max:
#         max=i
#     if i<min:
#         min=i
# print(max)
# print(min)

# k=('python',)
# print(type(k))

# res=10,13
# print(type(res))

# for x in 10,:
#     print(x)

# o={1,2}
# p={5,7}
# res=o+p
# print(res)

# l1=[5, 2,3,5,4,3,2,1] 
# print(set(l1))

# str="programming"
# set1=set(str)
# print(set1)

# set1={1,2,3}
# set2={3,4,5}
# U=set1 | set2
# print(U)

# a={10,20,30} 
# b={50, 60,10,70}
# c=a.difference(b)
# print(c)

# s="MOM"
# rev = ""
# for i in s:
#     rev = i + rev
# if rev == s:
#     print(f"{s} is a Palindrome")
# else:
#     print(f"{s} is not a Palindrome")


# str1="Python Programming"
# s=str1.lower()
# count = 0
# for i in s:
#     if i in "aeiou":
#         count += 1
# print(count)

# str1 ="   Python Full Stack Developement  "
# s = str1.strip()
# print(s)

# str2="Python is a object oriented programming language"
# s=str2.split()
# print(len)

# str1="python program"
# for i in str1:
#     if str1.count(i) ==  1:
#         print(i)

# str1="PyThOn pRoGraM"
# s=str1.swapcase()
# print(s)

h=[]
n=int(input("Enter studemts: "))
for x in range (n):
    temp={}
    temp['name'] = input("Enter name: ")
    temp['pin'] = input("Enter pin")
    temp['city'] = input("Ente city: ")
    h.append(temp)
print(h)