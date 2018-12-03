import os
from classes.Stock import Stock
from classes.MovingAverage import MovingAverage
from classes.Trader import Trader

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
# first = int(input('First moving average: '))
# second = int(input('Second moving average: '))

first = 20
second = 50

if first == second or first == 0 or second == 0:
    print('Wrong moving average, exiting...')
    exit()

if first > second: 
    lower = second 
    higher = first
else: 
    lower = first
    higher = second

stoploss = float(input('Stoploss percent: '))
# takeprofit = float(input('Takeprofit percent: '))
takeprofit = 0

maXY = MovingAverage(lower, higher, stock)

positive = 0
negative = 0

# vásárlási ár, eladási szint, kiszállási ár
trader = Trader(stoploss, takeprofit)

for index, data in enumerate(Stock.data):
    diff = maXY.getDiff(index)

    lowest = "%.2f" % maXY.prevLow
    highest = "%.2f" % maXY.prevHigh
    # if diff != 0:
    # print('Date: {0:10}, lowestMA: {1:5}, highestMa: {2:5}, Diff: {3}'.format(data.date, lowest, highest, diff))

    # trader
    if trader.checkPrices(data, diff):
        stoplossPrice = "%.4f" % trader.stoplossPrice
        price = "%.4f" % trader.sellPrice
        print('- Date: {0:10}, Status: {1:10} Ár: {2:7} Stoploss {3}'.format(data.date, trader.lastAction, price, stoplossPrice))
    
    if diff == 1:
        trader.buyStock(data)
        stoplossPrice = "%.4f" % trader.stoplossPrice
        price = "%.4f" % trader.price
        print('+ Date: {0:10}, Status: {1:10} Ár: {2:7} Stoploss {3}'.format(data.date, 'Buy', price, stoplossPrice))

print('Trader is completed')
print('Success: {0:5}, Lose: {1:5}, Buys: {2:3}'.format(trader.success, trader.fail, trader.buyCounter))
