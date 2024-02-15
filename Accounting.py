# Requirment
# Login / Register
# while login ask user to deposit, withdraw or check balance
# deposit  : ask the amount and store the amount of the user in a file
# withdraw : ask the amount and reduce the amount of the user in a file 
# check balance : print the user total amount

import json

def register():
    username = input("Enter a username : ")
    password = input("Create a password: ")

    userdata = {"username": username, "password": password}
    json_userdata = json.dumps(userdata)

    f = open("D:/Python With Django/Mind Riser/Accounting/userdata.txt","a")
    f.write(json_userdata + "-")
    f.close()

    user_choice = input("Do you want to login? [y/n]: ").lower()
    if user_choice == "y":
        login()
    else:
        print("Registration Successfully!")

def login():
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")

    f = open("D:/Python With Django/Mind Riser/Accounting/userdata.txt","r")
    json_user_datas = f.read()
    f.close()


    list_user_data = json_user_datas.split("-")
    user_login = False
    for i in list_user_data:
        if i!= '':
            dict_data = json.loads(i)
            if (user_name == dict_data.get("username")) and password == dict_data.get("password"):
                user_login = True
                break

    if user_login == True:
        print("Login Successful!!") 
        print("What would you like to do? ")       
        user_choice = input("[deposit/ withdraw/ check balance]: ").lower()
        if user_choice == "deposit":
            deposit(user_name)
        elif user_choice == "withdraw":
            withdraw(user_name)
        elif user_choice == "check balance" or user_choice == "checkbalance":
            check_balance(user_name)
        else:
            print("Invalid Selection!!")



    if user_login == False:
        print("Invalid credentials!!!")
        input_again = input("Would you like to login again? [y/n]: ").lower()
        if input_again == "y":
            login()
        else:
            print("Please try again.")


def deposit(username):
    deposit_amount = int(input("Enter the deposit amount: "))
    f = open("D:/Python With Django/Mind Riser/Accounting/account.txt","r")
    account_json = f.read()
    f.close()
    list_account = account_json.split("-")
    current_balance = 0
    if list_account != []:
        for i in list_account:
            if i!= "":
                dict_data = json.loads(i)
                if (username == dict_data.get("username")):
                    current_balance = dict_data.get("Balance")
        new_balance = int(current_balance) + deposit_amount
        account = {"username":username , "deposit_amount":deposit_amount, "Balance": new_balance}
        json_data = json.dumps(account)
        f = open("D:/Python With Django/Mind Riser/Accounting/account.txt","a")
        f.write(json_data + "-")
        f.close()
        print(f"Successfully deposited Rs. {deposit_amount}. Your balance is Rs. {new_balance}")
        return 
    
    account = {"username":username ,"deposit_amount":deposit_amount, "Balance": deposit_amount}
    json_data = json.dumps(account)
    f = open("D:/Python With Django/Mind Riser/Accounting/account.txt","a")
    f.write(json_data + "-")
    f.close()
    print(f"Successfully deposited Rs. {deposit_amount}. Your balance is Rs. {new_balance}")
         
    


def check_balance(username):
    f = open("D:/Python With Django/Mind Riser/Accounting/account.txt","r")
    account_json = f.read()
    f.close()
    current_balance = 0
    list_account = account_json.split("-")
    if list_account != []:
        for i in list_account:
            if i!= "":
                dict_data = json.loads(i)
                if (username == dict_data.get("username")):
                    current_balance = dict_data.get("Balance")
    print(f"Hi {username}! Your balance is Rs. {current_balance}")


def withdraw(username):
    withdraw_amount = int(input("Enter the withdraw amount: "))
    f = open("D:/Python With Django/Mind Riser/Accounting/account.txt","r")
    account_json = f.read()
    f.close()
    current_balance = 0
    list_account = account_json.split("-")
    if list_account != []:
        for i in list_account:
            if i!= "":
                dict_data = json.loads(i)
                if (username == dict_data.get("username")):
                    current_balance = dict_data.get("Balance")
    if withdraw_amount <= current_balance:
        new_balance = current_balance - withdraw_amount
        account = {"username":username , "withdraw_amount": withdraw_amount, "Balance": new_balance}
        json_data = json.dumps(account)
        g = open("D:/Python With Django/Mind Riser/Accounting/account.txt","a")
        g.write(json_data + "-")
        g.close()
        print(f"Successfully Withdrawn Rs. {withdraw_amount}. Your balance is Rs. {new_balance}")
        
    else: 
        print("Insufficient balance!")



while True:
    user_choice = input("Do you want to login or register? ").lower()

    if user_choice == "register":
        register()
    elif user_choice == "login":
        login()
    else: 
        print("Invalid option!!!")
    user_choice = input("Do you want to use this CLI program again? (y/n)")
    if(user_choice =="y" or user_choice == "Y"):
        continue
    elif(user_choice =="n" or user_choice =="N"):
        print("Thank you for using this CLI program ")
        break
    else:
        print("Invalid Option")
        break

withdraw()