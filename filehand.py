import csv
with open('csv100.csv','w',newline="") as k:
    obj=csv.writer(k)
    obj.writerow(['s.no','employee_name','employee_age','employee_salary'])
    n=3
    for x in range(n):
        a=int(input("Enter s.no: "))
        b=input("Enter employee_name: ")
        c=int(input("Enter employee_age: "))
        d=float(input("Enter employee_salary: "))
        obj.writerow([a,b,c,d])
print("Employee with age 35 and salary >10000 ")
with open('csv100.csv', 'r') as k:
    reader = csv.DictReader(k)
    for x in reader:
        if int(x['employee_age']) == 35 and float(x['employee_salary']) > 10000:
            print(x['employee_name'])




