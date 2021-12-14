with open('input.csv') as f:
  data = [i.strip() for i in f]

pair_ins = {i[:2]:i[-1] for i in data[2:]}

polymer = {i[:2]:0 for i in data[2:]}
for i, char in enumerate(data[0][:-1]):
  polymer[data[0][i:i+2]] += 1

def insert(polymer, pairs):
  new_polymer = polymer.copy()
  for i in polymer:
    new_polymer[i[0]+pair_ins[i]] += polymer[i]
    new_polymer[pair_ins[i]+i[1]] += polymer[i]
    new_polymer[i] -= polymer[i]
  return new_polymer

for i in range(40):
  polymer = insert(polymer, pair_ins)

letter_count = {data[0][-1]:1}
for i in polymer:
  if i[0] in letter_count:
    letter_count[i[0]] += polymer[i]
  else:
    letter_count[i[0]] = polymer[i]

print(max(letter_count.values()) - min(letter_count.values()))