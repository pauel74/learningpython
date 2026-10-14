import os
import random
import time

RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

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

    print("Amount \t Reason\t\tBalance\n")

    balance = accounts[id].balance
    
    for x in range(len(accounts[id].history)):
        
        if accounts[id].history[x].amount > 0:
            print(GREEN, end="+")
        else:
            print(RED, end="")

        print(accounts[id].history[x].amount, "\t" , accounts[id].history[x].reason, f"\t{round(balance, 2)}$" , RESET)
        
        balance -= accounts[id].history[x].amount


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

        for x in range(random.randint(1,15)):
            newTransaction = Transaction(float(0), "")
            if random.randint(0, 1) == 1:
                newTransaction.amount = random.randint(0, int(newAccount.balance/5))
                newTransaction.reason = random.choice(["salary", "interest", "dividend", "bonus\t", "refund"])
            else:
                newTransaction.amount = random.randint(int(newAccount.balance/15), int(newAccount.balance/5)) * -1
                newTransaction.reason = random.choice(["groceries", "rent\t", "subscription", "shopping", "utilities"])
            newAccount.history.append(newTransaction)

        print(f"ceated {newAccount.name} (IBAN: {newAccount.iban}) with a balance of {newAccount.balance}$")
        time.sleep(0.1)
        
        accounts.append(newAccount)

    print("")
    home(accounts)

boot()
