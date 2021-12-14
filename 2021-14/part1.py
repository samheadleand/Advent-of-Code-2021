from collections import Counter

with open('input.csv') as f:
  data = [i.strip() for i in f]


polymer = data[0]
pair_ins = {i[:2]:i[-1] for i in data[2:]}


def insert(polymer, pairs):
  inserted = 0
  new_polymer = polymer
  for i, character in enumerate(polymer):
    if polymer[i:i+2] in pair_ins:
      new_polymer = new_polymer[:i+inserted+1] + pair_ins[polymer[i:i+2]] + new_polymer[i+inserted+1:]
      inserted += 1
  return new_polymer


for i in range(10):
  polymer = insert(polymer, pair_ins)

counter = Counter(polymer)

print(max(counter.values()) - min(counter.values()))
