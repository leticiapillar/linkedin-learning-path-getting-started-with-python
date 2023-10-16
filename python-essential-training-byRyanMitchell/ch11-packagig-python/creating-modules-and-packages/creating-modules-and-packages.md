# 02 Creating Modules and Packages

- Primes module
```bash
❯ python useModule.py
primes.py module name is primes
--- Use module primes ---
Number 5 is prime? True
List primes 0 to 100: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


❯ python usePackage.py
name in __init__.py is numbers
--- Use Package numbers ---
[1, 2, 4, 5, 10, 20, 25, 50, 100]


❯ python usePackage.py
name in __init__.py is numbers
name in factors.py is numbers.factors
--- Use Package numbers ---
[1, 2, 4, 5, 10, 20, 25, 50, 100]


❯ python primes.py
primes.py module name is __main__
This is a module. please import using:
import primes

```