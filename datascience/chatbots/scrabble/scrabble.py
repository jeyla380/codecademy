letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
#print(letter_to_points)
letter_to_points[" "] = 0
#print(letter_to_points)

def score_word(word):
  point_total = 0

  for letter in word:
    if letter == word[-1]:
      print(letter)
    else:
      print(letter + " + ", end='')

  for letter in word:
    if letter == word[-1]:
      print(str(point_total))
    else:
      print(str(point_total) + " + ", end='')
    point_total += letter_to_points.get(letter, 0)
  print("")
  return point_total

#brownie_points = score_word("BROWNIE")
#print(brownie_points)


player_to_words = {
"player1": ['BLUE', 'TENNIS', 'EXIT'], 
"wordNerd": ['EARTH', 'EYES', 'MACHINE'], 
'Lexi Con': ['PENCIL', 'BELLY', 'HUSKY'], 
'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

player_to_points = {}

for player, words in player_to_words.items():
  #print(player + " + " + str(words))
  player_points = 0

  for word in words:
    player_points = score_word(word)

  player_to_points[player] = player_points

#print(player_to_points)
