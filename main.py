from requests import get
import csv


def album_search(artist, song):
    url_song = f"https://itunes.apple.com/search?term={artist}&attribute=artistTerm&entity=song&limit=300"
    result = get(url_song).json()
    try:
        if result != []:
            for row in result["results"]:
                if row['artistName'] == artist and row['trackName'] == song:
                    print(f"Ваш альбом - {row['collectionName']}")
                    return row["collectionId"]

    except Exception as ex:
        print(ex)
        return


def song_search(album, artist):
    lst_song = []
    url_album = f"https://itunes.apple.com/lookup?id={album}&entity=song"  
    result = get(url_album).json()
    if result != []:
        for row in result["results"]:
            if row['artistName'] == artist:
                if "trackName" in row:
                    lst_song.append([f'Артист - {row["artistName"]}, Альбом - {row["collectionName"]}, песня - {row["trackName"]}'])
        return lst_song
    else:
        print(f'Что то пошло не так...')
        return


def write_data(lst_song):
    with open("song.csv", "w", newline = '') as f:
        writer=csv.writer(f)
        writer.writerows(lst_song)
        print('Данные сохранены в song.csv')


if __name__ == '__main__':
    artist = input("Введите название группы: ")
    song = input("Введите название песни: ")

    album = album_search(artist, song)

    if album:
        lst_song = song_search(album, artist)
        if lst_song:
            write_data(lst_song)
        else:
            print("Все плохо")
    else:
        print('Ни чего не найдено!')
