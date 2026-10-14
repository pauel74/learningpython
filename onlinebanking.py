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

def moveBack(accounts, index): #moves every entry at given index one back so a new transaction can be addad at [0]
    temporaryTransaction = Transaction(float(0), "")
    accounts[index].history.append(temporaryTransaction)
    for x in range(len(accounts[index].history)):
        accounts[index].history[(len(accounts[index].history)-x) -1] = accounts[index].history[(len(accounts[index].history)-x) -2]
    return accounts

def accountInfo(accounts, id):
    print(f"\n{accounts[id].name}'s transaction history:\n")
    time.sleep(0.25)

    print("Amount \t Reason\t\tBalance\n")
    time.sleep(0.25)

    balance = accounts[id].balance
    
    for x in range(len(accounts[id].history)):
        
        if accounts[id].history[x].amount > 0:
            print(GREEN, end="+")
        else:
            print(RED, end="")

        print(int(accounts[id].history[x].amount), "\t" , accounts[id].history[x].reason, f"\t{round(balance, 2)}$" , RESET)
        time.sleep(0.05)
   
        balance -= accounts[id].history[x].amount
    time.sleep(0.25)
    print(YELLOW + "\n[1] Send money")
    time.sleep(0.1)
    print("[2] Back" + RESET)
    time.sleep(0.1)
    if input("\n") == "1":
        
        time.sleep(0.1)
        targetAccount = int(input("\nIBAN: " + YELLOW))

        for x in range(len(accounts)):
            if accounts[id].iban == targetAccount:
                time.sleep(0.25)
                print(RED + "\nYou cannot send money to yourself!" + RESET)
                time.sleep(1)
                accountInfo(accounts, id)
                break
            if accounts[x].iban == targetAccount:
                time.sleep(0.25)
                print(RESET + "\naccount found!")
                time.sleep(0.25)
                money = input("\nAmount: " + YELLOW)
                if float(money) > accounts[id].balance:
                    time.sleep(0.25)
                    print(RED + f"\nYou only have {round(accounts[id].balance,2)}$" + RESET)
                    time.sleep(1)
                    accountInfo(accounts, id)
                    break
                else:
                    time.sleep(0.25)
                    print(GREEN + f"\n{accounts[id].iban}" + RESET, end=" ")
                    time.sleep(0.15)
                    for y in range(20):
                        time.sleep(0.1)
                        print(">", end="", flush=True) # flush makes it so it shows the progress instead of just waiting 2 seconds and then printing it to the console

                    newTransaction = Transaction(float(money), f"{accounts[x].name}\t")
                    accounts = moveBack(accounts, id)
                    accounts[id].history[0] = (newTransaction)
                    accounts[id].balance -= float(money)

                    newTransaction = Transaction(float(money), f"{accounts[id].name}\t")    
                    accounts = moveBack(accounts, x)
                    accounts[x].history[0] = (newTransaction)
                    accounts[x].balance += float(money)

                    time.sleep(0.25)
                    print(GREEN + f" {targetAccount}")
                    time.sleep(0.5)
                    print("\nTransaction completed")

                    accountInfo(accounts, id)

        time.sleep(0.25)
        print(RED + "\nAccount not found!" + RESET)
        time.sleep(1)
        accountInfo(accounts, id)

    else: print(); home(accounts)


def home(accounts):

    time.sleep(0.25)
    print(f"IBAN\tName\t\tBalance\n")
    time.sleep(0.25)


    for x in range(len(accounts)):
        print(YELLOW + f"{accounts[x].iban}\t" + RESET + f"{accounts[x].name}\t\t{round(accounts[x].balance,2)}$")
        time.sleep(0.05)


    targetAccount = int(input("\nOpen Wallet (ID): "))

    for x in range(len(accounts)):
        if accounts[x].iban == targetAccount:
            time.sleep(0.25)
            print("\naccount found!")
            time.sleep(0.25)
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

        if(x == 0): print(); time.sleep(0.25) # for space in console and "calculating" >_<

        newAccount = Account(

        f"{random.choice(names)}",
        float(random.randint(0, 1000000)/100),
        [],
        random.randint(0,99)+((x+1)*100))

        for x in range(random.randint(3,15)):
            newTransaction = Transaction(float(0), "")
            if random.randint(0, 1) == 1:
                newTransaction.amount = random.randint(0, int(newAccount.balance/5))
                newTransaction.reason = random.choice(["salary", "interest", "dividend", "bonus\t", "refund"])
            else:
                newTransaction.amount = random.randint(int(newAccount.balance/15), int(newAccount.balance/5)) * -1
                newTransaction.reason = random.choice(["groceries", "rent\t", "subscriptions", "shopping", "utilities"])
            newAccount.history.append(newTransaction)

        print(f"ceated {newAccount.name} (IBAN: {newAccount.iban}) with a balance of {newAccount.balance}$")
        time.sleep(0.1)
        
        accounts.append(newAccount)

    print("")
    home(accounts)

boot()
