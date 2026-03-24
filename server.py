from flask import Flask, request
from main import place_buy, place_sell
import os 

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.data.decode("utf-8")
        print("📩 ALERT RECEIVED:", data)

        message = data.strip()

        if message == "UT Long":
            print("➡️ BUY SIGNAL")
            place_buy()

        elif message == "UT Short":
            print("➡️ SELL SIGNAL")
            place_sell()

        else:
            print("⚠️ Unknown signal:", message)

        return "ok"

    except Exception as e:
        print("❌ ERROR:", e)
        return "error", 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port = port)