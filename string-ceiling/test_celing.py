"""
test_celing.py
--------------
Accuracy test for celing.py.

Generates 1000 random positive and 1000 random negative numbers with
1-2 decimal places, runs each through celing(), and compares the result
with Python's official math.ceil(). It then prints how many answers
were incorrect -- expect 0 for both groups.

Run with:  python test_celing.py
"""

import math
import random

from celing import celing

random.seed(42)     # fixed seed, so the test gives the same numbers every time
TESTS = 1000        # number of random values to check for each sign

wrong_positive = 0  # count of wrong answers for positive numbers
wrong_negative = 0  # count of wrong answers for negative numbers


def random_number(negative):
    """Build one random number as a string with 1-2 decimal places."""
    whole = random.randint(0, 999)
    decimals = random.choice([1, 2])
    frac = "".join(random.choice("0123456789") for _ in range(decimals))
    sign = "-" if negative else ""
    return f"{sign}{whole}.{frac}"


for i in range(TESTS):
    # Check a positive number, e.g. "47.3"
    num = random_number(negative=False)
    if int(celing(num)) != math.ceil(float(num)):
        wrong_positive += 1

    # Check a negative number, e.g. "-47.3"
    num = random_number(negative=True)
    if int(celing(num)) != math.ceil(float(num)):
        wrong_negative += 1

print(f"numbers tested per sign : {TESTS}")
print(f"positive -- incorrect   : {wrong_positive}")
print(f"negative -- incorrect   : {wrong_negative}")
