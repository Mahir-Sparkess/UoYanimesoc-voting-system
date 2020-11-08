from jikanpy import Jikan
import csv
import time
jikan = Jikan()

slotA = []
slotB = []
slotC = []


with open('submissions/AnimeSoc Termly Anime Nomination Form (Responses) - Form responses 1.csv',newline='') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')

    for row in readCSV:
        currentitem = 4
        while currentitem <= 16:
            id = ''
            for i in row[currentitem+1]:
                if str.isdigit(i):
                    id=id+i
                if i == '/' and len(id) > 1:
                    break
            if row[currentitem+2] == 'Slot A':
                slotA.append([row[currentitem],row[currentitem+1],str(row[currentitem+3]).replace("'","\'"),jikan.anime(id).get("image_url"),jikan.anime(id).get("synopsis").replace("'","\'")])
            elif row[currentitem+2] == 'Slot B':
                slotB.append([row[currentitem],row[currentitem+1],str(row[currentitem+3]).replace("'","\'"),jikan.anime(id).get("image_url"),jikan.anime(id).get("synopsis").replace("'","\'")])
            elif row[currentitem+2] == 'Slot C':
                slotC.append([row[currentitem],row[currentitem+1],str(row[currentitem+3]).replace("'","\'"),jikan.anime(id).get("image_url"),jikan.anime(id).get("synopsis").replace("'","\'")])
            time.sleep(4)
            currentitem+=4

with open('Slot A.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile,delimiter=',')
    filewriter.writerow(['Title','MAL Link','Nomination Description','Image URL','Synopsis'])
    for row in slotA:
        filewriter.writerow([row[0],row[1],row[2],row[3],row[4]])

with open('Slot B.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile,delimiter=',')
    filewriter.writerow(['Title','MAL Link','Nomination Description','Image URL','Synopsis'])
    for row in slotB:
        filewriter.writerow([row[0],row[1],row[2],row[3],row[4]])

with open('Slot C.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile,delimiter=',')
    filewriter.writerow(['Title','MAL Link','Nomination Description','Image URL','Synopsis'])
    for row in slotC:
        filewriter.writerow([row[0],row[1],row[2],row[3],row[4]])

print("Complete")