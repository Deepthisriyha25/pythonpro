def stud(Name,Age,Gender,Qualification):
    print("Name:",Name)
    print("Age:",Age)
    print("Gender:",Gender)
    print("Qualification:",Qualification)
stud("Alice",21,"Female","B.Sc Computer Science")

#Fav Food Items using Arbitrary
def fav_foods(*foods):
    print(*foods)
fav_foods("Choclate","Biriyani","idli","DOsa","Ice Cream", "Gulab jamun")

#AbhiBus Operator
def passenger_det(passengername,fromplace,toplace,buspartner="AbhiBus"):
    print(f"Hello {passengername}, greetings from {buspartner}, Your Journey from {fromplace} to {toplace} is confirmed. happy Journey")
passenger_det("Jhon","hyd","Vijayawada")

