def match_status(team,match_won):
    if(match_won):
        print(f"{team} won the match")
    else:
        print(f"{team} lost the match")
match_status("RCB",True)
match_status("PBKS",False)
match_status("SRH",True)
match_status("CSK",False)

def login_status(email,password):
    if email and password == 1:
        print("Login Sucessfull")
    else:
        print("Login Failed")
login_status(True,True)
login_status(False,True)
login_status(True,False)
login_status(False,False)

def evenodd(a):
    if a%2==0:
        print(f"{a} is Even Number")
    else:
        print(f"{a} is Odd Number")
evenodd(6)

def maxmin(x,y):
    if x>y:
        print(f"{x} is Maximum Number")
    else:
        print(f"{y} is Maximum Number")
maxmin(20,55)

def marks(x):
    if x>=35:
        print("Passed in Exams")
    else:
        print("Failed in Exams")
marks(90)
marks(30)

def Age(x):
    if x>=18:
        print("Eligible for Vote")
    else:
        print("Not Eligible for vote")
Age(15)
Age(87)
def checker(x):
    if x>0:
        print("Greater NUmber")
    else:
        print("Less Number")
checker(27)
checker(-98)

def lenght(s):
    if len(s) %2 == 0:
        print("even lenght")
    else:
        print("odd lenght")
lenght("Deepthisriyha")
lenght("Priya")

def discount(price):
    if price > 1000:
        dis = price*(10/100)
        finalprice = price-dis
        print(f"{finalprice} your total")
    else:
        print(f"{price}Rs")
discount(2000)
discount(200)
