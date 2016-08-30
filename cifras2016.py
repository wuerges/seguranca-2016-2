import argparse
import sys
import numpy
from itertools import zip_longest, chain, cycle
from math import ceil
from random import shuffle

#converts the k argument of a function to an int
def int_key(func):
    def w(k, d):
        return func(int(k), d)
    return w

#converts the k argument of a function to an array of ints
def word_key(func):
    def w(k, d):
        return func(k.encode(), d)
    return w

# functions for the ceasar cipher
def ceasar_enc(k, d):
    return bytes((x + k) % 256 for x in d)

def ceasar_dec(k, d):
    return ceasar_enc(k * -1, d)

# functinos for the transposition cipher

def transp_enc(k, d):
    m = [d[i:i+k] for i in range(0, len(d), k)]
    r = zip_longest(*m, fillvalue=0)
    return bytes(sum(r, ()))

def transp_dec(k, d):
    kd = ceil(len(d) / k)
    return transp_enc(kd, d)

# functions for the vigenere cipher

def vig_enc(k, d):
    return bytes((b + a) % 256 for (a, b) in zip(cycle(k), d))

def vig_dec(k, d):
    return vig_enc([-ki for ki in k], d)


# functions for substitution cipher

def generate_random_subs_key():
    l = list(range(256))
    shuffle(l)
    return dict(enumerate(l))

# WARNING: if it doesn't find the file, it will create a new one with a random key
def load_key(filename):
    try:
        with open(filename, 'rb') as f:
            k = f.read()
            return dict(enumerate(k))
    except FileNotFoundError:
        print("WARNING: file <%s> not found. I will create a new random key and store it in <%s>" % (filename, filename), file=sys.stderr)

        rk = generate_random_subs_key()
        store_key(filename, rk)
        return rk


def store_key(filename, k):
    with open(filename, 'wb') as f:
        f.write(bytes(k.values()))

def dict_key(func):
    def w(k, d):
        return func(load_key(k), d)
    return w

def subs_enc(k, d):
    return bytes((k[x] for x in d))

def reverse_subs_key(k):
    return dict(((b,a) for (a, b) in k.items()))

def subs_dec(k, d):
    return subs_enc(reverse_subs_key(k), d)


if __name__ == "__main__":
    ciphers = { \
            'ceasar': { 'e': int_key(ceasar_enc), 'd': int_key(ceasar_dec) },
            'transp': { 'e': int_key(transp_enc), 'd': int_key(transp_dec) },
            'vig'   : { 'e': word_key(vig_enc),   'd': word_key(vig_dec)   },
            'subs'  : { 'e': dict_key(subs_enc),  'd': dict_key(subs_dec)  }
            }

    parser = argparse.ArgumentParser()
    parser.add_argument("cipher")
    parser.add_argument("mode")
    parser.add_argument("key")
    args = parser.parse_args()

    d = sys.stdin.buffer.read()

    o = ciphers[args.cipher][args.mode](args.key, d)

    sys.stdout.buffer.write(o)


