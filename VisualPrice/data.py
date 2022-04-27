import requests

Base_URL = 'http://127.0.0.1:5000'

def get_data_ticker(ticker, start):
  response = requests.get(f"{Base_URL}", params = {'ticker': ticker, 'start': start})
  json_data = response.json()
  s = json_data['data']
  return list(map(int, s.split()))


