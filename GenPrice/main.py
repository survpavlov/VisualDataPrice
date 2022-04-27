from flask import Flask, request, jsonify
import asyncio
from thread_price import *

app = Flask(__name__)

async def get_data_ticker(ticker, start):
    return " ".join(map(str, L[ticker][start:]))

@app.route('/', methods = ['GET'])
async def get_ticker():
    ticker = request.args.get('ticker', default = 0, type = int)
    start = request.args.get('start', default = 0, type = int)

    if ticker > 99: ticker = 99
    if ticker < 0: ticker = 0  
    t = await get_data_ticker(ticker, start)
    return jsonify(data = t)

if __name__ == "__main__":
    app.run(debug=True, host = '127.0.0.1')
