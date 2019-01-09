import numpy as np


def noise(input):
    for i in range(len(input)):
        r = np.random.rand()
        if r < 0.1:
            #input[i] = 1 - input[i]
            if input[i] == '0':
                input[i] = '1'
            elif input[i] == '1':
                input[i] = '0'
    output = input
    return output

