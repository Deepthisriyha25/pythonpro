#simple interst ---
P=int(input("Enter Principle Amount: "))
T=int(input("Enter Time Peroid (in days): "))
R=int(input("Enter Rate of Interst: "))
si=(P*T*R)/100
print("Simple Interst =",si)

#Temperature ----
c=int(input("Enter Temperature (in c)"))
f=c*(9/5)+32
print("Fahrenheit Temparture = ",f,"F")

#Average of 3 numbers
n1=int(input("Enter First Number : "))
n2=int(input("Enter Second Number : "))
n3=int(input("Enter Third  Number : "))
Avg = (n1+n2+n3)/100
print("Average of 3 numbers is ",Avg)

#Area of circle
pi=3.14
r=int(input("Enter Radius Value"))
Area  = pi*r**2
print("Area of Circle",Area)

#swap 2 numbers
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
temp=a
a=b
b=temp
print(a)
print(b)