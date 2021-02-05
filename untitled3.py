# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:47:51 2021

@author: Administer
"""

from math import sqrt
def is_prime(n):
    root = round(sqrt(n)) + 1
    for trial_factor in range(2, root):
        if n % trial_factor == 0:
            return False
    return True


prime_exponent = []
for p in range(3,66):
    if is_prime(p):
        prime_exponent.append(p)
        
print(prime_exponent)


def lucas():
    ll_seq = [4]
    zero_or_one = []
    if p > 2:
        for i in prime_exponent:
            print(i)
            n_i = ((ll_seq[i-1]) ** 2 -2) % ((2 ** p) - 1)
            ll_seq.append(n_i)
            
            for x in ll_seq:
                if ll_seq[-1] == 0:
                    zero_or_one(0)
                else:
                    zero_or_one(0)
