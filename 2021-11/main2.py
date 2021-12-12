from collections import OrderedDict

class Octo:
  def __init__(self, i, j, energy):
    self.i = i
    self.j = j
    self.normal_increase = False
    self.explosion_increase = False
    self.energy = energy
    self.lit_up_this_round = False
    self.max_height = len(data)
    self.max_width = len(data[0])
    self.adj_coords = list(self.find_adjacent_points())
  
  def test_invalid_points(self, coord):
    return (
      coord[0] in range(0, self.max_height) and
      coord[1] in range(0, self.max_width))

  def find_adjacent_points(self):
    coords = [
      (self.i+x, self.j+y)
      for x,y in [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]
    ]
    return filter(self.test_invalid_points, coords)
  
  def increase_energy(self,normal=True):
    self.energy += 1
    if normal:
      self.normal_increase = True
    else:
      self.explosion_increase = True

  
  def energy_to_zero(self):
    self.energy = 0
    self.lit_up_this_round = True


with open('test_input.csv') as f:
  data = [i.strip() for i in f]
  dict_of_octo = OrderedDict()
  for i in range(len(data)):
    for j in range(len(data[0])):
      dict_of_octo[(i, j)] = Octo(i, j, int(data[i][j]))


def oct_print():
  octs = []
  for i in range(len(data)):
    line = ''
    for j in range(len(data[0])):
      energy = str(dict_of_octo[(i, j)].energy)
      if len(energy) == 1:
        line += ' '
        line += energy
      else:
        line += energy
    octs.append(line)

  for i in octs:
    print(i)



def one_iteration():
  changed = True
  while changed:
    changed = False
    counter = 0
    for oct in dict_of_octo.values():
      if counter < 10:
        counter += 1
      else:
        return
      if not oct.normal_increase:
        oct.increase_energy()
      if oct.energy >= 9 and not oct.lit_up_this_round:
        oct.energy_to_zero()
        changed = True
        for adj in oct.adj_coords:
          if not dict_of_octo[adj].lit_up_this_round:
            dict_of_octo[adj].increase_energy(False)
      print(oct.i, oct.j)
      oct_print()
      print()
      
  for i in dict_of_octo.values():
    i.normal_increase=False
    i.explosion_increase=False
    i.lit_up_this_round=False
    oct.energy = min(oct.energy, 9)

one_iteration()
#one_iteration()
oct_print()



