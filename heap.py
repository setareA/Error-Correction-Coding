#!/usr/bin/python

#just checking how pull request works
class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            if other is None:
                return False
            if not isinstance(other, HeapNode):
                return False
            return self.freq == other.freq

        def get_freq(self):
            return self.freq

        def get_char(self):
            return self.char

        def get_right(self):
            return self.right

        def get_left(self):
            return self.left

        def set_right(self, r):
            self.right = r

        def set_left(self, l):
            self.left = l
