# String Ceiling 🧮

A ceiling function that **never converts your input to a number**. It takes
something like `"99.5"` as a string and returns `"100"` — computed one
character at a time.

## Why?

Python already has `math.ceil()`. This project isn't trying to replace it.

I built this because the problem itself is interesting: **what does
"rounding up" actually look like at the digit level?** Turns out it looks
like the carry you learned in school — a `9` rolls over to a `0` and bumps
the digit to its left (`99 + 1 = 100`). Doing that by hand, on strings, is
a fun way to make that mechanism explicit.

So yes, this is a learning/experiment project — a deliberately "wrong-tool"
solution, done for the joy of seeing how it works under the hood. And to
prove it's not just toy code, it ships with a test that checks it against
`math.ceil()` itself.

## How it works

1. Split the input on `"."` into a whole part and a fraction part.
2. If the fraction is all zeros (`"3.0"`), the number is already whole —
   return it unchanged.
3. Otherwise drop the fraction and round the whole part **up**:
   - **Positive** (`"99.5"` → `"100"`): add 1 to the last digit, carrying
     left through any `9`s, and prepend a `1` if every digit rolled over.
   - **Negative** (`"-3.2"` → `"-3"`): ceiling moves toward zero, so the
     whole part is simply kept as it is.

Result: identical to `math.ceil()` on every input tested.

## Usage

```bash
python celing.py
```

```
enter the number: 3.2
4
enter the number: -10.5
-10
enter the number: oops
try again
```

Or import it in your own code:

```python
from celing import celing

celing("99.5")   # returns "100"
```

## Testing

```bash
python test_celing.py
```

Generates 1,000 random positive and 1,000 random negative numbers
(1–2 decimal places) and compares each answer with `math.ceil()`:

```
numbers tested per sign : 1000
positive -- incorrect   : 0
negative -- incorrect   : 0
```

## Project structure

```
string-ceiling/
├── celing.py        # the string-based ceiling function + interactive mode
├── test_celing.py   # accuracy test against math.ceil()
└── README.md
```

## Honest note

If you need a ceiling in real code, use `math.ceil()`. This repo exists
because doing it the hard way — digit by digit, on strings — is a genuinely
neat puzzle, and because writing the carry logic by hand teaches you what
the built-in function is doing for you.

## License

MIT — do whatever you like with it.
