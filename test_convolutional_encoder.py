#!/usr/bin/python

import convolutional_encoder


def main():

    c = convolutional_encoder.ConvolutionalEncoder(input())
    print(c.encode())

if __name__ == "__main__":
    main()

