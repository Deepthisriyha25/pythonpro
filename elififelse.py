

def login_sys(login,user_role):
    if login == True:
        if (user_role=="admin"):
            return "Welcome Admin"
        else:
           return "Welcome User"
    else:
        return "go and login firest" 

print(login_sys(True,"admin"))

def rank(pass_st,rank):
    if pass_st == True:
        if (rank<=100000):
           print("Congrats u get seat in JNTUH")
        else:
           print("Local college")
    else:
        print("Not qualifies better to join in bcom")
print(rank(False))

def emp(fe,be,db):
    if(fe ==True and be==True and db==True):
        print(" full stack developer")
    elif fe==True:
        print(" frontend developer")
    elif be==True :
        print(" backend developer")
    elif db==True:
        print("Database Developer")
    else:
        print("go and join in 10000 coders ")
emp(True,True,True)
emp(False,False,True)


