#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:13:53 2020

@author: elisaluo
"""

import pandas as pd

out = open('good_defs.txt', 'w')

data = pd.read_csv('urbandict-word-defs.csv', error_bad_lines=False)


defs = data['definition']
words = data['word']

for index, row in data.iterrows():
    #get rid of bad entries
    if row["up_votes"] > row["down_votes"]*4:
        out.write(str(row["word"]))
        out.write(": ")
        out.write(str(row["definition"]))
        out.write("\n\n")
    
print("\n\n done")