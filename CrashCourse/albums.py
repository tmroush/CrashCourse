def make_album(artist_name, album_title, num_of_songs=None):
    """Return a dictionary with the artist name and album_title"""
    album = { 'name': artist_name, 'title': album_title}
    if num_of_songs:
        album['num_songs'] = num_of_songs
    return album

album1 = make_album("Kenny Rogers", "The Gambler")
album2 = make_album("Pink Floyd", "Dark Side of the Moon", 12)
album3 = make_album("Jordan Feliz", "Beloved")

print(album1)
print(album2)
print(album3)
