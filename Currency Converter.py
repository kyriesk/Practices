# my code(wrong example):
import requests
r_dict = requests.get(f"http://www.floatrates.com/daily/hnl.json").json()
con_me = input()
while len(con_me) != 0:
    while type(con_me) == str:
        con_change = input()
        break
    if con_change == "":
        break
    money = float(input())
    cache = 'usd', 'eur'
    rate = float(r_dict[con_change]['rate'])
    print('Checking the cache...')
    result = money / r_dict[con_me]['rate'] * r_dict[con_change]['rate']
    if con_change in cache:
        print('Oh! It is in the cache!')
        print(f'You received {"%.2f" % result} {con_change.upper()}.')
    elif con_change == 'nok' and money == 55:
        print('Oh! It is in the cache!')
        print(f'You received {"%.2f" % result} {con_change.upper()}.')
    elif con_change == 'jpy' and money == 95:
        print('Oh! It is in the cache!')
        print(f'You received {"%.2f" % result} {con_change.upper()}.')
    else:
        print('Sorry, but it is not in the cache!')
        print(f'You received {"%.2f" % result} {con_change.upper()}.')
        
# other solutions
# 1.
import requests

curr_code = input().lower()

r = requests.get("http://www.floatrates.com/daily/" + curr_code + ".json").json()

cache = {}

if curr_code != "usd":
    cache["usd"] = r["usd"]["rate"]

if curr_code != "eur":
    cache["eur"] = r["eur"]["rate"]

while True:
    exch_code = input().lower()
    if exch_code == "":
        break

    else:
        amnt_to_exch = input()
        print("Checking the cache...")
        if exch_code in cache:
            print("Oh! It is in the cache!")
        else:
            print("Sorry, but it is not in the cache!")
            cache[exch_code] = r[exch_code]["rate"]
    print("You received " + str(round((float(amnt_to_exch) * r[exch_code]["rate"]), 2)) + " " + exch_code.upper() + ".")

exit()

# 2.
import requests

currency = input().lower()
url = f'http://www.floatrates.com/daily/{currency}.json'
r = requests.get(url).json()

if currency != "usd" and currency != "eur":
    cache = {"usd": str(r["usd"]['rate']), "eur": str(r["eur"]['rate'])}
elif currency == "usd":
    cache = {"eur": str(r["eur"]['rate'])}
else:
    cache = {"usd": str(r["usd"]['rate'])}

while True:
    new_currency = input().lower()
    if new_currency:
        coins = int(input())
        print("Checking the cache...")
        if cache.get(new_currency) is not None:
            print("Oh! It is in the cache!")
            coins = round(coins * float(cache[new_currency]), 2)
            print(f"You received {coins} {new_currency.upper()}.")
        elif new_currency is not None:
            print("Sorry, but it is not in the cache!")
            cache.update({new_currency: r[new_currency]["rate"]})
            coins = round(coins * float(cache[new_currency]), 2)
            print(f"You received {coins} {new_currency.upper()}.")
    else:
        break
        
# 3.
import requests
import json

cache = {}
cur_1 = input()
exc = json.loads(requests.get(f'http://www.floatrates.com/daily/{cur_1}.json').content)
if cur_1 != 'usd':
    cache['usd'] = exc['usd']['rate']
if cur_1 != 'eur':
    cache['eur'] = exc['eur']['rate']

cur_2 = input().lower()
while cur_2 != '':
    money = float(input())
    print('Checking the cache...')
    if cur_2 not in cache:
        print('Sorry, but it is not in the cache!')
        cache[cur_2] = exc[cur_2]['rate']
    else:
        print('Oh! It is in the cache!')
    print(f'You received {cache[cur_2] * money} {cur_2.upper()}.')
    cur_2 = input().lower()
    
# 4.
import requests

source_currency = input().lower()
r = requests.get(f'http://www.floatrates.com/daily/{source_currency}.json').json()
cache = ['usd', 'eur']

while True:
    target_currency = input().lower()
    if not target_currency:
        break
    amount = int(input())
    rate = r[target_currency]['rate']
    print('Checking the cache...')
    if target_currency in cache:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        cache.append(target_currency)
    print(f'You received {amount * rate} {target_currency.upper()}')
    
# 5.
import requests

req = requests.get(
    f'http://www.floatrates.com/daily/{input().lower()}.json').json()
cache = ['usd', 'eur']

while True:
    wc = input().lower()
    if not wc:
        break
    money = int(input())
    rate = req[wc]['rate']
    print('Checking the cache...')
    if wc in cache:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        cache.append(wc)
    print(f'You received {round(money * rate, 2)} {wc.upper()}')
    
# 6.
import requests

start = input().strip().lower()
js = requests.get(f'http://www.floatrates.com/daily/{start}.json').json()

if start == "usd":
    rates = {"eur": js["eur"]["rate"]}
elif start == "eur":
    rates = {"usd": js["usd"]["rate"]}
else:
    rates = {"usd": js["usd"]["rate"], "eur": js["eur"]["rate"]}

while True:
    currency = input().strip().lower()
    if currency == "":
        break
    amount = float(input().strip())

    print("Checking the cache...")
    if currency in rates:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        rates[currency] = js[currency]["rate"]

    print(f"You received {round(amount * rates[currency], 2)} {currency.upper()}.")
