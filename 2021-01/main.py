with open('input.csv') as f:
    data = [int(idx.strip()) for idx in f]

# Part 1
counter = 0
for i, item in enumerate(data[:-1]):
  if item < data[i+1]:
    counter += 1

print(counter)

# Part 2
counter = 0
for i, item in enumerate(data[:-3]):
  if sum(data[i:i+3]) < sum(data[i+1:i+4]):
    counter += 1

print(counter)