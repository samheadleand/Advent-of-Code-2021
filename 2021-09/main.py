from itertools import permutations

with open('test_input.csv') as f:
  data = [i.strip() for i in f]

max_height = len(data)
max_width = len(data[0])

# Part 1
def test_invalid_points(coord):
  return (
    coord[0] in range(0, max_height) and
    coord[1] in range(0, max_width))

def find_adjacent_points(coord):
  coords = [
    (coord[0]+i, coord[1]+j)
    for i,j in [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ]
  return filter(test_invalid_points, coords)

def find_local_minima(coord):
  adj_coords = find_adjacent_points(coord)
  local_depth = data[coord[0]][coord[1]]
  adj_depths = [data[i[0]][i[1]] for i in adj_coords]
  return local_depth, local_depth < min(adj_depths)

local_minimas = []

local_minimas = 0
for i in range(len(data)):
  for j in range(len(data[0])):
    minima = find_local_minima([i,j])
    if minima[1]:
      local_minimas += int(minima[0]) + 1


# Part 2
def non_nine_coords(coord):
  adj_coords = find_adjacent_points(coord)
  valid_adj_coords = [
    i
    for i in adj_coords
    if data[i[0]][i[1]] != '9'
    ]
  return valid_adj_coords


def find_basin(local_minimas):
  basin = set()
  basin.add(tuple(local_minimas))
  len_increase = True
  while len_increase:
    len_increase = 0
    for i in list(basin):
      valid_adj_points = non_nine_coords(i)
      for j in valid_adj_points:
        if tuple(j) not in basin:
          basin.add(tuple(j))
          len_increase += 1
  return basin

local_minimas = []
for i in range(len(data)):
  for j in range(len(data[0])):
    minima = find_local_minima([i,j])
    if minima[1]:
      local_minimas.append([i,j])

basins = []
for i in local_minimas:
  basins.append(find_basin(i))

ordered_basins = [len(i) for i in basins]
ordered_basins.sort()
print(ordered_basins[-3] * ordered_basins[-2] * ordered_basins[-1])