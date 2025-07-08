from mock_api import MockBinanceClient
import logging

def place_limit_order(client, symbol, side, quantity, price):
    try:
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be greater than 0.")

        result = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price
        )
        print("✅ Limit order placed:", result)
        logging.info(f"Limit Order Placed: {result}")
        return result

    except Exception as e:
        logging.error(f"[Limit Order Error] {str(e)}")
        print("❌ Error placing limit order:", e)
        return None
