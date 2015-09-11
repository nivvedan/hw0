# COMS W4111 Introduction to Databases - Fall 2015
# Homework 0

# Work of Nivvedan Senthamil Selvan (ns2984)

import re

with open('iowa-liquor-sample.csv') as f:
  counter = 0
  for line in f:
    if re.search('single malt scotch', line, re.IGNORECASE):
      counter += 1
  print counter
