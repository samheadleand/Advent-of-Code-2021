with open('input.csv') as f:
  data = [int(j) for j in [i.strip().split(',') for i in f][0]]

min_max = (min(data), max(data))
avg = int(sum(data)/len(data))

def crabulate_linear_total_diff(data, value):
  return sum([abs(i-value) for i in data])

def crabulate_triangle_total_diff(data, value):
  return sum([((abs(i - value)+1) * (abs(i - value)))/2 for i in data])    

min_diff = 9999999999
for i in range(min_max[0], min_max[1]):
  total_diff = crabulate_linear_total_diff(data, i)
  if min_diff < total_diff:
    break
  else:
    min_diff = total_diff
print(min_diff)

min_diff = 9999999999
for i in range(min_max[0], min_max[1]):
  total_diff = crabulate_triangle_total_diff(data, i)
  min_diff = min(min_diff, total_diff)
print(min_diff)

