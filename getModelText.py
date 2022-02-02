from lib2to3.pgen2 import token
import requests as r
import lyricsgenius as lg
from bs4 import BeautifulSoup as bs
import os

lyrics_token = os.getenv('GENIUS_TOKEN')

artists = ['JPEGMAFIA', 'Kendrick Lamar', 'Kanye West', 'David Bowie', 'Mac Miller', 'Billy Joel', 'Paul McCartney',
           'John Lennon', 'Queen', 'MF DOOM', 'Tyler, The Creator', 'Earl Sweatshirt', 'Radiohead', 'Frank Ocean',
           'Beyoncé', 'Lin-Manuel Miranda', 'Tears for Fears', 'George Michael', 'Eminem', 'Prince', 'Michael Jackson',
           'Jimi Hendrix', 'Fleetwood Mac', 'Simon & Garfunkel', 'Stevie Wonder', 'Elton John', 'Bruce Springsteen',
           'Bob Dylan', "Morrissey", "Peter Gabriel", "Phil Collins"]
info = []
genius = lg.Genius(lyrics_token)
# for artist in artists:
# info = genius.search_artist(artists[0], max_songs=3, sort='popularity')
artist = genius.search_artist('David Bowie', max_songs=1)
response = r.get(artist.get_lyrics())
# print(info)
# str = 'https://genius.com/{}-{}-lyrics'
# artistsURL = artists[:]
# artistsURL = [artist.replace(" ", "-") for artist in artistsURL]
# artistsURL = [artist.replace(",", "") for artist in artistsURL]
# print(artistsURL)

# for artist in artists:
#         artist = artist.replace(' ', '-')
#         print(artist)
#         artistsURL.append[artist]
#         print(artistsURL[artist])
# print(artistsURL)
