import matplotlib.pyplot as plt
import random
import time

def generatePrice(prices = []):
    prices.append(prices[len(prices)-1] + (random.randint(-100,100))/25)
    prices[len(prices)-1] *= 1 + 0.07 / 365 # average 7% a year
    return prices
    
plt.ion()

start = 100

prices = [start]

for i in range(365):
    prices = generatePrice(prices)

    print(round(prices[-1],2))

    plt.clf() # clears diagram

    # ui
    plt.title("Price: " + str(round(prices[-1],2)) + "$ Percentage: ")
    plt.xlabel("Day")
    plt.ylabel("Price")

    if prices[-1] > start:
        plt.plot(prices, color="green")
    else:
        plt.plot(prices, color="red")

    plt.pause(0.1)

plt.ioff() # deactivate dynamic mode
plt.show() # keep diagram open after simulation
