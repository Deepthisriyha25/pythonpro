a=100 #literal notation
b=100 #literal notation
print(id(a))
print(id(b))
#Taking Consturctor
a=int("90")
b=int("90")
###
print(id(a))
print(id(b))

#Interning
a = "10000 Coders"
b = "10000 Coders" 
print(id(a))
print(id(b))
#Garbage Value
#Mutable
a = [1, 2]
print(id(a))
a.append(3)
print(id(a))
#Immutable
C = 10
print(id(C))
C = C + 1
print(id(C))  

