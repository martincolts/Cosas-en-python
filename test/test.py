import csv
with open('/home/tincho/Escritorio/0269e21475ac65ad57fbec9c83ab4960ec66581b.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        print (row[3])

