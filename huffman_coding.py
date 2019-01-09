#!/usr/bin/python

import heapq
import heap
import copy


class HuffmanCoding:

    def __init__(self, frequency):
        self.minHeap = []
        self.frequency = frequency
        self.codes = {}
        self.reverse_mapping = {}
        #self.make_heap(frequency)

    def make_minheap(self, text):
        for key in text:
            heap_node = heap.HeapNode(key, self.frequency[key])
            #print("heap_node.get_char()", heap_node.get_char())
            heapq.heappush(self.minHeap, heap_node)

    def write_code(self, root, current_code):
        if root is None:
            return

        if root.get_char() != 'None':
            self.codes[root.get_char()] = current_code
            self.reverse_mapping[current_code] = root.get_char()
            return

        self.write_code(root.get_left(), current_code + "0")
        self.write_code(root.get_right(), current_code + "1")

    def check_input(self, text):
        if text.isalpha():
            for c in text:
                if not c.islower():
                    return False
            return True
        else:
            return False

    def encode(self, text):

        if self.check_input(text) == False:
            print("invalid input")
            return None
        self.make_minheap(text)

        while len(self.minHeap) > 1:
            node_left = heapq.heappop(self.minHeap)
            #print("node_left.get_freq()", node_left.get_freq())
            node_right = heapq.heappop(self.minHeap)

            merged = heap.HeapNode('None', node_left.get_freq() + node_right.get_freq())
            merged.set_left(node_left)
            merged.set_right(node_right)

            heapq.heappush(self.minHeap, merged)

        root = heapq.heappop(self.minHeap)
        current_code = ""
        self.write_code(root, current_code)

        encoded = ""
        for character in text:
            encoded += self.codes[character]
        return encoded

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text