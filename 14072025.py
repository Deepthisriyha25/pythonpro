# h=[]
# n=int(input("Enter studemts: "))
# for x in range (n):
#     temp={}
#     temp['name'] = input("Enter name: ")
#     temp['pin'] = input("Enter pin")
#     temp['city'] = input("Ente city: ")
#     h.append(temp)
# print(h)

# h={'a':10,'b':20}
# res=dict([('a',10),('b',20)])
# print(res)

# j='python'
# dict={}
# for i in j:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict)

# g={'a':10,'b':20,'c':30}
# sum=0
# for val in g:
#     sum+=g[val]
# print(sum)

# a=input("Enter a alpha: ")
# dict={}
# if a in "aeiou":
#     print(a)
# else:
#     dict[(a.upper())] = ord(a.upper())  
#     print(dict)

# a=['name','pin','city']
# b=['ajay',101,'hyd']
# dict={}
# for i in range(len(a)):
#     dict[a[i]] = b[i]
# print(dict)


# l=['python','java','c++']
# res= [len(x) for x in l ]
# print(res)

# k=[2,3,4,5]
# res=["even" if x%2==0 else "Odd" for x in k ]
# print(res)

# n=11

# res=[x for x in range(1,n) if n%x==0]
# if len(res)==1:
#     print("prime")
# else:
#     print("Not")

# res=[x for x in range(10,20) if all(x%y!=0 for y in range(2,x))]
# print(res)

# num=2
# for i in range(10,20):
#     for j in (2,num):
#         if i%j == 0:
#             break
#         else:
#             print(i)
#         i+=1

# question: {10:[1,2,5],11:[1],12:[1,2,3,4,6]}
# # number and factors of number

# g ="python"
# res=[x for x in g if x in 'AEIOUaeiou']
# print(res)

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# c= list(set(list1) & set(list2))
# print(c) 

# res=[x for x in range(1,20) if x%3 == 0 and x%5 == 0]
# print(res)

# l1=['apple', 'window', 'python', 'garden', 'madam', 'level', 'radar', 'Wow','Mom']
# count=0
# for i in l1:
#     i=i.lower()
#     if i == i[::-1]:
#         count += 1
# print(count)
        
# str1="Python Language"
# res=[ord(x) for x in str1]
# print(res)

# str1 =["Sriyha","Sarada","sandhya","shyamala","Suvarna","Sujatha","Samskirthi"]
# res = [x[::-1] for x in str1]
# print(res)

# l1= [3, 4, 7, 10, 13, 17, 20, 23, 28, 29, 30, 37]
# res = [x for x in l1 if all(x%y != 0 for y in range(2,x))]
# print(res)

# d = {'a': 10, 'b': 5, 'c': 15} 
# max = max(d.values())
# min = min(d.values())
# print("Max number :",max)
# print("Min number:", min)

# l2 = [[1, 2, 3], [4, 5, 6]]
# res= [x for y in l2 for x in y]
# print(res)

# a = "python"
# print(a[0] + a[-1])

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# x = (1)
# print(type(x))

# a = [10, 20, 30, 40, 50]
# print(a[1:4])
# a[1:4] = [99]
# print(a)

# text = "Vamsi"
# text[0] = 'v'
# print(text)
# data = [1, 2, 3]
# print(data + data * 2)

# x = "Python"
# print(x[::3])

# a = [1, 2, 3]
# b = a[:]
# b.append(4)
# print(a)


# info = {'name': 'Vamsi', 'age': 22}
# info['name'] = ['Vamsi', 'Kiran']
# info['name'][0] = 'Ram'
# print(info)

# nums = [1, 2, 3]
# nums[1:2] = [10, 20, 30]
# print(nums)

# a = ['apple', 'banana', 'mango']
# b = a
# a = a + ['grape']
# print(b)

# val = [100]
# for i in val:
#     val.append(i + 1)
#     if i > 102:
#         break
# print(val)


# t = (1, 2, [3, 4])
# t[2][0] = 99
# print(t)

# a = "abcde"
# print(a[10:])
# print(a[-10:])

