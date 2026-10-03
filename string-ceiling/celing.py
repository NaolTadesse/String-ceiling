"""
celing.py
---------
A ceiling function that works on a number as a STRING, without ever
converting it to an int or float.

Why strings? It shows how ceiling works at the digit level:
each character is moved to the next digit by hand, the same way
you would do it on paper.

How it works:
  1. Split the input on "." into a whole part and a fraction part.
  2. If the fraction is all zeros (e.g. "3.0"), the number is already
     whole, so return it unchanged.
  3. Otherwise, drop the fraction and round the whole part UP:
       - Positive numbers: add 1 to the last digit. If it is a "9",
         it rolls over to "0" and the digit on its left is increased
         instead (same as 99 + 1 = 100).
       - Negative numbers: ceiling moves toward zero, so the whole
         part is kept as it is (e.g. -3.2 becomes -3).

This matches Python's official math.ceil() on every input.
Run the file directly to try it interactively, or import celing()
from your own code. See test_celing.py for an accuracy test.
"""

# Lookup table: each digit mapped to the next one.
# "9" maps to "0", which tells the code a carry is needed.
INCREMENT = {
    "0": "1",
    "1": "2",
    "2": "3",
    "3": "4",
    "4": "5",
    "5": "6",
    "6": "7",
    "7": "8",
    "8": "9",
    "9": "0",
}


def parse_input(num):
    """Check the input and split it into (whole, fraction) strings.

    Returns None if the input is not a valid number like "3.2" or "-10.5"
    (wrong number of dots, empty parts, or non-digit characters).
    """
    parts = num.split(".")
    if len(parts) != 2:
        return None
    whole, frac = parts
    digits = whole.lstrip("-")  # ignore a leading minus sign when checking
    if not digits or not digits.isdigit() or not frac.isdigit():
        return None
    return whole, frac


def is_whole_number(frac):
    """True if the fraction part is all zeros, e.g. "000" for "3.000"."""
    return set(frac) == {"0"}


def ceil_positive(whole, frac):
    """Ceiling of a positive number: increase the whole part by 1.

    The increase is done digit by digit with a carry: a "9" rolls over
    to "0" and the digit to its left is increased instead. If every
    digit is a "9", a leading "1" is added (99 -> 100).
    """
    if is_whole_number(frac):   # e.g. "3.0" is already whole, keep "3"
        return whole
    digits = list(whole)
    pos = len(digits) - 1
    while pos >= 0:
        if digits[pos] == "9":
            digits[pos] = "0"   # roll over and carry to the left
            pos -= 1
        else:
            digits[pos] = INCREMENT[digits[pos]]
            break
    else:
        digits.insert(0, "1")   # all digits were 9: 99 -> 100
    return "".join(digits)


def ceil_negative(whole, frac):
    """Ceiling of a negative number: keep the whole part unchanged.

    Ceiling always moves toward zero, so for a negative number like
    -3.2 the answer is -3. Whole numbers like -5.0 also stay as they are.
    """
    return whole


def celing(num):
    """Return the ceiling of a number given as a string, as a string.

    Example: celing("3.2") returns "4". Invalid input returns "try again".
    This is the function to import from other code.
    """
    parts = parse_input(num)
    if parts is None:
        return "try again"
    whole, frac = parts
    if whole.startswith("-"):
        return ceil_negative(whole, frac)
    return ceil_positive(whole, frac)


def main():
    """Run the program: keep asking for a number and print its ceiling."""
    while True:
        num = input("enter the number: ")
        print(celing(num))


if __name__ == "__main__":
    main()
