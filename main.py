import os
from classes.Stock import Stock
from classes.MovingAverage import MovingAverage

#legyen bementi adat a csv fájl?
#print(os.path.dirname())
dirPath = os.path.dirname(os.path.realpath(__file__)) + '\\csv\\'

fileName = ''

fileName = input('The csv file name without the .csv: ')

if (fileName == ''):
    print('No file provided, exiting...')
    exit()

path = dirPath + fileName + '.csv'

if (os.path.isfile(path) == False):
    print('No valid file, exiting...')
    exit()


stock = Stock(path)
# fel kell dolgozni a csv-t

# egy időponthoz tartozó adatok feldolgozása a moving averageval
first = int(input('First moving average: '))
second = int(input('Second moving average: '))

if first == second or first == 0 or second == 0:
    print('Wrong moving average, exiting...')
    exit()

if first > second: 
    lower = first 
    higher = second
else: 
    lower = second
    higher = first

# stoploss = float(input('Stoploss percent: '))
# takeprofit = float(input('Takeprofit percent: '))

maXY = MovingAverage(lower, higher, stock)

positive = 0
negative = 0

# vásárlási ár, eladási szint, kiszállási ár

for index, data in enumerate(Stock.data):
    diff = maXY.getDiff(index)
    if diff == 1:
        # vásárlási pozíció
        positive += 1
    elif diff == -1:
        # eladási pozíció
        negative += 1
    print('Date: {0:10}, Price: {1:10}, Diff: {2}'.format(data.date, data.close, diff))

print('positive: {0:5}, negative: {1:5}'.format(positive, negative))