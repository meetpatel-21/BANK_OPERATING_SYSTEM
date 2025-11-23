class Bank:
     bank_name="HDFC"
     branch_name="A23,Anand Nagar,Thane"
     account_counter=1000
     #creating account
     def __init__(self,username,pan_id,address,password):
      self.username=username
      self.pan_id=pan_id
      self.address=address
      self.balance=0.0
      self.password=password
      self.account_no=Bank.account_counter
      Bank.account_counter+=1
      self.transaction_history=[]

     def deposit(self,amount):
         if amount<0:
             print("please add amount that should be positive")
         else:
             print(f" hello {self.username} your account is created sucessfully")  
             self.balance=amount+self.balance
             self.transaction_history.append(f"deposited {amount}")
             print( f" Hello {self.username} rupees {amount} is credited to your account")
         
     def withdraw(self,amount):
         if amount<0:
             print("withdraw amount should be positive")
         elif amount<=self.balance:
            self.balance=self.balance-amount
            self.transaction_history.append(f"withdraw {amount}")
            print(f"{amount} is withdrawn from your account")
         else:
           print("insufficient fund")
           
     def ministatement(self):
         print(f"{self.balance} is your current balance")
         print("Transaction History")
         for transaction in self.transaction_history:
             print(transaction)

     def add_interest(self,rate,years):
         interest=self.balance*(rate/100)*years
         self.balance=self.balance+interest
         self.transaction_history.append(f"interest added{interest}")
         print(f"interest added{interest}")
               
     def change_address(self,new_address):
         self.address=new_address
         print("address is updated sucessfully")
         
     def show_details(self):
         print(f"Username:{self.username}")
         print(f"Pan_id:{self.pan_id}")
         print(f"Address:{self.address}")
         print(f"Account_no:{self.account_no}")
         print(f"balance:{self.balance}")
     
    
print("------------------------------------------------")        
print(f"Welcome to {Bank.bank_name},{Bank.branch_name}")
print("------------------------------------------------")
username=input("enter the name of the user:")
pan_id=input("enter the id of pan card:")
address=input("enter the address:")
password=input("enter the password:")
d=Bank(username,pan_id,address,password)
while True:
    print("------------------------------------------------")
    print("Selected of the given option \n:")
    print("1)deposit")
    print("2)withdraw")
    print("3)Ministallment")
    print("4)Add interest")
    print("5)change address")
    print("6)Show details")
    print("7)Stop")
    print("------------------------------------------------")
    choice=int(input("enter choice form:1 to 7:"))         
    if choice==1:
        amount=float(input("enter the deposited amount:"))
        d.deposit(amount)
    elif choice==2:
        amount=float(input("enter the withdrawn amount:"))
        d.withdraw(amount)
    elif choice==3:
        d.ministatement()
    elif choice==4:
        rate=int(input("enter the rate is:"))
        years=int(input("enter the year:"))
        d.add_interest(rate,years)
    elif choice==5:
        new_address=input("enter the address:")
        d.change_address(new_address)
    elif choice==6:
        d.show_details()
    elif choice==7:
        print("thank for using")                   
        break
    else:
        print("invalid input")


