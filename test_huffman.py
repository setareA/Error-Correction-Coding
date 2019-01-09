#!/usr/bin/python

import scipy.io
import huffman_coding


def convert_mat_to_dictionary(size, mat):

    frequency = {}
    for i in range(size):
        frequency[chr(i+97)] = mat[i][0]
    return frequency


def main():
    mat = scipy.io.loadmat('freq.mat')
    freq = mat['freq']
    frequency = convert_mat_to_dictionary(26, freq)

    huffman = huffman_coding.HuffmanCoding(frequency)
    input_string = input()
    encoded = huffman.encode(input_string)
    print(encoded)
    if encoded is not None:
        decoded = huffman.decode_text(encoded)
        print(decoded)


if __name__ == "__main__":
    main()
