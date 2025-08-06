# import time
# class name:
#     def __init__(self):
#         print("Comsturcto")
#     def __del__(self):
#         print("Desctructor")
#     def method1(self):
#         print("Method")
# obj=name()
# obj.method1()
# time.sleep(2)
# del obj
# obj.method1()

# class india:
#     def capital(self):
#         self.india_C='new delhi'
#         print(self.india_C)
#     def n_language(self):
#         self.n_L = "hindi"
#         print(self.n_L)
# class America:
#     def captial(self):
#         self.C = 'washing ton DC'
#         print(self.C)
#     def n_language(self):
#         self.n_language='English'
#         print(self.n_language)
# def method(obj):
#     obj.capital()
#     obj.n_language()
# india_obj=india()
# method(india_obj)

# class A:
#     def __init__(self,a=None,b=None,c=None,d=None):
#         if a!=None and b!=None and c!=None and d!=None:
#             print(a+b+c+d)
#         elif a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=None and b!=None:
#             print(a+b)
#         else:
#             print("Enter two values: ")
# obj1=A([10,20,30],[100,200,300])


class B:
    def fun101(self,*v):
        T=0
        for x in v:
            T+=x
        print(T)
obj=B()
obj.fun101(10,20)
# obj.fun101(10,'AJay',True,12,103)




    