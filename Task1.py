a=300
b=50.23
print(id(a))
print(a//b)

list1=["Mango",9,"chennai","apple",25,2,4,"Banglore"]
print(len(list1))
print(id(list1))
print(list1[3])
list1[3]=100
print(list1)

Tuple1=(0,"Hyderabad",2,"10000Coders",4,"Python",7,"html")
print(id(Tuple1))
print(type(Tuple1))
print(len(Tuple1))
print(Tuple1[3])

dict1 = {"name": "Thor","type": "Truck","range": "300 miles","battery": "800 kWh"}
print(len(dict1))
print(id(dict1))
print(dict1)
print(dict1["type"])

str1 = "10000 coders Hyderabad"
print(len(str1))
print(str1[12])
print(str1[-9])

set1={25,9,20,2,4,5,25,29,25,5,4}
print(set1)
print(len(set1))
set1.add(99)
print(set1)

frozenset1={1,4,2,3,5,7,8}
print(frozenset1)