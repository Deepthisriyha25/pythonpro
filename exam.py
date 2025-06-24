#Write a function generate_pin() that returns a random 4-digit numeric PIN
"""import random
def generate_pin():
    a=random.randint(1000,9999)
    print(a)
generate_pin()
"""
"""cities = ["Hyderabad", "Mumbai", "delhi", "Pune", "chennai", "KOLKATA"]
for i in cities:
    if i.isupper() or i.islower():
        print(i)
    """
"""nested = [100, 200, [300, 400, [500, "target"]]]
print(nested[2][2][1])"""

"""template = "Hello {user}, your booking in {location} is confirmed for {days} days."
print(template.format (user="Ananya", location="Goa",days=3 ))"""

import copy
list2 = [[1, 2], [3, 4]]
shallow = copy.copy(list2)
deep = copy.deepcopy(list2)
list2[0][0] = 999
print("list:", list2)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)
