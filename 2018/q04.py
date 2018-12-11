from aocd import data
import operator
from collections import Counter

def a(data):
  minutes_asleep, total_sleep = helper(data)
  slept_most = max(total_sleep.iteritems(), key=operator.itemgetter(1))[0]
  return int(slept_most[1:]) * Counter(minutes_asleep[slept_most]).most_common(1)[0][0]

def b(data):
  minutes_asleep, sleep_minutes = helper(data)
  most_slept_count = {}
  for key in sleep_minutes.keys():
    min_count = Counter(minutes_asleep[key]).most_common(1)[0]
    most_slept_count[min_count[1]] = ( min_count[0], key)
  most = max(most_slept_count, key=int)
  guard_no = most_slept_count[most][1]
  return int(guard_no[1:]) * most_slept_count[most][0]

def helper(data):
  times = data.split('\n')
  times.sort()
  total_sleep = {}
  minutes_asleep = {}
  for i in range(0, len(times)):
    splitted = times[i].split(' ')
    if '#' in times[i]:
      guard_no = splitted[3]
    elif 'wakes' in times[i]:
      min_asleep = range(int(times[i-1].split(' ')[1][3:5]), int(splitted[1][3:5]))
      time_slept = min_asleep[-1] - min_asleep[0]
      if guard_no in total_sleep.keys():
        total_sleep[guard_no] += time_slept
        minutes_asleep[guard_no] += min_asleep
      else:
        total_sleep[guard_no] = time_slept
        minutes_asleep[guard_no] = min_asleep
  return minutes_asleep, total_sleep
# print(a(data))
print(b(data))
