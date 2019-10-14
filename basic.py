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
        
    def login(self, name):
        if self.user_id == True:
            print("\nAlready logged in...")
        else:
            entered_pin = int(input("Enter your pin to log in_ "))
            if entered_pin == self.pin:
                print("\nLogged in successfully")
                Atm.user[name]['user_id'] = True
            else:
                print("\nWrong pin!!!")

    def balance_check(self, name):
        if self.user_id == True:
            print('Logged in...')
        else:
            entered_pin = int(input("Enter your pin to log in_ "))

            if entered_pin == self.pin:
                print("\nLogged in successfully")
                Atm.user[name]['user_id'] = True
            else:
                print("\nWrong pin!!!")
                return

        print("\nYour account balance is {}".format(self.balance))

    def withdraw(self, name):
        if self.user_id == True:
            print('Logged in...')
        else:
            entered_pin = int(input("Enter your pin to log in_ "))
            if entered_pin == self.pin:
                print("\nLogged in successfully")
                Atm.user[name]['user_id'] = True
            else:
                print("\nWrong pin!!!")
                return
        print("\nPossible withdraw Money {}".format(self.withdrawMoney))
        amount_withdraw = int(input("\nEnter amount to withdraw_ "))
        
        if amount_withdraw <= self.balance and Atm.amount_in_atm >= amount_withdraw and self.withdrawMoney >= amount_withdraw: 
            self.balance = self.balance - amount_withdraw
            Atm.user[name]['balance'] = Atm.user[name]['balance'] - amount_withdraw
            print("\nBalance after withdraw {}".format(self.balance))
            Atm.amount_in_atm = Atm.amount_in_atm - amount_withdraw
            Atm.user[name]['withdrawMoney'] = Atm.user[name]['withdrawMoney'] - amount_withdraw
        else:
            print("\nLimit Exceeded / Less Money")

    def change_pin(self, name):
        if self.user_id == True:
            print('Logged in...')
        else:
            entered_pin = int(input("Enter your pin to log in_ "))
            if entered_pin == self.pin:
                print("\nLogged in successfully")
                Atm.user[name]['user_id'] = True
            else:
                print("\nWrong pin!!!")
                return

        new_pin = int(input("Enter your new pin..."))
        confirm_new_pin = int(input("Enter pin again to confirm..."))
        
        if(new_pin == confirm_new_pin):
            Atm.user[name]['pin'] = confirm_new_pin
            print("\nPin changed successfully!.")
            Atm.user[name]['user_id'] = False

    def transfer_money(self, name):
        if self.user_id == True:
            print('Already Logged in...')
        else:
            entered_pin = int(input("Enter your pin to log in_ "))

            if entered_pin == self.pin:
                print("\nLogged in successfully")
                Atm.user[name]['user_id'] = True
            else:
                print("\nWrong pin!!!")
                return

        transfer_name = input("\nEnter name of person to transfer...")
        amount_transfer = int(input("Enter amount to transfer..."))
        transfer_person = Atm(Atm.user.get(transfer_name))
        Atm.user[transfer_name]['balance'] = Atm.user[transfer_name]['balance'] + amount_transfer
        self.balance = (self.balance - amount_transfer) 
        print("\nMoney Transferred Successfully!.")
        print("\nYour balance after transfer {}".format(self.balance))

    def logout(self, name):
        self.user_id = False
        Atm.user[name]['user_id'] = False
        print("\nLogged out Successfully")

    def no_option(name):
        exit()

option = 1

while(option != 0):
    print("\n\n    Log In \t\t\tBalance Check")
    print("{user_name}.login \t {user_name}.balance\n")
    print("    Withdraw \t\t\tTransfer Money")
    print("{user_name}.withdraw \t {user_name}.transfer\n")
    print("    Change Pin \t\t\t Log Out")
    print("{user_name}.change_pin \t    {user_name}.logout\n")
    print("\t\t\tExit")
    print("\t\t{user_name.exit}\n\n")

    option = input("Enter choice - in above format_ \n")
    name, function_to_do = option.split('.')[0], option.split('.')[1]

    user_name = Atm(Atm.user.get(name))

    def choice(function_to_do):
        switch = {'login': user_name.login, 
                    'balance': user_name.balance_check, 
                    'withdraw': user_name.withdraw,
                    'transfer': user_name.transfer_money, 
                    'change_pin': user_name.change_pin, 
                    'logout': user_name.logout, 
                    'exit': user_name.no_option
                }
        return switch.get(function_to_do, "Invalid Choice")(name)  
    choice(function_to_do)