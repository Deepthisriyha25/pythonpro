""""def larsmall(a,b,c):
    if a>b and a>c:
        print("A is large")
    elif  b>c:
        print("B is largrst")
    else:
        print("C is largest")
a=int(input("enter1: "))
b=int(input("enter2: "))
c=int(input("enter3: "))
larsmall(a,b,c)

def small(a,b,c):
    if a<b and a<c:
        print("A is small")
    elif  b<c:
        print("B is small")
    else:
        print("C is small")
a=int(input("enter1: "))
b=int(input("enter2: "))
c=int(input("enter3: "))
small(a,b,c)

def table(num):
    for i in range(1,11):
        print(f"{num} * {i} = ",num*i)
num=int(input("ENter"))
table(num)"""

mobiles = [
    {"name": "Apple", "model": "iPhone 16 Pro Max", "ram": 8, "camera": "48MP + 48MP + 12MP", "price": 135900},
    {"name": "Samsung", "model": "Galaxy Z Fold6", "ram": 12, "camera": "50MP + 12MP + 10MP", "price": 138990},
    {"name": "Google", "model": "Pixel 9 Pro XL", "ram": 12, "camera": "50MP + 48MP + 48MP", "price": 124999},
    {"name": "Vivo", "model": "X Fold3 Pro", "ram": 12, "camera": "50MP + 64MP + 50MP", "price": 87590},
    {"name": "Samsung", "model": "Galaxy S25 Ultra", "ram": 12, "camera": "200MP + 50MP + 10MP + 50MP", "price": 117999},
    {"name": "Xiaomi", "model": "15 Ultra", "ram": 12, "camera": "50MP + 50MP + 200MP", "price": 109998},
    {"name": "OnePlus", "model": "10 Pro 5G", "ram": 8, "camera": "48MP + 50MP + 8MP", "price": 50199},
    {"name": "Sony", "model": "Xperia 1 IV", "ram": 12, "camera": "12MP + 12MP + 12MP", "price": 108999},
    {"name": "Apple", "model": "iPhone 16 Plus", "ram": 8, "camera": "Dual Primary Camera", "price": 126999},
    {"name": "Vivo", "model": "X200 Pro", "ram": 12, "camera": "50MP + 50MP + 200MP", "price": 87590}
]
for mble in mobiles:
    if mble["ram"]>8 and mble["price"] < 120000:
        print(mble)

