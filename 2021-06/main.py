with open('input.csv') as f:
  data = [int(j) for j in [i.strip().split(',') for i in f][0]]

fish = {i:data.count(i) for i in range(9)}

def change_all_fish(dict_of_fish):
  new_timer_fish = {i:0 for i in range(9)}
  for i in dict_of_fish:
    new_timer_fish[i-1 if i else 6] += dict_of_fish[i]
  new_timer_fish[8] = dict_of_fish[0]
  return new_timer_fish

dict_of_fish = fish.copy()
for i in range(256):
  dict_of_fish = change_all_fish(dict_of_fish)

print(sum(dict_of_fish.values()))