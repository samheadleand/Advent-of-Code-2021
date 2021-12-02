from operator import add

with open('input.csv') as f:
    data =[(x, int(y)) for x,y in [idx.strip().split(' ') for idx in f]]

# Part 1
change = {
  'forward': lambda a: [a,0],
  'down': lambda a: [0,a],
  'up': lambda a: [0,-a]
  }

coord = [0,0]
for i in data:
  coord = list(map(add, coord, change[i[0]](i[1])) )

print(coord[0] * coord[1])

# Part 2

change = {
  'forward': lambda a, coord: [
    coord[0] + a,
    coord[1] + (coord[2] * a),
    coord[2]
    ],
  'down': lambda a, coord: list(map(add, coord, [0,0,a])),
  'up': lambda a, coord: list(map(add, coord, [0,0,-a]))
  }

# [hor, depth, aim]
coord = [0,0,0]
for i in data:
  coord = change[i[0]](i[1], coord)

print(coord[0] * coord[1])
