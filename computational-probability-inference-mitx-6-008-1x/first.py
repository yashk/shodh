#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:12:05 2018

@author: ykochare
"""
import comp_prob_inference

flips = comp_prob_inference.flip_fair_coins(100)
# print(flips)
comp_prob_inference.plot_discrete_histogram(flips)


n = 10000
heads_so_far = 0
fraction_of_heads = []
for i in range(n):
    if comp_prob_inference.flip_fair_coin() == 'heads':
        heads_so_far += 1
    fraction_of_heads.append(heads_so_far / (i+1))


import matplotlib.pyplot as plt


plt.figure(figsize=(8, 4))
plt.xscale('log')
plt.plot(range(1, n+1), fraction_of_heads)
plt.xlabel('Number of flips')
plt.ylabel('Fraction of heads')


model = {'heads':1/2,'tails':1/2}
sample_space=set(model.keys())

print(set(model.keys()))
