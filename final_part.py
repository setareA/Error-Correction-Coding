#!/usr/bin/python

import huffman_coding
import convolutional_encoder
import viterbi_decoder
import scipy.io
import noise

def convert_mat_to_dictionary(size, mat):

    frequency = {}
    for i in range(size):
        frequency[chr(i+97)] = mat[i][0]
    return frequency


def main():
    freq = scipy.io.loadmat('freq.mat')['freq']
    frequency = convert_mat_to_dictionary(26, freq)

    huffman = huffman_coding.HuffmanCoding(frequency)
    output_of_huffman_coding = huffman.encode('setareaskari')

    c = convolutional_encoder.ConvolutionalEncoder(output_of_huffman_coding)
    output_of_convolutional_encoder = c.encode()

    #### noise
    out_noise = noise.noise(list(output_of_convolutional_encoder))

    vd = viterbi_decoder.ViterbiDecoder()
    str1 = ''.join(out_noise)
    output_of_viterbi_decoder = vd.decode(str1)

    output_of_huffman_decoder = huffman.decode_text(output_of_viterbi_decoder)
    print(output_of_huffman_decoder)



if __name__ == "__main__":
    main()

