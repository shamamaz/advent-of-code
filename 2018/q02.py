from aocd import data
from collections import Counter
from itertools import combinations

def a(data):
  counters = [Counter(string) for string in data.split()]
  twos,threes = 0,0
  for counter in counters:
    print(counter)
    if 2 in counter.values():
      twos +=1
    if 3 in counter.values():
      threes +=1
  return twos*threes

def b(data):
    strings = data.split()
    for i in range(len(strings)):
      for j in range(i, len(strings)):
          diff = find_difference(strings[i], strings[j])
          if (len(diff) == 1):
            print(strings[i])
            return strings[i].replace(diff, '')

def find_difference(string_a, string_b):
  diff = ''
  for i in range(len(string_a)):
    if (not (string_b[i] == string_a[i])):
      diff = diff + string_a[i]
  return diff

print(b(data))

