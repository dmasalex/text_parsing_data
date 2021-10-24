from typing import Text
from requests import get


artist = input("Введите название группы: ")
song = input("Введите название песни: ")


def album_search(artist, song):
    url_song = f"https://itunes.apple.com/search?term={artist}&attribute=artistTerm&entity=song&limit=300"
    result = get(url_song).json()
    try:
        if result != []:
            for row in result["results"]:
                if row['artistName'] == artist and row['trackName'] == song:
                    print(f"Страница вашей песни - {row['trackViewUrl']}")
                    return row["trackViewUrl"]

    except Exception as ex:
        print(ex)
        return


#def parsing_page(url):
#    result = get(url)
#    text = result.text
#    for w in text:
#        if w == "chords" or w == 'text':
#            print(w)
    

def search_info(song, artist):
    url_song = f"https://itunes.apple.com/search?term={song}"
    result = get(url_song).json()
    text = ''
    try:
        if result != []:
            for row in result["results"]:
                if "description" in row and row['artistName'] == artist:
                    text += row['description']
            
            return text 

    except Exception as ex:
        print(ex)
        return

def write_data(lst_song):
    with open("text.txt", "w") as file:
        file.write(lst_song)


url = album_search(artist, song)
text = search_info(song, artist)
if text != '':
    write_data(text)
    print("Данные записаны в text.txt")
else:
    print("Данные не найдены")
    
