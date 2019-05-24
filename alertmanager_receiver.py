from flask import Flask
from flask import request

import requests
import urllib.parse
import json
import os


TELEGRAM_TOKEN = ''
TELEGRAM_CHAT_ID = ''


app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def alert():
    headers = request.headers

    body = request.data.decode('utf8')
    body = json.loads(body)['alerts'][0]['annotations']['description']
    body = urllib.parse.quote(body)

    requests.get('https://api.telegram.org/bot'+TELEGRAM_TOKEN+'/sendMessage?chat_id='+TELEGRAM_CHAT_ID+'&text='+body+'&disable_notification=true')
    return("")

if __name__ == '__main__':

    errors = []
    if 'TELEGRAM_TOKEN' in os.environ:
        TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
    else:
        errors.append('TELEGRAM_TOKEN not found in environments variables.')

    if 'TELEGRAM_CHAT_ID' in os.environ:
        TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
    else:
        errors.append('TELEGRAM_CHAT_ID not found in environments variables.')

    if len(errors) > 0:
        for err in errors:
            print('- ', err)
        exit(2)

    app.run(host='0.0.0.0', port=80)
