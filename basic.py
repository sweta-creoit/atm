class Atm:

    amount_in_atm = 10000
    status = False

    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def login(self):
        if(Atm.status == True):
            print("You are already logged in...")
        else:
            entered_pin = int(input("Enter your pin to log in_ "))
            if(entered_pin == self.pin):
                print("Logged in Successfully!")
                Atm.status = True
            else:
                print("Wrong pin ! kindly check")

    def balance_check(self):
        if(Atm.status == False):
            print("You are not logged in.")
            entered_pin = int(input("Enter your pin to check balance_ "))

            if(entered_pin == self.pin):
                print("Logged in Successfully.")
                Atm.status = True
            else:
                print("Wrong Pin!!!")

        print("Your balance is {}".format(self.balance))
          
    def withdraw(self):
        if(Atm.status == False):
            print("Log In to withdraw money. ") 
            entered_pin = int(input("Enter pin to withdraw money. ")) 
               
            if(entered_pin == self.pin): 
                Atm.status = True 
       
        money_to_withdraw = int(input("Enter anmount to withdrawn. "))
        
        if(money_to_withdraw <= self.balance and Atm.amount_in_atm >= money_to_withdraw): 
            self.balance = self.balance - money_to_withdraw
            Atm.amount_in_atm = Atm.amount_in_atm - money_to_withdraw

        else: 
            print("Amount balance is less. ")

    def transfer_money(self):
        if (status == False):
            print("Log In to transfer money. ")
            entered_pin = int(input("Enter pin to transfer money_ "))

            if(entered_pin == self.pin):
                print("Logged in")
                name = input("Enter person name to transfer_ ")
                amount = int(input("Enter amount to transfer "))

                self.balance = self.balance - amount
                #name.balance = name.balance + amount

    def change_pin(self):
        if (Atm.status == False):
            print("Log in to change pin")
            entered_pin = int(input("Enter pin to log in: "))

            if(self.pin == entered_pin):
                Atm.status == True

        new_pin = int(input("Enter new pin: "))
        confirm_new_pin = int(input("Enter once again to confirm: "))    

        if(new_pin == confirm_new_pin):
            print("Pin changed successfully")    
            self.pin = copy.deepcopy(new_pin)

    def logout(self):
        Atm.status = False
        print("logged out Successfully")

obj = []
Tom = Atm('Tom', 1234, 15000)
Jerry = Atm('Jerry', 5678, 15000)
Quacker = Atm('Quacker', 1357, 15000)

a = 1

while(a != 0):
    print("1. Log In")
    print("2. Balance Check")
    print("3. Withdraw")
    print("4. Transfer money")
    print("5. Change Pin")
    print("6. Log Out")
    print("0. Exit") 
    user = input("Enter your name to get started_ ")
    #pin = int(input("Enter your pin_ "))
   		 
            
    a = int(input("Enter choice-"))
   
    if(a == 1):
    	user.login()
    elif(a == 2):
    	user.balance_check()
    elif(a == 3):
    	user.withdraw()
    elif(a == 4):
    	user.transfer_money()
    elif(a == 5):
    	user.change_pin()
    elif(a == 6):
    	user.logout()
    else:
    	print("Invalid choice")	