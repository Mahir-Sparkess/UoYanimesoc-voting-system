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
for row in slotC:
    print(row[0])
