import requests

print("**CRYPTO DATA**")
searchMethod = int(input("1 -- Top Grossing Coins  2 -- Search Coins "))


def manInput():
    print("ENTER COINS, ENTER OK WHEN DONE")
    coins = []
    Done = False
    while not Done:
        inputCoin = str(input('Enter coin: '))
        if(inputCoin == 'ok' or inputCoin == 'OK'):
            Done = True
        else:
            coins.append(inputCoin)
    return coins

if searchMethod == 1:
    coins = ['bitcoin', 'etherum', 'monero']
elif searchMethod == 2:
    coins = manInput()

##Fetch data##

for n in range(len(coins)):
    coin = coins[n]
    coin = coin.lower()
    response = requests.get("https://api.coincap.io/v2/assets/"+coin)
    if (response.status_code != 200):
        print('Error fetching data')
    else:
        print(response.json()['data']['name'])
        print("Price: ", response.json()['data']['priceUsd'])
        print("Market Cap: ", response.json()['data']['marketCapUsd'])
        print("Change % 24 hr", response.json()['data']['changePercent24Hr'])


