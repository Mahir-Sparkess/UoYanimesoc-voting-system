import csv

slotA = []
slotB = []
slotC = []


with open('submissions/AnimeSoc Termly Anime Nomination Form (Responses) - Form responses 1.csv',newline='') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')

    for row in readCSV:
        currentitem = 4
        
        while currentitem <= 16:
            if row[currentitem+2] == 'Slot A':
                slotA.append([row[currentitem],row[currentitem+1],row[currentitem+3]])
            elif row[currentitem+2] == 'Slot B':
                slotB.append([row[currentitem],row[currentitem+1],row[currentitem+3]])
            elif row[currentitem+2] == 'Slot C':
                slotC.append([row[currentitem],row[currentitem+1],row[currentitem+3]])

            currentitem+=4

with open('Slot A.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile,delimiter=',')
    filewriter.writerow(['Title','MAL Link','Description'])
    for row in slotA:
        filewriter.writerow([row[0],row[1],row[2]])

with open('Slot B.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile,delimiter=',')
    filewriter.writerow(['Title','MAL Link','Description'])
    for row in slotB:
        filewriter.writerow([row[0],row[1],row[2]])

with open('Slot C.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile,delimiter=',')
    filewriter.writerow(['Title','MAL Link','Description'])
    for row in slotC:
        filewriter.writerow([row[0],row[1],row[2]])