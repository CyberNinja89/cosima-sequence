#!/usr/bin/env python3

import argparse


# Terminal Colors
GREEN = '\x1B[32m'
END = '\x1B[0m'


def decypher(g, b):
    final = ""
    if g:
        seq = input(GREEN+'Enter Your Genetic Sequence: '+END)
        final = ascii(binary(seq))
    if b:
        seq = input(GREEN+'Enter Your Binary Sequence: '+END).strip().replace(" ", "")
        final = ascii(seq)
    print(GREEN+final+END)


def binary(sequence):
    conv = ""
    for base in sequence:
        if base.upper() in ['C', 'G']:
            conv += "0"
        if base.upper() in ['A', 'T']:
            conv += "1"
    return conv


def ascii(binary):
    try:
        binary = int(binary, 2)
        return str(binary.to_bytes((binary.bit_length() + 7) // 8, 'big').decode()).upper()
    except:
        print("decoder.py: error: invalid binary")
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cosima's Genome Decryption")
    parser.add_argument('-b', '--binary', help="Convert Binary Sequence to ASCII", action="store_true")
    parser.add_argument('-g', '--genome', help="Convert Human Base Pairs to ASCII", action="store_true")
    args = parser.parse_args()

    decypher(args.genome, args.binary)
