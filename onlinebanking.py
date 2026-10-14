import os
import random
import time
clear = lambda: os.system('clear')

accounts = []

class Account:
    def __init__(self, name, balance, history, iban):
        self.name = name #account userName
        self.balance = balance #float
        self.history = history #transaction history array
        self.iban = iban #id to send money to

class Transaction:
    def __init__(self, amount, reason):
        self.amount = amount
        self.reason = reason

def accountInfo(accounts, id):
    print(f"\n{accounts[id].name}'s transaction history:\n")
    print(Transaction)

def home(accounts):

    print(f"IBAN\tName\t\tBalance\n")

    for x in range(len(accounts)):
        print(f"{accounts[x].iban}\t{accounts[x].name}\t\t{accounts[x].balance}$")

    targetAccount = int(input("\nOpen Wallet (ID): "))

    for x in range(len(accounts)):
        if accounts[x].iban == targetAccount:
            print("\naccount found!")
            accountInfo(accounts, x)

def boot():

    clear()

    names = [
        "Adrian", "Amelia", "Andrew", "Audrey", "Calvin",
        "Carmen", "Celine", "Damian", "Daniel", "Darren",
        "Elijah", "Emily", "Ethan", "Felix", "Harper",
        "Isabel", "Jordan", "Julian", "Lauren", "Logan",
        "Marcus", "Morgan", "Naomi", "Oliver", "Rachel",
        "Samuel", "Stella", "Thea", "Thomas", "Victor"
    ]

    for x in range(int(input("How many accounts do you want to generate?: "))):

        if(x == 0): print() # for space in console

        newAccount = Account(

        f"{random.choice(names)}",
        float(random.randint(0, 1000000)/100),
        [],
        random.randint(0,99)+((x+1)*100))


        """
        for x in range(random.randint(10)):
            newTransaction = Transaction(float(0), "")
            if random.randint(0, 1) == 1:
                newTransaction.amount = #plus
                newTransaction.reason = #salary, ...
            else:
                newTransaction.amount = #minus
                newTransaction.reason = #groceries, rent, ...
        """


        print(f"ceated {newAccount.name} (IBAN: {newAccount.iban}) with a balance of {newAccount.balance}$")
        time.sleep(0.1)
        
        accounts.append(newAccount)

    print("")
    home(accounts)

boot()
