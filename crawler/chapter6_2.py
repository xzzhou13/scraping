from urllib.request import urlopen
from io import StringIO
import csv

'''读取CSV文件'''
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
#用csv.reader读取
csvReader = csv.reader(dataFile)
for row in csvReader:
    print(row)
#用csv.DictReader读取
dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)
for row in dictReader:
    print(row)