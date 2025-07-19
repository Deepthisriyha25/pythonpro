"""num=4
op=isinstance(4,float)
op=isinstance((1,2,3),list)
print(op)"""
"import random"
"""y=random.random()
print(y)"""
"""z=random.uniform(5,8)
print(z)"""
"""k=["HELLO","hi","PYTHON","css","js","react","DJANGO"]
for x in k: 
    if x==x.upper():
        print(x)
for y in k:
    if y==y.lower():
        print(y)"""
"""str="hello world"
op=str.capitalize()
print(op)"""
"""str="hello i am from nellore my name is deepthi sriyha"
op=str.title()
print(op)"""
"""str1="My NaME Is deepthiSRIYHA"
op3=str1.swapcase()
print(op3)"""
"""ip="wlcom"
op=ip.find("e")
print(op)
"""
"""str="welcome hello"
op=str.rfind("e")
print(op)"""
"""str1="s@o@m@e@t@h@i@n@g"
op=str1.split("@",5)
print(op)"""
"""ip=[5,7,8]
ip.extend({4,5,6}) #this will allows
print(ip)"""
"""ip=[1,2,3,3,2,1]
ip.pop(1) 
# #it will remove only first match of the argument and doesn't returns anything
print(ip)"""
"""#shallow copy and deep copy.
import copy
ip1=[[1,2],[5,6]]
ip2=ip1.copy()
ip2[0][1]="hi"

print(ip1,ip2)
ip1=[["hi","hello"],["js","python"]]
ip2=copy.deepcopy(ip1)

ip2[0][1]="bye"

print(ip1,ip2)
"""
