import sys, re
from math import log2

# https://github.com/hoxxep/passwordentropy.com/blob/master/src/lib/calculations.ts

CHARSET_SIZES = {
    "lower": 26,
    "upper": 26,
    "digit": 10,
    "symbols": 10  # Assumption
}

def calc_entropy(l,r):
    return l*log2(r)

def get_pool_info(p):
    has_lower = re.search("[a-z]", p)
    has_upper = re.search("[A-Z]", p)
    has_digit = re.search("[0-9]", p)
    has_symbols = re.search("[^a-zA-Z0-9]", p)

    pool_names = set()
    charset_size = 0
    if has_lower:
        charset_size += CHARSET_SIZES["lower"]
        pool_names.add("lowercase")
    if has_upper:
        charset_size += CHARSET_SIZES["upper"]
        pool_names.add("uppercase")
    if has_digit:
        charset_size += CHARSET_SIZES["digit"]
        pool_names.add("numbers")
    if has_symbols:
        charset_size += CHARSET_SIZES["symbols"]
        pool_names.add("symbols")

    if pool_names == {"numbers"}:
        name = "numeric"
    elif pool_names == {"lowercase", "uppercase"}:
        name = "mixed case letters"
    elif pool_names == {"lowercase", "uppercase", "numbers"}:
        name = "alphanumeric"
    elif pool_names == {"lowercase", "uppercase", "numbers", "symbols"}:
        name = "alphanumeric + symbols"
    else:
        name = " + ".join(pool_names) if pool_names else "empty"

    return charset_size, name

def main(p):
    print(f"Calculating entropy for password '{p}'")

    l = len(p)
    r,n = get_pool_info(p)
    e = calc_entropy(l,r)

    print(f"{'Password length:':<20} {l}")
    print(f"{'Charset pool size:':<20} {r} ({n})")
    print(f"{'Entropy:':<20} {round(e, 3)}")

if __name__ == "__main__":
    main(sys.argv[1])
