#!/usr/bin/python

import copy

class ViterbiDecoder:
    def __init__(self):
        self.PM_prev = {'state_00': 0, 'state_01': float("inf"), 'state_10': float("inf"), 'state_11': float("inf")}
        self.PM_current = {}
        self.state_machine_in = {('state_00', 'state_00'): ('0','00'), ('state_00', 'state_10'): ('1','11'),
                              ('state_01', 'state_00'): ('0','10'), ('state_01', 'state_10'): ('1','01'),
                              ('state_10', 'state_01'): ('0','11'), ('state_10', 'state_11'): ('1','00'),
                              ('state_11', 'state_01'): ('0','01'), ('state_11', 'state_11'): ('1','10')}
        self.next_state = {'state_00':('state_00', 'state_10'),
                           'state_01': ('state_00', 'state_10'),
                           'state_10': ('state_01', 'state_11'),
                           'state_11': ('state_01', 'state_11')}

    def count_diff(self, seq1, seq2):
        return sum(1 for a, b in zip(seq1, seq2) if a != b)

    def find_min_state(self, PM):
        min = float("inf")
        for key in PM:
            if PM[key] < min:
                answer = key
                min = PM[key]
        return answer, min

    def calculate_PM(self, min_prev_state, pm, next_state1, next_state2, current_input):

        diff_pass1 = self.count_diff(self.state_machine_in[(min_prev_state,next_state1)][1] , current_input)
        if next_state1 in self.PM_current:
            if pm + diff_pass1 < self.PM_current[next_state1]:
                self.PM_current[next_state1] = pm + diff_pass1
        else:
            self.PM_current[next_state1] = pm + diff_pass1

        diff_pass2 = self.count_diff(self.state_machine_in[(min_prev_state, next_state2)][1], current_input)
        if next_state2 in self.PM_current:
            if pm + diff_pass2 < self.PM_current[next_state2]:
                self.PM_current[next_state2] = pm + diff_pass2
        else:
            self.PM_current[next_state2] = pm + diff_pass2

    def decode(self, input):
        if len(input) % 2 != 0:
            print("invalid input")
            return
        decoded_output =""
        while len(input) != 0:
            current_input = input[0:2]
            #print(current_input)
            input = input[2:]
            min_prev_state, pm = self.find_min_state(self.PM_prev)
            next_state = self.next_state[min_prev_state]
            next_state1 = next_state[0]
            next_state2 = next_state[1]
            self.calculate_PM(min_prev_state, pm, next_state1, next_state2, current_input)
            #print("self.current_PM", self.PM_current)
            min_current_state, pm = self.find_min_state(self.PM_current)

            decoded_output += self.state_machine_in[(min_prev_state, min_current_state)][0]
            #print(decoded_output)

            print("selected path :", min_prev_state, "----> ", min_current_state)

            self.PM_prev = copy.deepcopy(self.PM_current)
            self.PM_current = {}

            if len(input) == 0:
                print("last PM: ", pm)

        return decoded_output




