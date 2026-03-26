from flask import Flask, request
from main import place_buy, place_sell
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        #  Get clean message
        data = request.data.decode("utf-8").strip().lower()

        print("ALERT RECEIVED:", data)

        #  BUY SIGNAL
        if "long" in data:
            print("BUY SIGNAL")
            place_buy()

        #  SELL SIGNAL
        elif "short" in data:
            print("SELL SIGNAL")
            place_sell()

        else:
            print("Unknown signal:", data)

        return "ok", 200

    except Exception as e:
        print("ERROR:", e)
        return "error", 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)