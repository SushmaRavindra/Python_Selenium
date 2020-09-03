class Portfolio:
    def __init__(self):
        self._stocks = []

    def buy(self, name, shares, price):
        self._stocks.append(
            {'name': name,
             'shares': shares,
             'price': price}
            )

    def cost(self):
        amount = 0.00
        for stock in self._stocks:
            amount += stock['shares'] * stock['price']
        return amount

    def sell(self, name, nshares):
        names = {stock['name'] for stock in self._stocks}
        if not name in names:
            raise ValueError('You dont own the stock')
        for stock in self._stocks:
            if stock['name'] == name:
                if stock['shares'] < nshares:
                    raise ValueError('Not Enough Stocks')
                stock['shares'] -= nshares
                break


# p = Portfolio()
# p.buy("IBM", 10, 10)
# assert p.cost() == 150.00
# p.buy('HP', 10, 20)
# assert p.cost() == 300.00