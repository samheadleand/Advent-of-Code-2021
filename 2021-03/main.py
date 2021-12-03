with open('input.csv') as f:
  data = [idx.strip() for idx in f]

MAX = 0
MIN = 1

def calculate_column_max(lines, position):
  zero = 0
  for i in lines:
    if i[position] == '0':
      zero += 1
  one = len(lines) - zero
  return ('0', '1') if zero > one else ('1', '0')

# Part 1
gamma = ''
epsilon = ''
for i in range(len(data[0])):
  result = calculate_column_max(data, i)
  gamma += result[0]
  epsilon += result[1]

print(int(gamma, 2) * int(epsilon,2))

# Part 2
def reduce_list(lines, position, max_or_min):
  max_tuple = calculate_column_max(lines, position)
  return list(filter(lambda i: i[position] == max_tuple[max_or_min], lines))

def find_rating(lines, max_or_min):
  for i in range(len(lines[0])):
    if len(lines) == 1:
      break
    else:
      lines = reduce_list(lines, i, max_or_min)
  return lines[0]

print(int(find_rating(data, MAX), 2) * int(find_rating(data, MIN), 2))