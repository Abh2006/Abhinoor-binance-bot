from mock_api import MockBinanceClient
import logging

def place_market_order(client, symbol, side, quantity):
    try:
        result = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        print("Market order placed:", result)
        logging.info(f"Market Order: {result}")
        return result

    except Exception as e:
        logging.error(f"Error placing market order: {str(e)}")
        print("An error occurred:", e)
        return None
