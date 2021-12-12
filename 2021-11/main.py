with open('input.csv') as f:
  data = [i.strip() for i in f]
  dict_of_octo = {}
  for i in range(len(data)):
    for j in range(len(data[0])):
      dict_of_octo[(i, j)] = int(data[i][j])

def grow_energy(dict_of_octo):
  for oct in dict_of_octo:
    dict_of_octo[oct] += 1
  return dict_of_octo

def test_invalid_points(coord):
  return (
    coord[0] in range(len(data)) and
    coord[1] in range(len(data))
    )

def find_adjacent_points(coord):
  coords = [
    (coord[0]+x, coord[1]+y)
    for x,y in [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]
  ]
  return filter(test_invalid_points, coords)

def apply_explosion(dict_of_octo, coord):
  adj_points = find_adjacent_points(coord)
  for i in adj_points:
    dict_of_octo[i] += 1
  return dict_of_octo

def oct_print():
  octs = []
  for i in range(len(data)):
    line = ''
    for j in range(len(data[0])):
      energy = str(dict_of_octo[(i, j)])
      if len(energy) == 1:
        line += ' '
        line += energy
      else:
        line += energy
    octs.append(line)

  for i in octs:
    print(i)


oct_print()
print()

def apply_all_explosions(dict_of_octo):
  explosions = 0
  changed = True
  exploded = []
  while changed:
    changed = False
    for i in dict_of_octo:
      if dict_of_octo[i] > 9 and i not in exploded:
        dict_of_octo = apply_explosion(dict_of_octo, i)
        exploded.append(i)
        changed = True
        explosions += 1
  return dict_of_octo, explosions

def reset_exploded_octos(dict_of_octo):
  for i in dict_of_octo:
    dict_of_octo[i] = 0 if dict_of_octo[i] > 9 else dict_of_octo[i]
  return dict_of_octo

def apply_round(dict_of_octo):
  dict_of_octo = grow_energy(dict_of_octo)
  dict_of_octo, explosions = apply_all_explosions(dict_of_octo)
  dict_of_octo = reset_exploded_octos(dict_of_octo)
  return dict_of_octo, explosions

def check_all_flashing(dict_of_octo):
  for i in dict_of_octo.values():
    if i != 0:
      return False
  return True

explosions = 0
for i in range(1000):
  dict_of_octo, new_explosions = apply_round(dict_of_octo)
  explosions += new_explosions
  if check_all_flashing(dict_of_octo):
    print(i+1)
    break

oct_print()
#print()

#print(explosions)