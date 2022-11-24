# practices
**A study record**

## Project1: Simple Chatty Bot （Completed on 2022.9.29）

## Project2: Currency Converter (Completed on 2022.10.3)

**Objectives:**  

Take the first input – the currency that you have. It is default for all the calculations.
Retrieve the data from FloatRates as before.
Save the exchange rates for USD and EUR (these are the most popular ones, so it's good to have rates for them in advance).
Take the second input – the currency code that you want to exchange money for, and the third input – amount of money you have.
Check the cache. Maybe you already have what you need?
If you have the currency in your cache, calculate the result.
If not, get it from the site, and calculate the result.
Save the rate to your cache.
Print the result.
Repeat steps 4-9 until there is no currency left to process.

**Example 1:**
```python{.line-numbers}
> ILS
> USD
> 45
Checking the cache...
Oh! It is in the cache!
You received 13.84 USD.
> RSD
> 57
Checking the cache...
Sorry, but it is not in the cache!
You received 1684.41 RSD.
> EUR
> 33
Checking the cache...
Oh! It is in the cache!
You received 8.38 EUR.
```
**Example 2:**
```python{.line-numbers}
> USD
> EUR
> 20
Checking the cache...
Oh! It is in the cache!
You received 16.52 EUR.
> NOK
> 45
Checking the cache...
Sorry, but it is not in the cache!
You received 382.1 NOK.
> SEK
> 75
Checking the cache...
Sorry, but it is not in the cache!
You received 624.66 SEK.
> NOK
> 55
Checking the cache...
Oh! It is in the cache!
You received 467.02 NOK.
> ISK
> 91
Checking the cache...
Sorry, but it is not in the cache!
You received 11708.38 ISK.
```
