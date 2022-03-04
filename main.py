import requests
import json
import time

# api url
link = "https://api.coingecko.com/api/v3/simple/price?ids=1sol&vs_currencies=usd&include_24hr_vol=true&include_24hr_change=true"

# token telegram (create with botfather)
token = ""
# chat id (to get chat id -> https://t.me/RawDataBot)
chat_id = ""

while True:
  getPrice = requests.get(link).text
  loadPrice = json.loads(getPrice)
  resultPrice = loadPrice["1sol"]["usd"]
  resultChange = int(loadPrice["1sol"]["usd_24h_change"])
  
  postPrice = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(token,'SendMessage'),
        data={
          'chat_id': {chat_id},
          'text': '*❗️[Price Alert]❗️*\n Price 1SOL now is *${0} [{1}%]*'.format(resultPrice, resultChange),
          'parse_mode': 'Markdown'
          }
    ).json()

  if(postPrice['ok'] == True):
    print('Success')
  else:
    print('Failed')

  print('Update every 5 minutes')
  time.sleep(300)
