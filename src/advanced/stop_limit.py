import logging
from datetime import datetime
import random

def place_stop_limit_order(client, symbol, side, quantity, stop_price, limit_price):
    try:
        if quantity <= 0 or stop_price <= 0 or limit_price <= 0:
            raise ValueError("All numeric values must be > 0.")

        order_id = random.randint(100000, 999999)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        order = {
            "orderId": order_id,
            "symbol": symbol,
            "side": side,
            "type": "STOP_LIMIT",
            "quantity": quantity,
            "stop_price": stop_price,
            "limit_price": limit_price,
            "status": "TRIGGERED",
            "timestamp": timestamp
        }

        print("🟡 Stop-Limit order placed:", order)
        logging.info(f"Stop-Limit Order: {order}")
        return order

    except Exception as e:
        logging.error(f"[Stop-Limit Error] {str(e)}")
        print("❌ Error placing stop-limit order:", e)
        return None
