import string

with open('input.csv') as f:
  data = [i.strip().split('-') for i in f]

  joins = {
    **{i[0]:set() for i in data},
    **{i[1]:set() for i in data}
  }

  for i in data:
    joins[i[0]].add(i[1])
    joins[i[1]].add(i[0])

  joins = {
    cave:[join for join in joins[cave] if join != 'start']
    for cave in joins
    }

def check_small_caves(path):
  small_caves = [
    step for step in path
    if step[0] in string.ascii_lowercase
    ]
  return len(set(small_caves)) >= len(small_caves) - 1

def check_paths(paths=[['start']]):
  paths_iteration = paths[:]
  for path in paths_iteration:
    if path[-1] == 'end':
      break
    additional_steps = joins[path[-1]]
    additional_paths = []
    for step in additional_steps:
      if check_small_caves(path+[step]):
        additional_paths = additional_paths + check_paths([path+[step]])
    paths.remove(path)
    paths.extend(additional_paths)
  return paths

paths = check_paths()
print()

print(len(paths))