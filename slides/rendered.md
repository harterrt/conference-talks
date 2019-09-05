background-color: black
class: center, middle, title

# Common Sense Stats: Bootstrapping

**Ryan Harter**

Senior Staff Data Scientist, Mozilla

---

# Sampling

* Population: Big and unweildy
* Sample: Small and wieldy

---

# Example - Pile of Money

![Breaking Bad Bed of Money](static/breaking-bad-money-bed.jpeg)

???

For example, let's say you have a Walter White style pile of money.

You don't know the mix of denominations but
you know the pile weighs about 200 pounds.

---

# Example - Pile of Money

## Facts:

* 200 lbs of US Bills (~90k bills)
* Unknown denominations
* Takes 1 hour to count 1 pound
* Takes ~2.5 weeks to count it all

???

A US bill weighs about 1 gram,
there's about 450 grams per pound,
so ~90k bills.

Working 80 hour weeks, it would take 2.5 weeks to count it all.

But, you have better things to do than counting money.
A reasonable person would count a bunch of money and scale it up.

---

# The Pile

https://github.com/harterrt/conference-talks/


```python
import pandas as pd

pile = pd.read_csv('data/pile_of_money.csv')
pile_value = sum(pile['denomination'])

print('Number of bills in pile: {0}\n'.format(len(pile)))

print('Sample values:\n {0} \n'.format(pile[10:15].to_string(index=False)))
```

    Number of bills in pile: 90600
    
    Sample values:
      denomination
               20
               50
               20
               20
               10 
    


---

# The Plan

* Count one pound of bills
* Multiply by 200
* Good enough for me

???

For this exercise, I've generated some data to represent our pile of money.
I got a random selection of ~90k bills of varying denominations.

---
# Sample - Results


```python
bills_per_pound = 450

sample = pile.sample(bills_per_pound, random_state=42)
sample_value = sum(sample['denomination'])

print('Sample value: ${0:,}'.format(sample_value))
print('Estimated population value: ${0:,}'.format(sample_value * 200))
print('Actual population value   : ${0:,}'.format(pile_value))
print(
  '\nError: {0:0.2f}%'
  .format((sample_value * 200 / pile_value - 1) * 100)
)
```

    Sample value: $16,817
    Estimated population value: $3,363,400
    Actual population value   : $3,566,992
    
    Error: -5.71%


---
# Sample - Posibilities?

* What does the risk look like?
* We have an advantage of seeing everything

???

TODO: insert code for drawing lots of samples

---

# Sample - Simulation

???

TODO: Show histogram of sampling errors

---

# Summary

* Cool, right?
* But not useful in practice
* We never see the population...

---

# Bootstrapping

* What if we re-use our sample?
* Contains all we know about the population
