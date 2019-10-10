import copy
class Atm:

    amount_in_atm = 10000
    user_id = 0

    user = [{'name': 'Tom', 'pin': 1234,'balance': 15000}, 
            {'name': 'Jerry', 'pin': 5678, 'balance': 15000}, 
            {'name': 'Quacker', 'pin': 1357, 'balance': 15000}]

    def login(name):
        for user_id in range(len(Atm.user)):
            if(name == Atm.user[user_id]['name']):
                break

        if user_id == Atm.user_id:
            print("Already logged in...")
        else:
            entered_pin = int(input("Enter your pin to log in_ "))
            if entered_pin == Atm.user[user_id]['pin']:
                Atm.user_id = copy.deepcopy(user_id)
                print("Logged in successfully")
            else:
                print("Wrong pin!!!")

    def balance_check(name):
        for user_id in range(len(Atm.user)):
            if(name == Atm.user[user_id]['name']):
                break

        if user_id == Atm.user_id:
            print('Already Logged in...')
        else:
            entered_pin = int(input("Enter your pin to log in_ "))
            if entered_pin == Atm.user[user_id]['pin']:
                Atm.user_id = copy.deepcopy(user_id)
                print("Logged in successfully")
            else:
                print("Wrong pin!!!")
                return

        print("Your account balance is {}".format(Atm.user[user_id]['balance']))

    def withdraw(name):
        for user_id in range(len(Atm.user)):
            if(name == Atm.user[user_id]['name']):
                break

        if user_id == Atm.user_id:
            print('Already Logged in...')
        else:
            entered_pin = int(input("Enter your pin to log in_ "))
            if entered_pin == Atm.user[user_id]['pin']:
                Atm.user_id = copy.deepcopy(user_id)
                print("Logged in successfully")
            else:
                print("Wrong pin!!!")
                return
        
        amount_withdraw = int(input("Enter amount to withdraw_ "))
        if(amount_withdraw <= Atm.user[user_id]['balance'] and Atm.amount_in_atm >= amount_withdraw): 
            Atm.user[user_id]['balance'] = copy.deepcopy(Atm.user[user_id]['balance'] - amount_withdraw)
            print("Balance after withdraw {}".format(Atm.user[user_id]['balance']))
            Atm.amount_in_atm = copy.deepcopy(Atm.amount_in_atm - amount_withdraw)
        else:
            print("Less amount cannot withdraw...") 

    def change_pin(name):
        for user_id in range(len(Atm.user)):
            if(name == Atm.user[user_id]['name']):
                break

        if user_id == Atm.user_id:
            print('Already Logged in...')
        else:
            entered_pin = int(input("Enter your pin to log in_ "))
            if entered_pin == Atm.user[user_id]['pin']:
                Atm.user_id = copy.deepcopy(user_id)
                print("Logged in successfully")
            else:
                print("Wrong pin!!!")
                return

        new_pin = int(input("Enter your new pin..."))
        confirm_new_pin = int(input("Enter pin again to confirm..."))

        if(new_pin == confirm_new_pin):
            Atm.user[user_id]['pin'] = copy.deepcopy(confirm_new_pin)
            print("Pin changed successfully!.")

    def transfer_money(name):
        for user_id in range(len(Atm.user)):
            if(name == Atm.user[user_id]['name']):
                break

        if user_id == Atm.user_id:
            print('Already Logged in...')
        else:
            entered_pin = int(input("Enter your pin to log in_ "))
            if entered_pin == Atm.user[user_id]['pin']:
                Atm.user_id = copy.deepcopy(user_id)
                print("Logged in successfully")
            else:
                print("Wrong pin!!!")
                return
        transfer_person = input("Enter name of person to transfer...")
        amount_transfer = int(input("Enter amount to transfer..."))

        print(transfer_person)
        for transfer_user_id in range(len(Atm.user)):
            if(transfer_person == Atm.user[transfer_user_id]['name']):
                break

        Atm.user[transfer_user_id]['balance'] = copy.deepcopy(Atm.user[transfer_user_id]['balance'] + amount_transfer)
        Atm.user[user_id]['balance'] = copy.deepcopy(Atm.user[user_id]['balance'] - amount_transfer) 
        print("Money Transferred Successfully!.")

    def logout(name):
        Atm.user_id = None
        print("logged out Successfully")

a = 1

while(a != 0):
    print("1. Log In")
    print("2. Balance Check")
    print("3. Withdraw")
    print("4. Transfer money")
    print("5. Change Pin")
    print("6. Log Out")
    print("0. Exit") 
    user_name = input("Enter your name to get started_ ")
    flag =0
    for i in range(len(Atm.user)):
        if user_name == Atm.user[i]['name']:
            flag = 1
            a = int(input("Enter choice-"))


    switch = {1: 'login', 2: 'balance_check', 3: 'withdraw', 4: 'transfer_money' 5: 'change_pin', 6: 'logout'}
    print('Atm.' + (switch.get(a)+'('+user_name+')'))
