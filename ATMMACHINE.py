#ATM MACHINE 

print("welcome to Kotak Mahindra Bank")
pw=int(input("enter 6 digit pin:"))
amount=50000
if (pw==123456):
    print("1-Withdrawal")
    print("2-Balance Enquiry")
    print("3-Fastcash")
    c=int(input("Please choose the required option for transaction:"))
    if(c==1):
        w=int(input("Enter the amount to be withdraw :"))
        if (w<amount and w%100==0):
            print(f"Please take the amount:{w}")
        else:
                print("invalid cash")
    if (c==2):
        print("your available balance is :",amount)
    elif(c==3):
        print("1->5000")
        print("2->10000")
        print("3->15000")
        print("4->20000")
        f=int(input("enter the fastcash option :"))
        if (f==1 and 5000<amount):
            print("please collect 5000")
        if (f==2 and 10000<amount):
            print("please collect 10000")
        if (f==3 and 15000<amount):
            print("please collect 15000")
        if (f==4 and 20000<amount):
            print("please collect 20000")
        else:
            print("invalid option")
else:
    print("invalid password")
