# stage 3
## Description
A real coffee machine doesn't have an infinite supply of water, milk, or coffee beans. And if you input a really big number, it's almost certain that a real coffee machine wouldn't have the supplies needed to make all that coffee for you.

In this stage, you need to improve the previous program. Now you will check amounts of water, milk, and coffee beans available in your coffee machine at the moment.

## Objectives
Write a program that does the following:

It requests the amounts of water, milk, and coffee beans available at the moment, and then asks for the number of cups a user needs.
If the coffee machine has enough supplies to make the specified amount of coffee, the program should print "Yes, I can make that amount of coffee".
If the coffee machine can make more than that, the program should output "Yes, I can make that amount of coffee (and even N more than that)", where N is the number of additional cups of coffee that the coffee machine can make.
If the amount of given resources is not enough to make the specified amount of coffee, the program should output "No, I can make only N cups of coffee".
Like in the previous stage, the coffee machine needs 200 ml of water, 50 ml of milk, and 15 g of coffee beans to make one cup of coffee.

## Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:
```
Write how many ml of water the coffee machine has:
> 300
Write how many ml of milk the coffee machine has:
> 65
Write how many grams of coffee beans the coffee machine has:
> 100
Write how many cups of coffee you will need:
> 1
Yes, I can make that amount of coffee
```
Example 2:
```
Write how many ml of water the coffee machine has:
> 500
Write how many ml of milk the coffee machine has:
> 250
Write how many grams of coffee beans the coffee machine has:
> 200
Write how many cups of coffee you will need:
> 10
No, I can make only 2 cups of coffee
```
Example 3:
```
Write how many ml of water the coffee machine has:
> 1550
Write how many ml of milk the coffee machine has:
> 299
Write how many grams of coffee beans the coffee machine has:
> 300
Write how many cups of coffee you will need:
> 3
Yes, I can make that amount of coffee (and even 2 more than that)
```
Example 4:
```
Write how many ml of water the coffee machine has:
> 0
Write how many ml of milk the coffee machine has:
> 0
Write how many grams of coffee beans the coffee machine has:
> 0
Write how many cups of coffee you will need:
> 1
No, I can make only 0 cups of coffee
```
Example 5:
```
Write how many ml of water the coffee machine has:
> 0
Write how many ml of milk the coffee machine has:
> 0
Write how many grams of coffee beans the coffee machine has:
> 0
Write how many cups of coffee you will need:
> 0
Yes, I can make that amount of coffee 
```
Example 6:
```
Write how many ml of water the coffee machine has:
> 200
Write how many ml of milk the coffee machine has:
> 50
Write how many grams of coffee beans the coffee machine has:
> 15
Write how many cups of coffee you will need:
> 0
Yes, I can make that amount of coffee (and even 1 more than that)
```

## solution
```javascript
const input = require('sync-input')

// console.log(`Starting to make a coffee
// Grinding coffee beans
// Boiling water
// Mixing boiled water with crushed coffee beans
// Pouring coffee into the cup
// Pouring some milk into the cup
// Coffee is ready!`)
let water = input('Write how many ml of water the coffee machine has:');
let milk = input('Write how many ml of milk the coffee machine has:');
let beans = input('Write how many grams of coffee beans machine has:');
let userCups = input('Write how many cups of coffee you will need:');
// console.log(`For ${userCups == 1 ? `${userCups} cup` : `${userCups} cups`} of coffee you will need:
// ${userCups*200} ml of water
// ${userCups*50} ml of milk
// ${userCups*15} g of coffee beans`);
let cups = Math.min(Math.floor(water/200), Math.floor(milk/50), Math.floor(beans/15));
switch (Math.sign(cups - userCups)){
    case (-1):
        console.log(`No, I can make only ${cups} cups of coffee.`);
        break;
    case (0):
        console.log('Yes, I can make that amount of coffee');
        break;
    default:
        console.log(`Yes, I can make that amount of coffee (and even ${cups - userCups} more than that)`);
        break;
}
```
