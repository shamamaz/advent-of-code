from aocd import data

def a(data):
  len_str = [-1, 0]
  str0 = data
  while len_str[-1] != len_str[-2]:
    strs = set(data.lower())
    for x in strs:
      str0 = str0.replace(x.upper() + x, '').replace(x + x.upper(), '')
    len_str.append(len(str0))
  return len(str0)

def b(data):
  result = len(data)
  for x in list(map(chr, range(97, 123))):
    m = a(data.replace(x, '').replace(x.upper(), ''))
    result = min(m, result)
  return result

print(a(data))  # 10762
print(b(data))  # 6946
