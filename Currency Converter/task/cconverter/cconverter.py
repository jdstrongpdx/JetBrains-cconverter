import requests


def main():
    """ Main function gets, validates, and returns currency information to user """
    symbol_one = str(input(""))
    data_one = get_rate(symbol_one)
    cache = ['usd', 'eur']
    while True:
        symbol_two = input("")
        if symbol_two == "":
            break
        else:
            amount = float(input(""))
            print("Checking the cache...")
            if symbol_two in cache:
                print("Oh! It is in the cache!")
            else:
                print("Sorry, but it is not in the cache!")
            rate_one = data_one[symbol_two]['rate']
            cache.append(symbol_two)
            # calculate amount
            amount = rate_one * amount
            print(f"You received {amount:.2f} {symbol_two.upper()}.")


def get_rate(symbol):
    """ gets current currency rates via API
    :parameter (str) symbol: the stock symbol to lookup via API
    :return (json) data: returns the json data from the API
    """

    site = "http://www.floatrates.com/daily/" + symbol + ".json"
    response = requests.get(site)
    data = response.json()
    return data


main()
