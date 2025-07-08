import logging
from mock_api import MockBinanceClient
from market_orders import place_market_order
from limit_order import place_limit_order
from advanced.stop_limit import place_stop_limit_order
from advanced.oco import place_oco_order

# Logging setup
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasicBot:
    def __init__(self):
        self.client = MockBinanceClient()
        logging.info("Initialized BasicBot with Mock Client")

    def run(self):
        while True:
            print("\n=== Binance Mock Trading Bot ===")
            print("1. Market Order")
            print("2. Limit Order")
            print("3. Stop-Limit Order")
            print("4. OCO Order")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.handle_market_order()
            elif choice == "2":
                self.handle_limit_order()
            elif choice == "3":
                self.handle_stop_limit_order()
            elif choice == "4":
                self.handle_oco_order()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def handle_market_order(self):
        symbol = input("Symbol (e.g., BTCUSDT): ").upper()
        side = input("Side (BUY/SELL): ").upper()
        quantity = float(input("Quantity: "))
        place_market_order(self.client, symbol, side, quantity)

    def handle_limit_order(self):
        symbol = input("Symbol (e.g., BTCUSDT): ").upper()
        side = input("Side (BUY/SELL): ").upper()
        quantity = float(input("Quantity: "))
        price = float(input("Limit Price: "))
        place_limit_order(self.client, symbol, side, quantity, price)

    def handle_stop_limit_order(self):
        symbol = input("Symbol (e.g., BTCUSDT): ").upper()
        side = input("Side (BUY/SELL): ").upper()
        quantity = float(input("Quantity: "))
        stop_price = float(input("Stop Price: "))
        limit_price = float(input("Limit Price: "))
        place_stop_limit_order(self.client, symbol, side, quantity, stop_price, limit_price)

    def handle_oco_order(self):
        symbol = input("Symbol (e.g., BTCUSDT): ").upper()
        side = input("Side (BUY/SELL): ").upper()
        quantity = float(input("Quantity: "))
        take_profit = float(input("Take Profit Price: "))
        stop_loss = float(input("Stop Loss Price: "))
        place_oco_order(self.client, symbol, side, quantity, take_profit, stop_loss)


if __name__ == "__main__":
    bot = BasicBot()
    bot.run()
