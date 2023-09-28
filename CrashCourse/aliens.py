# creating a list of dictionaries

# first, make an empty list for storing aliens
aliens = []

# now we will make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# CHanging up the first 3 aliens:
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print(". . .")

# show the total number of aliens:
print(f"Total number of aliens: {len(aliens)}")
