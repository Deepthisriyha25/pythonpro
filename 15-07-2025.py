# l=[10,15,6,9,8]
# tem={}
# for n in l:
#     res = [x for x in range(1,n) if n%x==0]
#     tem[n] =res
# print(tem)
# res=(x for x in range(1,10) if x%2==0)
# print(*res)
# a=[1,2,3]
# b=[10,20,30]
# res=tuple((a[x]+b[x]) for x in range(len(a)))
# print(res)
# res1=tuple((x*2) for x in range(1,11) )
# print(res1)
# r=[1,2,3,4,5,6] 
# res={x:('even' if x%2 == 0 else 'odd') for x in r}
# print(res)
# k='python'
# res={x:ord(x) for x in k }
# print(res)

# res={x:('even' if x%2 == 0 else 'odd') for x in range(1,11)}
# print(res)

# a=0
# while a<10:
#     print(a)
#     a+=1

# a=-10
# while a<=-1:
#     print(a)
#     a+=1

# m="python"
# res=''
# for x in m:
#     res=x + res
# print(res)    

# m=123
# res =0
# while m>0:
#     digit=m%10
#     res=res*10+digit
#     m//=10
# print(res)

# k=45632
# primesum=0
# while k>0:
#     data = k%10
#     k//=10
# is_prime = True
#     for x in range(2,data):
#         if data%x==0:
#             is_prime=False
#             break
#     if is_prime:
#         primesum += data
# print(primesum)

# a=1
# while a<6:
#     b=1
#     while b<=10:
#         print(a,'x',b,'=',a*b)
#         b+=1
#     print()
#     a+=1


# n=6
# T=0
# for x in range(1,n):
#     if n%x==0:
#         T+=x
# if n==T:
#     print("Perfect number")
# else:
#     print("not perfect number")


# R=0
# m=153
# res=len(str(m))
# for i in str(m):
#     i = str(i)
#     data=i**res
#     R+=data
# print(R)

# n=14
# if n<=1:
#     print("Nearest prime is 2")
# else:
#     is_prime = True
#     i = 2
#     while i < n:
#         if n%i==0:
#             is_prime = False
#             break
#         i += 1
#     if is_prime:
#         print("Nearest prime number is:", n)
#     else:
#         a = n - 1
#         b = n + 1
#         while True:
#             is_a_prime = True
#             j = 2
#             while j < a:
#                 if a % j == 0:
#                     is_a_prime = False
#                     break
#                 j += 1
#             if is_a_prime and a > 1:
#                 print("Nearest prime number is:", a)
#                 break
#             is_b_prime = True
#             k = 2
#             while k < b:
#                 if b % k == 0:
#                     is_b_prime = False
#                     break
#                 k += 1
#             if is_b_prime:
#                 print("Nearest prime number is:", b)
#                 break

#             a -= 1
#             b += 1

# for n in range(1,11):
#     x=n+1
#     i=1
#     is_square = False
#     while i * i <= x:
#         if i * i == x:
#             is_square = True
#             break
#         i += 1
#     if is_square:
#         print(n)

# for i in range(1,6):
#     print(i*i)

# count = 0
# num=1
# while count < 5:
#     sum = 0
#     for j in range(1,num):
#         if num % j ==0:
#             sum += j
#     if sum == num:
#         print(num)
#         count += 1
#     num += 1

# for i in range(1,11):
#     print(i)

# for i in range(1, 21):
#     if i % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# for i in range(5):
#     if i >= 0:
#         print("ps")
#     else:
#         print("Neg")

# str="deepthisriyha"
# for i in str:
#     if i in "aeiouAEIOU":
#         print(i)

# list1 = [1, 4, 7, 10, 13, 16]
# count = 0
# for i in list1:
#     if i % 2 ==0:
#         count += 1
# print(count)
    
# for i in range(1,51):
#     if i %3== 0:
#         print(i)

# for i in range(1,31):
#     if i % 5== 0:
#         print("Divisible by 5")
#     else:
#         print(i)

# for i in range(1,11):
#     print(i*i)

# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     print(i * i)

# n=input("enyer a str:")
# if n[0] in "aeiouAEIOU":
#     print("Starts with vowels")
# else:
#     print("Consonants")

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# marks = int(input("Enter marks: "))
# for i in range(5):
    
#     if marks >= 90:
#         print("Grade: A")
#     elif marks >= 70:
#         print("Grade: B")
#     elif marks >= 50:
#         print("Grade: C")
#     else:
#         print("Grade: Fail")

# str1=input("Enter:")
# v=0
# c=0
# d=0
# s=0
# for i in str1:
#     if i.lower() in "aeiou":
#         v += 1
#     elif i.isalpha():
#         c += 1
#     elif i.isdigit():
#         d+=1
#     elif i.isspace():
#         s+= 1
# print(v)
# print(c)
# print(d)
# print(s)

# for i in range(1,101):
#     if i > 1:
#         for n in range(2,i):
#             if i%n == 0:
#                 break
#         else:
#             print(i)

# lis1=["icdfeera","uidgdrlky","erdderhdc","aojdgg"]
# for i in lis1:
#     if i[0] in "aeiouAEIOU" and len(i) > 4:
#         print(i)

# n=6
# sum=0
# for i in range(1,6):
#     if n%i == 0:
#         sum+=i
# if n == sum :
#     print("Perfect")
# else:
#     print("NOT")

name=input('enter the name: ')
if name[0] in 'aeiou':
    print("starts with vowel")
else:
    print("starts with consonant")





