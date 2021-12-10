with open('input.csv') as f:
  data = [i.strip() for i in f]

matching = {
  '(': ')', '[': ']', '{': '}', '<': '>',
  ')': '(', ']': '[', '}': '{', '>': '<'
  }
opening = ['(', '{', '<', '[']

def match_brackets(segment):
  spare_ikea_brackets = []
  for b in segment:
    if b in opening:
      spare_ikea_brackets.append(b)
    elif matching[b] != spare_ikea_brackets.pop():
      return {')':3, '}':1197, ']':57, '>':25137}[b]
  return spare_ikea_brackets

# Part 1
print(sum([
      match_brackets(i)
      if isinstance(match_brackets(i), int)
      else 0 for i in data
      ]))

def calc_line_score(line):
  score = 0
  for i in match_brackets(line)[::-1]:
    score *= 5
    score += {'(':1, '{':3, '[':2, '<':4}[i]
  return score

score = [
  calc_line_score(i) for i in data
  if isinstance(match_brackets(i), list)
  ]
score.sort()
print(score[int(len(score)/2)])