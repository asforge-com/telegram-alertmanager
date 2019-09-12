from flask import Flask
from flask import request

import requests
import urllib.parse
import json
import sys
import os


TELEGRAM_TOKEN = ''
TELEGRAM_CHAT_ID = ''


app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def alert():
    headers = request.headers

    body = request.data.decode('utf8')
    body = json.loads(body)
    message_to_send = ""
    priority = None
    no_notification = "false"
    
    for P in ["P1","P2","P3","P4","P5"]:
        for alert in body['alerts']:
            if alert['labels']['severity'] == P:
                alert_description = alert['annotations']['description']
                message_to_send += '\n\n' + urllib.parse.quote(alert_description)
                if priority is None:
                    priority = P
                    
    if priority in ["P4","P5"]:
        no_notification = "true"

    r = requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&disable_notification=%s' % (TELEGRAM_TOKEN,TELEGRAM_CHAT_ID,message_to_send,no_notification))
    if r.status_code != 200:
        print("An error occured on telegram API. Status code %s, response %s" % (r.status_code,r.content),file=sys.stderr)
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
