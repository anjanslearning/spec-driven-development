# spec-driven-development

This repository contains a simple Python implementation for summing prime numbers in a range.

## KAN-5: AI Practise

Implemented `src/primesum.py` with the following behavior:
- `solve(n, k)` returns the sum of all prime numbers in the inclusive range `[n, k]`
- Accepts swapped bounds (`n > k`) by normalizing the range
- Supports command-line execution with `OUTPUT_PATH` or a default `output.txt`

## How to run

```bash
python src/primesum.py
```

Provide input in the following format:

```
t
n k
...
```

Example:

```
2
2 10
3 5
```

## Testing

Run the unit tests with:

```bash
python -m unittest discover -s tests
```
