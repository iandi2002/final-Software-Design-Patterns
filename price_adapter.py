

class PriceAdapter:
    def __init__(self, strategy):
        self.strategy = strategy

    def get_clothing_list(self):
        clothing_list = self.strategy.get_clothing_list()
        clothing_list = [(item, self._convert_to_tenge(price)) for item, price in clothing_list]
        return clothing_list

    def _convert_to_tenge(self, price_usd):
        exchange_rate = 422.40
        price_tenge = round(price_usd * exchange_rate, 2)
        return price_tenge
