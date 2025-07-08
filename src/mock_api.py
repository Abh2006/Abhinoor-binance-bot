import random
from datetime import datetime

class MockBinanceClient:
    def __init__(self):
        self.orders = []

    def futures_create_order(self, symbol, side, type, quantity, price=None):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if type == "LIMIT" and (price is None or price <= 0):
            raise ValueError("Valid price required for LIMIT order.")
        
        order_id = random.randint(10000, 99999)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        order = {
            "orderId": order_id,
            "symbol": symbol,
            "side": side,
            "type": type,
            "quantity": quantity,
            "price": price,
            "status": "FILLED",
            "timestamp": timestamp
        }

        self.orders.append(order)
        return order
