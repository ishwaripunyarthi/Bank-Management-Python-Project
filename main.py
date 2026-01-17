import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    # -------- Load Data --------
    if Path(database).exists():
        with open(database, "r") as fs:
            data = json.load(fs)
    else:
        data = []

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        chars = (
            random.choices(string.ascii_letters, k=3)
            + random.choices(string.digits, k=3)
            + random.choices("!@#$%^&*", k=1)
        )
        random.shuffle(chars)
        return "".join(chars)

    # -------- Create Account --------
    def Createaccount(self):
        name = input("Tell your name: ")
        age = int(input("Tell your age: "))
        email = input("Tell your email: ")
        pin = input("Tell your 4-digit PIN: ")

        if age < 18 or not pin.isdigit() or len(pin) != 4:
            print("❌ Age must be 18+ and PIN must be 4 digits")
            return

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "accountNo": Bank.__accountgenerate(),
            "balance": 0
        }

        Bank.data.append(info)
        Bank.__update()

        print("\n✅ Account created successfully!")
        for k, v in info.items():
            print(f"{k}: {v}")
        print("⚠ Please note down your Account Number\n")

    # -------- Deposit --------
    def depositmoney(self):
        accnumber = input("Account Number: ")
        pin = int(input("PIN: "))

        userdata = [u for u in Bank.data if u["accountNo"] == accnumber and u["pin"] == pin]

        if not userdata:
            print("❌ No such user found")
            return

        amount = int(input("Amount to deposit: "))
        if 0 < amount <= 10000:
            userdata[0]["balance"] += amount
            Bank.__update()
            print("✅ Amount deposited successfully")
        else:
            print("❌ Deposit must be between 1 and 10000")

    # -------- Withdraw --------
    def withdrawmoney(self):
        accnumber = input("Account Number: ")
        pin = int(input("PIN: "))

        userdata = [u for u in Bank.data if u["accountNo"] == accnumber and u["pin"] == pin]

        if not userdata:
            print("❌ No such user found")
            return

        amount = int(input("Amount to withdraw: "))
        if amount <= userdata[0]["balance"]:
            userdata[0]["balance"] -= amount
            Bank.__update()
            print("✅ Amount withdrawn successfully")
        else:
            print("❌ Insufficient balance")

    # -------- Show Details --------
    def showdetails(self):
        accnumber = input("Account Number: ")
        pin = int(input("PIN: "))

        userdata = [u for u in Bank.data if u["accountNo"] == accnumber and u["pin"] == pin]

        if not userdata:
            print("❌ No such user found")
            return

        print("\n📄 Your Details:")
        for k, v in userdata[0].items():
            print(f"{k}: {v}")

    # -------- Update Details --------
    def updatedetails(self):
        accnumber = input("Account Number: ")
