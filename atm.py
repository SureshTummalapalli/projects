#Atm application
balance=1000
while True: 
    option=int(input("enter the 1 for credit,2 for debit,3 for balance_checking,4 for pin generation,5 for exit:"))
    def credit():
        if option==1:
            inp=int(input("enter the amount to credit:"))
            global balance
            balance+=inp
            print("credit sucessfully")
    credit()

    def debit():
        if option==2:
            inp=int(input("enter the amount to debit:"))
            global balance        
            print("debit successfully")
            balance-=inp 
    debit()  

    def balance_checking():
        if option==3:
            global balance
            print(balance)
    balance_checking()

    def pin():
        if option==4:
           inp=input("enter the  new pin :")
           print("pin generated sucessfully")
    pin() 
    if option==5:
        print("thank you for visting")
        break