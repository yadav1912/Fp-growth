# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:19:08 2020

@author: HP
"""

import numpy as np
import pandas as pd
import pyfpgrowth

transactions = [[1, 2, 5],
                [2, 4],
                [2, 3],
                [1, 2, 4],
                [1, 3],
                [2, 3],
                [1, 3],
                [1, 2, 3, 5],
                [1, 2, 3]]


dataset = pd.read_csv('Market.csv', header = None)
transactions = []

for sublist in dataset.values.tolist():
    clean_sublist = [item for item in sublist if item is not np.nan]
    transactions.append(clean_sublist) 



patterns = pyfpgrowth.find_frequent_patterns(transactions, 2)

rules = pyfpgrowth.generate_association_rules(patterns, 0.7)