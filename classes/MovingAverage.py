from classes.Stock import Stock

class MovingAverage():
    prev = 0
    prevLow = 0
    prevHigh = 0

    def __init__(self, lower, higher, Stock: Stock):
        self.lower = lower
        self.higher = higher
        self.Stock = Stock
    
    def getLowerValueByDate(self, date):
        # az első átlag kiszámítása
        index = self.Stock.getIndexByDate(date)
        if (index == False):
            print('not valid date')
            return False
        else:
            value = self.calculateAverage(self.lower, index)
            return value

    def getHigherValueByDate(self, date):
        index = self.Stock.getIndexByDate(date)
        if (index == False):
            print('not valid date')
            return False
        else:
            value = self.calculateAverage(self.higher, index)
            return value

    def getLowerValueByIndex(self, index):
        # az első átlag kiszámítása
        if (index == False):
            print('not valid date')
            return False
        else:
            value = self.calculateAverage(self.lower, index)
            return value

    def getHigherValueByIndex(self, index):
        if (index == False):
            print('not valid date')
            return False
        else:
            value = self.calculateAverage(self.higher, index)
            return value

    def getDiff(self, index):
        # akkor lesz negatív ha a rövidebb MA növekedése megáll
        lower = self.getLowerValueByIndex(index)
        higher = self.getHigherValueByIndex(index)

        if higher == 0 or lower == 0: 
            self.prev = 0
            return 0

        diff = lower - higher
    
        if self.prev < 0 and diff > 0:
            self.prev = diff
            self.prevLow = lower
            self.prevHigh = higher
            return 1
        elif self.prevLow > lower:
            self.prev = diff 
            self.prevLow = lower
            self.prevHigh = higher
            return -1

        self.prevLow = lower
        self.prevHigh = higher
        self.prev = diff
        return 0

    def calculateAverage(self, length, dateIndex):
        # (napi adat + köv napi adat) / számolt adatok hossza
        average = 0
        for i in range(length):
            index = dateIndex - i
            data = self.Stock.getValuesByIndex(index)
            if (data == False):
                return 0
                
            average += data.open

        return average / length
