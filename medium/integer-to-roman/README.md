# 12. Integer to Roman

**Difficulty:** Medium

## Problem Description
Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

1. If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
2. If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example:
   - 4 is 1 (I) less than 5 (V): `IV`
   - 9 is 1 (I) less than 10 (X): `IX`
   - 40 is 10 (X) less than 50 (L): `XL`
   - 90 is 10 (X) less than 100 (C): `XC`
   - 400 is 100 (C) less than 500 (D): `CD`
   - 900 is 100 (C) less than 1000 (M): `CM`
3. Only powers of 10 (`I`, `X`, `C`, `M`) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (`V`), 50 (`L`), or 500 (`D`) multiple times. If you need to append a symbol 4 times use the subtractive form.

Given an integer, convert it to a Roman numeral.

## Examples

### Example 1
```
Input: num = 3749
Output: "MMMDCCXLIX"
```

### Example 2
```
Input: num = 58
Output: "LVIII"
```

### Example 3
```
Input: num = 1994
Output: "MCMXCIV"
```

## Constraints
- `1 <= num <= 3999`

## Approach
We use a **greedy** approach based on a fixed table of Roman symbols and their values, including the subtractive forms:

```text
I(1), IV(4), V(5), IX(9), X(10), XL(40), L(50),
XC(90), C(100), CD(400), D(500), CM(900), M(1000)
```

Algorithm:
1. Create an ordered list of pairs `(symbol, value)` from smallest to largest, including subtractive forms.
2. Iterate over this list in **reverse** (from largest value to smallest).
3. For each `(roman, val)`:
   - Compute how many times `val` fits into `num`: `count = num // val`.
   - Append `roman * count` to the result string.
   - Update `num = num % val`.
4. Continue until `num` becomes 0.
5. Return the resulting string.

This respects all the Roman numeral construction rules by always taking the largest possible symbol (or subtractive pair) at each step.

## Time & Space Complexity
- **Time Complexity:** `O(1)` — the list of Roman symbols is fixed size, and each iteration does constant work.
- **Space Complexity:** `O(1)` extra space (excluding the output string).

