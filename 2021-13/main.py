with open('input.csv') as f:
  data = [i.strip().split(',') for i in f]

coords = set([
  (int(i[0]), int(i[1]))
  for i in data[:data.index([''])]
])

folds = [
  (0 if 'x' in i[0] else 1,
  int(i[0][i[0].find('=')+1:]))
  for i in data[data.index(['']) + 1:]
]

def new_coord(coord, direction, fold):
  n_coord = list(coord)
  n_coord[direction] = min(
    (2 * fold) - coord[direction],
    coord[direction]
    )
  return tuple(n_coord)

def do_fold(coords, fold_inst):
  return set(
    new_coord(coord, *fold_inst) for coord in list(coords)
  )

for i in folds:
  coords = do_fold(coords, i)

def create_list(length):
  return [[' '] * length]

length=40
dots = [create_list(length) for i in range(length)]


for i in coords:
  dots[i[1]][0][i[0]] = '#'

for i in dots:
  print(''.join(i[0]))