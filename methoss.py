"""num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
num1 = int(input("Enter a number"))
sum = 0
while(num1>0):
    sum += num1%10
    num1 //= 10
print(sum)"""
"""str1=input("Enter a string")
count = 0
for i in str1:
    x = i.lower()
    if x in "aeiou":
        count += 1
print(count)
"""
# palindrome = input("Enter string")
# s = ""
# for i in range(len(palindrome)-1,-1,-1):
#     s += palindrome[i]
# if (palindrome == s):
#     print(f"{palindrome} is a palindrome")
# else:
#     print(f"{palindrome} is not a palindrome")


# list1=[23,55,78,33,79,24,98,33,78,50,1111]
# print(max(list1))

# str5 = input("Enter string")
# s2 = ""
# for i in range(len(str5)-1,-1,-1):
#     s2 += str5[i]
# print(s2)
# list3=[3,5,56,87,56,22,78,11,2,4,56,78,22,87]
# ele = int(input("Enter element: "))
# count1= list3.count(ele)
# print(f"{ele} apper {count1} times ")



"""li2= [3,55,78,99,2,3,44,44,22,45,66,3]
l=[]
for i in li2:
    if i not in l:
        l.append(i)
print(l)

N = int(input("Enter a number: "))
for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
"""
"""n = int(input("Enter N Values: "))
num = 2
while n > 0:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
        n -= 1
    num += 1"""

N = int(input("Enter the value of N: "))
i = 2
count = 0

print(f"First {N} prime numbers are:")

while count < N:
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")
        count += 1
    i += 1
