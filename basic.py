import copy
class Atm:

    amount_in_atm = 10000
    status = False

    user = {'Tom': {'pin': 1234, 'balance': 15000},
            'Jerry': {'pin': 5678, 'balance': 15000}, 
            'Quacker': {'pin': 1357, 'balance': 15000}}

    def login(name):
        if Atm.status == True:
            print("Already logged in...")
        else:
            entered_pin = int(input("Enter your pin to log in_ "))
            if entered_pin == Atm.user[name]['pin']:
                print("Logged in successfully")
                Atm.status = True
            else:
                print("Wrong pin!!!")

    def balance_check(name):
        if Atm.status == True:
            print('Logged in...')
        else:
            entered_pin = int(input("Enter your pin to log in_ "))

            if entered_pin == Atm.user[name]['pin']:
                print("Logged in successfully")
                status = True
            else:
                print("Wrong pin!!!")
                return

        print("Your account balance is {}".format(Atm.user[name]['balance']))

    def withdraw(name):
        if Atm.status == True:
            print('Logged in...')
        else:
            entered_pin = int(input("Enter your pin to log in_ "))

            if entered_pin == Atm.user[name]['pin']:
                print("Logged in successfully")
                Atm.status = True
            else:
                print("Wrong pin!!!")
                return

        amount_withdraw = int(input("Enter amount to withdraw_ "))

        if(amount_withdraw <= Atm.user[name]['balance'] and Atm.amount_in_atm >= amount_withdraw): 
            Atm.user[name]['balance'] = copy.deepcopy(Atm.user[name]['balance'] - amount_withdraw)
            print("Balance after withdraw {}".format(Atm.user[name]['balance']))
            Atm.amount_in_atm = copy.deepcopy(Atm.amount_in_atm - amount_withdraw)
        else:
            print("Less amount cannot withdraw...") 

    def change_pin(name):
        if Atm.status == True:
            print('Logged in...')
        else:
            entered_pin = int(input("Enter your pin to log in_ "))
            if entered_pin == Atm.user[name]['pin']:
                print("Logged in successfully")
                Atm.status = True
            else:
                print("Wrong pin!!!")
                return

        new_pin = int(input("Enter your new pin..."))
        confirm_new_pin = int(input("Enter pin again to confirm..."))
        
        if(new_pin == confirm_new_pin):
            Atm.user[name]['pin'] = copy.deepcopy(confirm_new_pin)
            print("Pin changed successfully!.")

    def transfer_money(name):
        if Atm.status == True:
            print('Already Logged in...')
        else:
            entered_pin = int(input("Enter your pin to log in_ "))

            if entered_pin == Atm.user[name]['pin']:
                print("Logged in successfully")
                Atm.status = True
            else:
                print("Wrong pin!!!")
                return

        transfer_person = input("Enter name of person to transfer...")
        amount_transfer = int(input("Enter amount to transfer..."))
    
        Atm.user[transfer_person]['balance'] = copy.deepcopy(Atm.user[transfer_person]['balance'] + amount_transfer)
        Atm.user[name]['balance'] = copy.deepcopy(Atm.user[name]['balance'] - amount_transfer) 
        print("Money Transferred Successfully!.")

    def logout(name):
        Atm.status = False
        print("logged out Successfully")

option = 1

while(option != 0):
    print("1. Log In")
    print("2. Balance Check")
    print("3. Withdraw")
    print("4. Transfer money")
    print("5. Change Pin")
    print("6. Log Out")
    print("0. Exit") 
    user_name = input("Enter your name to get started_ ")
    option = int(input("Enter choice-"))
    '''flag =0
    for i in range(len(Atm.user)):
        if user_name == Atm.user[i]['name']:
            flag = 1
            
    if flag == 0:
        print("Invalid User")'''

    def choice(option):
        #print("Value of choice {}".format(option))     
        switch = {1: Atm.login, 
                    2: Atm.balance_check, 
                    3: Atm.withdraw, 
                    4: Atm.transfer_money, 
                    5: Atm.change_pin, 
                    6: Atm.logout
                    }
        #print(switch.get(option))
        return switch.get(option, "Invalid Choice")(user_name)  

    
    choice(option)