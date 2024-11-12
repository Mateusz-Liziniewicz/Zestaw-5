from math import gcd

def simplify(frac):
    num, den = frac
    if den == 0:
        raise ValueError("Błąd: dzielenie przez 0.")
    divisor = gcd(abs(num), abs(den))
    num //= divisor
    den //= divisor
    if den < 0:
        num = -num
        den = -den
    return [num, den]

def add_frac(frac1, frac2):
    num = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    return simplify([num, den])

def sub_frac(frac1, frac2):
    num = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    return simplify([num, den])

def mul_frac(frac1, frac2):
    num = frac1[0] * frac2[0]
    den = frac1[1] * frac2[1]
    return simplify([num, den])

def div_frac(frac1, frac2):
    if frac2[0] == 0:
        raise ValueError("Błąd: dzielenie przez 0.")
    num = frac1[0] * frac2[1]
    den = frac1[1] * frac2[0]
    return simplify([num, den])

def is_positive(frac):
    num, den = simplify(frac)
    return num > 0

def is_zero(frac):
    num, _ = simplify(frac)
    return num == 0

def cmp_frac(frac1, frac2):
    diff = sub_frac(frac1, frac2)
    if diff[0] > 0:
        return 1
    elif diff[0] < 0:
        return -1
    return 0

def frac2float(frac):
    return frac[0] / frac[1]
