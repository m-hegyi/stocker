from classes.StockData import StockData
import csv

class Stock(object):

    data = []

    def __init__(self, path):
        # csv fájl megnyitása és memóráiába töltése
        print('csv opening...')
        with open(path, 'r') as csvfile:
            data = csv.reader(csvfile, delimiter=',', quotechar='|')
            columns = {}

            for index, row in enumerate(data):
                if (index == 0):
                    for i, value in enumerate(row):
                        columns[value] = i
                elif (index != 0):
                    self.data.append(StockData(
                        row[columns['Date']], row[columns['Low']], row[columns['High']], row[columns['Open']], row[columns['Close']]))

        print('csv loaded...')

    def getValuesByDate(self, date):
        for data in self.data:
            if (data.date == date):
                return data

    def getIndexByDate(self, date):
        for index, data in enumerate(self.data):
            if (data.date == date):
                return index

        return False

    def getValuesByIndex(self, index):
        try: 
            return self.data[index]
        except IndexError:
            return False