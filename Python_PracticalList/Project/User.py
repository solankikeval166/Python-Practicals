user={
    'income': 0,
    'expance':0,
    'balance':0
}

while True:
    choice = int(input("Enter your choice: "))
    
    if choice == 0:
        print("Program terminated successfully")
        break
        
    elif choice == 1:
        user['income']=int(input("Input income: "))
        print("Your Balance: ")
        
    elif choice == 2:
        user['expance']=int(input("Enter expance: "))
        print("Your expenses: ")
        
    elif choice == 3:
        user['balance']=user['income']-user['expance']
        print("Your balance is :")