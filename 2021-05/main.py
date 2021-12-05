with open('input.csv') as f:
  data = [i.strip().split(' -> ') for i in f]
  data = [[x.split(','), y.split(',')] for x,y in data]
  data = [[[int(x), int(y)] for x,y in i] for i in data]

def check_if_not_diagonal(coords):
  one, two = coords
  if one[0] == two[0] or one[1] == two[1]:
    return True
  else:
    return False

def find_change_coord_in_line(coords):
  start, finish = coords
  x_inc = finish[0] - start[0]
  y_inc = finish[1] - start[1]
  return [
    int(x_inc/abs(x_inc)) if x_inc != 0 else 0,
    int(y_inc/abs(y_inc)) if y_inc != 0 else 0
  ]

def find_coords_in_line(coords):
  start, finish = coords
  change_coord = find_change_coord_in_line(coords)
  coords_in_line = [start]
  current_coord = start
  while current_coord != finish:
    current_coord = [a + b for a, b in zip(current_coord, change_coord)]
    coords_in_line.append(current_coord)
  return coords_in_line

def find_vent_coord(data, consider_diagonals=False):
  vent_coords = {}
  multiple_lines = set()
  for i in data:
    if check_if_not_diagonal(i) or consider_diagonals:
      coords = find_coords_in_line(i)
      for j in coords:
        if tuple(j) in vent_coords:
          vent_coords[tuple(j)] += 1
          multiple_lines.add(tuple(j))
        else:
          vent_coords[tuple(j)] = 1
  return vent_coords, multiple_lines

vent_coords, multiple_lines = find_vent_coord(data)
print(len(multiple_lines))

vent_coords, multiple_lines = find_vent_coord(data, True)
print(len(multiple_lines))
