with open('input.csv') as f:
  data = []
  for i in f:
    j = [h.split(' ') for h in i.strip().split(' | ')]
    j = [list(map(lambda a: set(a), k)) for k in j]
    data.append(j)

# Part 1
print(
  sum(
    [1 for i in data for j in i[1] if len(j) in [2,3,4,7]]
  )
)

# Part 2
def calculate(data_item):
  number_sets = {}

  for i in data_item[0]:
    if len(i) == 2:
      number_sets[1] = i
    elif len(i) == 3:
      number_sets[7] = i
    elif len(i) == 4:
      number_sets[4] = i
    elif len(i) == 7:
      number_sets[8] = i
  
  six_segment = [i for i in data_item[0] if len(i) == 6]

  five_segment = [i for i in data_item[0] if len(i) == 5]
  
  # 6
  for i in six_segment:
    diff = number_sets[1] - i
    if len(diff) == 1:
      number_sets[6] = i
      six_segment.remove(i)

  # 3
  for i in five_segment:
    diff = number_sets[1] - i
    if len(diff) == 0:
      number_sets[3] = i
      five_segment.remove(i)
  
  # 0 & 9
  for i in six_segment:
    diff = number_sets[8] - number_sets[3] - i
    if len(diff) == 1:
      number_sets[9] = i
    else:
      number_sets[0] = i

  # 2 & 5
  for i in five_segment:
    diff = number_sets[4] - i
    if len(diff) == 1:
      number_sets[5] = i
    else:
      number_sets[2] = i

  return number_sets

def calculate_line_total(line):
  data_item = calculate(line)
  data_list = [data_item[i] for i in range(10)]
  return int(
    ''.join([str(data_list.index(i)) for i in line[1]])
    )

print(sum([calculate_line_total(i) for i in data]))