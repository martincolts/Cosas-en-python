import csv
with open("00f1221ebf94129c8d4643d1542ebd4c1fabf9d5.csv", 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    bateryLevel = 0
    wifiStatus = 0
    list = []
    rowList = []
    for row in spamreader:
        if "power" in row[3]:
            if "level" in row[3]:
                 bateryLevel = row[4]
        if "wifi" in row[3]:
            if "state" in row[3]:
                if "enabled" in row[4]:
                    wifiStatus = 1
                else:
                    wifiStatus = 0
                print (bateryLevel,";",row[3],row[4],wifiStatus)
                rowList.append(bateryLevel)
                rowList.append(wifiStatus)
                print(rowList)
                list.append(rowList)
                rowList = []

with open('result.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for rowL in list:
        spamwriter.write(rowL[0], rowL[1])