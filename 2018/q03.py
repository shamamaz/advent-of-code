from aocd import data

def helper(data):
  multiple = 0
  multiple_claim_ids = set()
  all_ids = set()
  grid = {}
  for line in data.split('\n'):
    claim_id, at, claim, dim = line.split(' ')
    all_ids.add(claim_id)
    x, y = map(int, claim.rstrip(':').split(','))
    w, h = map(int, dim.split('x'))
    for i in range(x, x + w):
      for j in range(y, y + h):
        pt = (i,j)
        if pt in grid:
          grid[pt].append(claim_id)
          if len(grid[pt]) == 2:
            multiple +=1
          multiple_claim_ids.update(grid[pt])
        else:
          grid[pt] = [claim_id]

  return multiple, (all_ids-multiple_claim_ids)

def a(data):
  return helper(data)[0]

def b(data):
  return helper(data)[1]

print(a(data)) #110389
print(b(data)) #552
