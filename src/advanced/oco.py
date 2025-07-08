import logging
from datetime import datetime
import random

def place_oco_order(client, symbol, side, quantity, take_profit, stop_loss):
    try:
        if quantity <= 0 or take_profit <= 0 or stop_loss <= 0:
            raise ValueError("All numeric values must be > 0.")

        order_id = random.randint(100000, 999999)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        order = {
            "orderId": order_id,
            "symbol": symbol,
            "side": side,
            "type": "OCO",
            "quantity": quantity,
            "take_profit": take_profit,
            "stop_loss": stop_loss,
            "status": "ACTIVE",
            "timestamp": timestamp
        }

        print("🟢 OCO order placed:", order)
        logging.info(f"OCO Order: {order}")
        return order

    except Exception as e:
        logging.error(f"[OCO Order Error] {str(e)}")
        print("❌ Error placing OCO order:", e)
        return None
