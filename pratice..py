import random
class Bank:
    H_Details=[]
    def create_new_ACCOUNT(self):
        new_Holder={}
        new_Holder['H_name']=input('Enter Holder name:')
        new_Holder['Moblie']=input("Enter Mobile Number:")
        new_Holder['Aadhar']=input("Enter Aadhar Number:")
        new_Holder['IFSC'] = 'IFSC0125' 
        data=random.randint(1000000000,9999999999)
        new_Holder['Accoun_nu'] = data
        n1=input('Select Account savong/Zero....').lower()
        while True:
            if n1 == 'saving':
                n2=int(input('Your Acc is Saving deposite 1000 Rupees'))
                if n2 == 1000:
                    new_Holder['Balance'] = n2
                else:
                    print("Deposit 1000 rupees......")
            elif n1 == 'Zero':
                n3 = int(input("Deposit 500 Rupees"))
                if n3==500:
                    new_Holder['Balance']=n3   
                    break
                else:
                    print("Deposit 500 Rupees /.........")
        Bank.H_Details.append(new_Holder)
        print(Bank.H_Details) 
    def Deposit(self):
        p1 = input('Enter Account Number')
        p2=input('Enter Holder Name: ') 
        p3=input('Enter Deposit money:')

        for x in Bank.H_Details:
            if x['Accoun_nu'] == p1 and x['H_name'] == p2 :
                data3=x.get('Balance')
                x['Balance']=data3+p3
            else:
                print('invalid Details')
        print(Bank.H_Details)
    def Withdraw(self):
        p1 = input('Enter Account Number')
        p2=input('Enter Holder Name: ') 
        p3=input('Enter Withdraw money:')
        for x in Bank.H_Details:
            if x['Accoun_nu'] == p1 and x['H_name'] == p2 :
                if x['Balnce'] >= p3:
                    x['Balance'] -= p3
                    print("Withdrawal successful.")
                else:
                    print("Insufficient Balance.")
                    break
            else:
                print("Invalid Details.")

        print(Bank.H_Details)
obj=Bank()
obj.create_new_ACCOUNT()
obj.Deposit()
obj.Withdraw()



                

