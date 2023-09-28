players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('Original players list')
print(players)
print('\nplayers[0:3]')
print(players[0:3])
print('\nplayers[1:4]')
print(players[1:4])
print('\nEvery other player:')
print(players[0::2])

print('\nHere are the first 3 players on my team:')
for player in players[:3]:
    print(player.title())
