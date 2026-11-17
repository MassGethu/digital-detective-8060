# Mission 5 — Numbers and data

## 1. Task / objective

Work out conversions by hand, confirm them with Python, build a converter and explain encoding.

## 2. Work completed

### Task 5.1 — Manual conversions

| Question | Working and answer |
| --- | --- |
| Decimal 13 to binary | 13 = 8 + 4 + 1, so the 8, 4, 2, 1 positions give **1101₂**. |
| Decimal 25 to binary | 25 = 16 + 8 + 1, so the 16, 8, 4, 2, 1 positions give **11001₂**. |
| Binary 1010 to decimal | 1×8 + 0×4 + 1×2 + 0×1 = **10**. |
| Binary 1101 to decimal | 1×8 + 1×4 + 0×2 + 1×1 = **13**. |
| Hexadecimal A to decimal | A is the digit for 10, so A×16⁰ = **10**. |
| Hexadecimal 1F to decimal | 1×16 + 15×1 = **31**. |
| Binary 1111 to hexadecimal | 8 + 4 + 2 + 1 = 15, which is the single hex digit **F**. |

### Task 5.2 — Verification with Python

| Expression | Observed result | Matches manual result |
| --- | --- | --- |
| `bin(13)` | `0b1101` | Yes |
| `bin(25)` | `0b11001` | Yes |
| `int("1010", 2)` | `10` | Yes |
| `int("1101", 2)` | `13` | Yes |
| `int("A", 16)` | `10` | Yes |
| `int("1F", 16)` | `31` | Yes |
| `hex(int("1111", 2))` | `0xf` | Yes |
| `hex(25)` | `0x19` | Yes |

For the extra decimal-to-hexadecimal check, 25 = 1×16 + 9. Python’s `0x19` is hexadecimal 19. The prefixes `0b` and `0x` identify the base.

### Task 5.3 — Number converter

Run `python3 number_converter.py` from this mission folder. `input()` reads the text and `int(..., 10)` interprets it as a decimal integer. Then `bin()` and `hex()` produce strings in base 2 and base 16, which `print()` displays. Invalid integer input produces a short message.

| Test number | Binary output | Hexadecimal output |
| --- | --- | --- |
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 31 | `0b11111` | `0x1f` |

Zero, a negative integer and invalid text were also exercised.

### Task 5.4 — Text encoding

Uppercase **A** has ASCII decimal code **65** and lowercase **a** has code **97**. The two values were checked with Python’s `ord()`. An encoding gives software an agreed way to map characters to stored bytes so the original text can be read back correctly. The character **é** is outside basic ASCII and can be represented using UTF-8.

## 3. Commands / tools used

`python3` evaluated the conversion expressions and ran the converter. `input()`, `int()`, `bin()`, `hex()`, `ord()` and `print()` read input, interpreted or represented data, and displayed results.

## 4. My understanding

The base determines the weight of each place. Four binary digits can be written as a single hex digit. Encodings give bytes an agreed interpretation as text.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[number_converter.py](number_converter.py), the manual working, and both result tables.

## 8. Commit details

Commit message: `Build number converter and practise data representation`. See the repository’s commit history for this checkpoint.
