class StockData():
    def __init__(self, date, low, high, open, close):
        self.date = date 
        self.low = float(low) 
        self.high = float(high)
        self.open = float(open)
        self.close = float(close)

    def __repr__(self):
        return 'StockData date: {0} low: {1} high: {2} open: {3} close: {4}'.format(self.date, self.low, self.high, self.open, self.close)
