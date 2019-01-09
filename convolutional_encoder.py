#!/usr/bin/python


class ConvolutionalEncoder:

    def __init__(self, text):
        self.current_state = '00'
        #self.encode(text)
        self.text = text

    def encode(self):

        encoded_text = ""
        for c in self.text:
            if self.current_state == '00':
                encoded_text += self.state_00(c)
            elif self.current_state == '10':
                encoded_text += self.state_10(c)
            elif self.current_state == '11':
                encoded_text += self.state_11(c)
            elif self.current_state == '01':
                encoded_text += self.state_01(c)
        return encoded_text

    def state_00(self, input):
        if input == '1':
            self.current_state = '10'
            return '11'
        elif input == '0':
            self.current_state = '00'
            return '00'

    def state_10(self, input):
        if input == '1':
            self.current_state = '11'
            return '00'
        elif input == '0':
            self.current_state = '01'
            return '11'

    def state_11(self, input):
        if input == '1':
            self.current_state = '11'
            return '10'
        elif input == '0':
            self.current_state = '01'
            return '01'

    def state_01(self, input):
        if input == '1':
            self.current_state = '10'
            return '01'
        elif input == '0':
            self.current_state = '00'
            return '10'

