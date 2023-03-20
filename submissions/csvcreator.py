from requests import request
from urllib.parse import urlparse
import csv
import time

jikan_url = "https://api.jikan.moe/v4/"


def get_anime(anime_id: str):
    anime = request(method='get', url=f'{jikan_url}anime/{anime_id}/full').json()
    return anime


slotA = []
slotB = []
slotC = []


def main():
    with open('AnimeSoc Termly Anime Nomination Form (Responses) - Form responses 1.csv', newline='', encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV, None)
        for row in readCSV:
            row
            currentitem = 4

            while currentitem <= 16:
                if row[currentitem] == '':
                    break
                url = urlparse(row[currentitem + 1])
                anime_id = url.path.split('/')[2]
                anime = get_anime(anime_id)

                if row[currentitem + 2] == 'Slot A':
                    slotA.append([
                        row[currentitem],
                        anime['data']['url'],
                        str(row[currentitem + 3]).replace("'", "\'"),
                        anime['data']['images']['jpg']['image_url'],
                        anime['data']['synopsis'],
                        anime['data']['trailer']['url']
                    ])
                elif row[currentitem + 2] == 'Slot B':
                    slotB.append([
                        row[currentitem],
                        anime['data']['url'],
                        str(row[currentitem + 3]).replace("'", "\'"),
                        anime['data']['images']['jpg']['image_url'],
                        anime['data']['synopsis'],
                        anime['data']['trailer']['url']
                    ])
                elif row[currentitem + 2] == 'Slot C':
                    slotC.append([
                        row[currentitem],
                        anime['data']['url'],
                        str(row[currentitem + 3]).replace("'", "\'"),
                        anime['data']['images']['jpg']['image_url'],
                        anime['data']['synopsis'],
                        anime['data']['trailer']['url']
                    ])
                time.sleep(1)
                currentitem += 4

    with open('Slot A.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(['Title', 'MAL Link', 'Nomination Description', 'Image URL', 'Synopsis', 'YouTube URL'])
        for row in slotA:
            try:
                filewriter.writerow([row[0], row[1], row[2], row[3], row[4], row[5]])
            except UnicodeError:
                filewriter.writerow([row[0], row[1], "Ahhhhh", row[3], row[4], row[5]])

    with open('Slot B.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(['Title', 'MAL Link', 'Nomination Description', 'Image URL', 'Synopsis'])
        for row in slotB:
            try:
                filewriter.writerow([row[0], row[1], row[2], row[3], row[4], row[5]])
            except UnicodeError:
                filewriter.writerow([row[0], row[1], "Ahhhhh", row[3], row[4], row[5]])

    with open('Slot C.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(['Title', 'MAL Link', 'Nomination Description', 'Image URL', 'Synopsis'])
        for row in slotC:
            try:
                filewriter.writerow([row[0], row[1], row[2], row[3], row[4], row[5]])
            except UnicodeError:
                filewriter.writerow([row[0], row[1], "Ahhhhh", row[3], row[4], row[5]])

    print("Complete")


if __name__ == '__main__':
    main()
