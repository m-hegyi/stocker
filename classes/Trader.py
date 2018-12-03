from classes.StockData import StockData
# elvégzi a vásárlást és eladást ellenőrízve az adatokat

class Trader:
    stoploss    = 0
    takeprofit  = 0
    success     = 0
    fail        = 0
    price       = 0
    hasActive   = False
    buyCounter  = 0
    lastAction  = ''
    sellPrice   = 0
    stoplossPrice = 0

    def __init__(self, stoploss, takeprofit):
        self.stoploss   = stoploss
        self.takeprofit = takeprofit

    def __repr__(self):
        return 'Trader'

    def checkPrices(self, StockData: StockData, diff):
        if self.hasActive == False:
            return

        self.lastAction = ''
        self.sellPrice = 0
        
        # ellenőrizni kell hogy a stoploss-t vagy a meghatározott eladási pontot érte-e el
        stoplossPrice = self.price - self.price * (self.stoploss / 100)
        self.stoplossPrice = stoplossPrice
        
        if stoplossPrice > StockData.low:
            # eladunk veszteséggel
            self.sellStock(False)
            # veszteség esetén a stoploss a mértékadó ár
            self.sellPrice = stoplossPrice
            self.lastAction = 'Lose'
            return True
        elif diff == -1:
            # eladunk a meghatározz szinten
            self.sellStock(True)
            # eladás esetén a záró árat kell nézni ? talán
            self.sellPrice = StockData.close
            self.lastAction = 'Success'
            return True

        return False

    def buyStock(self, StockData: StockData):
        if self.hasActive == True:
            return 

        self.hasActive = True

        price = (StockData.close + StockData.open + StockData.high + StockData.low) / 4

        self.price = price
        self.buyCounter += 1

    def sellStock(self, isSucceeded):
        self.hasActive = False
        self.price = 0

        if isSucceeded == True:
            self.success += 1
        else:
            self.fail +=1