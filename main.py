from delta_rest_client import DeltaRestClient, OrderType
import os

# ✅ Initialize client
delta_client = DeltaRestClient(
    base_url='https://cdn-ind.testnet.deltaex.org',
    api_key=os.getenv("DELTA_API_KEY"),
    api_secret=os.getenv("DELTA_API_SECRET")
)

PRODUCT_ID = 84

# 🔥 Track position
current_position = None


def place_buy():
    global current_position

    try:
        if current_position == "BUY":
            print("⚠️ Already in BUY. Skipping...")
            return

        print("📈 Placing BUY order...")

        response = delta_client.place_order(
            product_id=PRODUCT_ID,
            size=1,
            side='buy',
            order_type=OrderType.MARKET,
        )

        print("✅ BUY RESPONSE:", response)
        current_position = "BUY"

    except Exception as e:
        print("❌ BUY ERROR:", e)


def place_sell():
    global current_position

    try:
        if current_position == "SELL":
            print("⚠️ Already in SELL. Skipping...")
            return

        print("📉 Placing SELL order...")

        response = delta_client.place_order(
            product_id=PRODUCT_ID,
            size=1,
            side='sell',
            order_type=OrderType.MARKET,
        )

        print("✅ SELL RESPONSE:", response)
        current_position = "SELL"

    except Exception as e:
        print("❌ SELL ERROR:", e)