import argparse
import sys
import numpy
from itertools import zip_longest, chain, cycle
from math import ceil


def ceasar_enc(k, d):
    return bytes((x + int(k)) % 256 for x in d)

def ceasar_dec(k, d):
    return ceasar_enc(int(k) * - 1, d)

def transp_enc(k, d):
    ki = int(k)
    m = [d[i:i+ki] for i in range(0, len(d), ki)]
    r = zip_longest(*m, fillvalue=0)
    return bytes(sum(r, ()))

def transp_dec(k, d):
    ki = int(k)
    kd = ceil(len(d) / ki)
    return transp_enc(kd, d)

def vig_enc(k, d):
    return bytes((b + a) % 256 for (a, b) in zip(cycle(k.encode()), d))

def vig_dec(k, d):
    return bytes((b - a + 256) % 256 for (a, b) in zip(cycle(k.encode()), d))

ciphers = { \
        'ceasar': { 'e': ceasar_enc, 'd': ceasar_dec },
        'transp': { 'e': transp_enc, 'd': transp_dec },
        'vig': { 'e': vig_enc, 'd': vig_dec },
        }

parser = argparse.ArgumentParser()
parser.add_argument("cipher")
parser.add_argument("mode")
parser.add_argument("key")
args = parser.parse_args()

d = sys.stdin.buffer.read()

o = ciphers[args.cipher][args.mode](args.key, d)

sys.stdout.buffer.write(o)


