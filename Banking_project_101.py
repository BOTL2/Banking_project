#Python PRoject 101
#Banking Operation

import random
import time

class Bank:
    Bank_name = "Jamuna Bank"
    Bank_branch_location = "Jamuna Bank Tower, Plot# 14, Bir Uttam A. K. Khandaker Road, Block# C, Gulshan-1, Dhaka, Bangladesh."

    def __init__(self, username, id, phone_num, password):
        self.username = username
        self.id = id
        self.phone_num = phone_num
        self.password = password
        self.balance = 0.0
        self.dict1 = {}
        self.dict1["UserName"] = self.username
        self.dict1["ID"] = self.id
        self.dict1["Phone Number"] = self.phone_num

        print("Welcome", self.username, "To", Bank.Bank_name, ".You Have Created a Account Successfully!")

    def authenticate(self, password):
        return self.password == password

    def deposite(self, amount):
        self.balance += amount
        print(amount, "Tk Deposited Successfully")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(amount, "Tk Successfully Withdrawn")
        else:
            print("Sorry Insufficient Balance!")

    def balance(self):
        print("Your Current Balance Is", self.balance)

    def display(self):
        print("Your Information Below..")
        print(self.dict1)

    def cash_in(self, cash_in):
        self.balance += cash_in
        print(cash_in, "Tk Successfully Added!")

    def generate_otp(self):
        return random.randint(100000, 999999)

    def generate_pass_via_otp(self):
        new_password=input("Enter Your Password..")
        confirm_password=input("Again Enter Your Password..")

        if new_password==confirm_password:
            OTP=self.generate_otp()
            print("Your OTP is",OTP)
            Otp_1=input("Enter The OTP You Have Got Right Now..")
            if Otp_1==OTP:
                self.password=new_password
            else:
                print("Wrong OTP Entered..Try Again")


        else:
            print("Password Mismatched..")

special_chr="@#!*"
id_1="0123456789"
username = input("Enter Your Username: ")
id = input("Enter Your Account Id: ")
if len(id)<8 and id_1 not in id:
    print("Wrong Id ..Try Again")
else:
    id=id

phone_num = input("Enter Your Phone Num: ")
if len(phone_num)<10 :
    print("Phone Number Total Digit is 11 ")
elif len(phone_num)>10 and id.startswith("01"):
    id=id
password = input("Create a Password: ")
if len(password)>6 and special_chr in password :
    password=password

else:
    print("should be 6 length Long..")



C_time=time.localtime()
formate=time.strftime("%Y-%m-%d %H:%M:%S",C_time)
print("Local Date & Time is",formate)

print("Welcome to ", Bank.Bank_name, Bank.Bank_branch_location, "Branch\n=========================")

obj1 = Bank(username, id, phone_num, password)

while True:
    print('Please Select Any Option Below!')
    print("1. Deposite\n2. Withdraw\n3. Balance\n4. Stop\n5. Display\n6.Set_Password_With_OTP")

    option = int(input("Enter option: "))

    if option == 4:
        print("Thanks For Using", Bank.Bank_name, "Online Platform. Have A Great Day!")
        break

    if option == 1:
        password = input("Enter your password: ")
        if obj1.authenticate(password):
            amount = float(input("Enter your amount: "))
            obj1.deposite(amount)
        else:
            print("Incorrect Password!")

    if option == 2:
        password = input("Enter your password: ")
        if obj1.authenticate(password):
            amount = float(input("Enter the Amount of Withdraw: "))
            obj1.withdraw(amount)
        else:
            print("Incorrect Password!")

    if option == 3:
        password = input("Enter your password: ")
        if obj1.authenticate(password):
            obj1.balance()
        else:
            print("Incorrect Password!")

    if option == 5:
        password = input("Enter your password: ")
        if obj1.authenticate(password):
            obj1.display()
        else:
            print("Incorrect Password!")

    # if option == 6:
    #     password = input("Enter your password: ")
    #     if obj1.authenticate(password):
    #         cash_in = float(input("Enter The Amount You Want To CashIn: "))
    #         obj1.cash_in(cash_in)


    if option==6:
        password=input("Enter The Password..")
        if obj1.authenticate(password):
            obj1.generate_pass_via_otp()
        else:
            print("Wrong Password..")
