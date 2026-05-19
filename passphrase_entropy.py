import sys
from math import log2

EFF_SIZE = 7776

def calc_entropy(w,d):
    """
    w = number of words
    d = number of possible words in dictionary
    """
    return w*log2(d)

def get_word_count(p):
    return len(p.split("-"))

def main(n):
    print(f"Calculating entropy for EFF passphrase with {n} words")
    print(f"Based on EFF wordlist ({EFF_SIZE} words)")

    e_eff = calc_entropy(1,EFF_SIZE)
    e = calc_entropy(n,EFF_SIZE)

    print(f"{'EFF per-word entropy:':<25} {round(e_eff)}")
    print(f"{'Entropy:':<25} {round(e, 3)}")

if __name__ == "__main__":
    main(int(sys.argv[1]))
