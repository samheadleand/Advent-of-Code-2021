#from itertools import combinations

with open('input.csv') as f:
  data = [idx.strip() for idx in f]

def format_bingo_cards(data):
  card = []
  player = 0
  players = {}
  numbers = set()
  for i in data:
    if i == '':
      players[player] = (card, numbers)
      card = []
      numbers = set()
      player += 1
    else:
      line = [x for x in i.split(' ')]
      line = [int(x) for x in (filter(lambda a: a != '', line))]
      card.append(line)
      numbers = numbers.union(set(line))
  players[player] = (card, numbers)
  return players


def win_cards_for_player(player, player_number):
  cards = player[0]
  rows = {}
  for i in cards:
    rows[tuple(i)] = player_number
  columns = {}
  for position in range(len(cards[0])):
    column = []
    for card in cards:
      column.append(card[position])
    columns[tuple(column)] = player_number
  return {**rows, **columns}


def all_possible_wins(players):
  win_cards = {}
  for i in players.keys():
    player_win_cards = win_cards_for_player(players[i], i)
    win_cards = {**win_cards, **player_win_cards}
  return win_cards


def calculate_winning_score(player_num, players, numbers_called):
  numbers_on_players_card = set(players[player_num][1])
  last_number = numbers_called[-1]
  remaining_numbers = numbers_on_players_card - set(numbers_called)
  return sum(list(remaining_numbers)) * last_number


def check_if_numbers_the_same(card, numbers):
  for i in card:
    if i not in numbers:
      return False
  return True


numbers = [int(i) for i in data[0].split(',')]
players = format_bingo_cards(data[2:])
winning_cards = all_possible_wins(players)

def answer(winning_cards, numbers, players, idx_to_start=4, players_to_skip=[]):
  for i,number in enumerate(numbers[idx_to_start:]):
    for row_or_column in winning_cards:
      if check_if_numbers_the_same(row_or_column, numbers[:i+idx_to_start]):
        player = winning_cards[row_or_column]
        if player not in players_to_skip:
          #print(player, players, numbers[:i+idx_to_start])
          return player, calculate_winning_score(player, players, numbers[:i+idx_to_start]), i

# Part 1
#print(answer(winning_cards, numbers, players))

# Part 2
players_to_skip = []
idx_to_start = 4

while len(players_to_skip) < len(players.keys()):
  player, winning_score, number_idx = answer(
    winning_cards,
    numbers,
    players,
    idx_to_start,
    players_to_skip
    )
  players_to_skip.append(player)
  idx_to_start = number_idx+1
  print(winning_score)
