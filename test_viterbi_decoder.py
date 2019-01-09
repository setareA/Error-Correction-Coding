#!/usr/bin/python

import viterbi_decoder


def main():

    vd = viterbi_decoder.ViterbiDecoder()
    print( vd.decode('111110'))

if __name__ == "__main__":
    main()

