import copy
class Atm:

    amount_in_atm = 10000
    status = False

    user = {'Tom': {'pin': 1234, 'balance': 15000, 'withdrawMoney': 6000, 'user_id': False},
            'Jerry': {'pin': 5678, 'balance': 15000, 'withdrawMoney': 6000, 'user_id': False}, 
            'Quacker': {'pin': 1357, 'balance': 15000, 'withdrawMoney': 6000, 'user_id': False}}

    def __init__(self, kwargs):
        self.balance = kwargs.get("balance")
        self.pin = kwargs.get("pin")
        self.withdrawMoney = kwargs.get("withdrawMoney")
        self.user_id = kwargs.get("user_id")
    
    def balance_check(self, name):
        print("\nYour account balance is {}\n".format(self.balance))

    def withdraw(self, name):
        print("\nPossible withdraw Money {}".format(self.withdrawMoney))
        amount_withdraw = 0
        while True:
            try:
                amount_withdraw = int(input("\nEnter amount to withdraw_ "))
                break
            except ValueError:
                print("Not a valid amount!!!")
        
        if amount_withdraw <= self.balance and Atm.amount_in_atm >= amount_withdraw and self.withdrawMoney >= amount_withdraw: 
            self.balance = self.balance - amount_withdraw
            Atm.user[name]['balance'] = Atm.user[name]['balance']- amount_withdraw
            Atm.amount_in_atm = Atm.amount_in_atm - amount_withdraw
            self.withdrawMoney = self.withdrawMoney - amount_withdraw
            Atm.user[name]['withdrawMoney'] = Atm.user[name]['withdrawMoney'] - amount_withdraw
            print("Balance after withdraw {}\n".format(self.balance))
        else:
            print("\nLimit Exceeded / Less Money\n")

    def change_pin(self, name):
        new_pin, confirm_new_pin = 0, 0
        while True: 
            try:
                new_pin = int(input("Enter your new pin in 4 digits..."))
                confirm_new_pin = int(input("Enter pin again to confirm..."))
                if re.match(r"[0-9]{4}", new_pin) and re.match(r"[0-9]{4}", confirm_new_pin) and new_pin == confirm_new_pin :
                    Atm.user[name]['pin'] = confirm_new_pin
                    print("\nPin changed successfully!.")
                    self.user_id = False
                    Atm.user[name]['user_id'] = False
                    Atm.status = False
                    print("Enter credentials again to log in...\n")
                else:
                    print("Pin conditions unmatched...")    
                break
            except ValueError:
                print("Invalid pin")    

    def transfer_money(self, name):
        transfer_name = input("\nEnter name of person to transfer...")
        amount_transfer = 0
        while True:
            try:
                amount_transfer = int(input("Enter amount to transfer..."))
                break
            except ValueError:
                print("Not a valid amount...")  

        transfer_person = Atm(Atm.user.get(transfer_name))
        Atm.user[transfer_name]['balance'] = Atm.user[transfer_name]['balance'] + amount_transfer
        self.balance = (self.balance - amount_transfer) 
        print("\nMoney Transferred Successfully!.")
        print("Your balance after transfer {}\n".format(self.balance))

    def logout(self, name):
        self.user_id = False
        Atm.user[name]['user_id'] = False
        Atm.status = False
        print("\nLogged out Successfully\n ")

    def no_option(self, name):
        exit()

while(Atm.status == False):
    print("LOG IN::")
    user_name = input("User Name_ ")
    pin = int(input("Pin_ "))
    if pin == Atm.user[user_name]['pin']:
        print("\nLogged In\n ")
        user = Atm(Atm.user.get(user_name))
        user.user_id = True
        Atm.status = True
    else:
        print("Try Again!")
        continue  

    while(user.user_id == True):
        print("1. Balance Check")
        print("2. Withdraw")
        print("3. Transfer Money")
        print("4. Change Pin")
        print("5. Logout")
        print("6. Exit")

        try: 
            option = int(input("\nEnter choice_ "))
        except ValueError:
            print("\nInvalid Choice\n") 
            continue

        def choice(option):
            if option >=1 and option <=6:
                switch = {1: user.balance_check, 
                            2: user.withdraw,
                            3: user.transfer_money, 
                            4: user.change_pin, 
                            5: user.logout, 
                            6: user.no_option
                        }       
                return switch.get(option, "Invalid Choice")(user_name)
            else:
                print("\nInvalid Choice!!!\n")     
        choice(option)