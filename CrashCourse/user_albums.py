def make_album(artist_name, album_title, num_of_songs=None):
    """Return a dictionary with the artist name and album_title"""
    album = { 'name': artist_name, 'title': album_title}
    if num_of_songs:
        album['num_songs'] = num_of_songs
    return album


while True:
    print("\nEnter an artists name and album title.")
    print("(enter q at any time to quit).")
    artist = input("Enter artist: ")
    if artist == 'q':
        break
    album_name= input("Enter album name: ")
    if album_name == 'q':
        break
    print("\nHere is your album: ")
    album = make_album(artist, album_name)
    print(album)
