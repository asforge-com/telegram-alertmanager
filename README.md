# telegram-alertmanager

This is an API written in python created in a monitoring context to be linked with alertmanager from prometheus to allow alertmanager to send alerts on Telegram.

### Table of contents

1. [TLDR](#tldr)
2. [Tokens](#tokens)
3. [How to use the API?](#howto)
4. [Alertmanager integration](#alertmanager-integration)

# TLDR <a name="tldr"></a>

## Docker

```bash
docker run --name asforge/telegram-alertmanager \
	-e TELEGRAM_TOKEN="bot_token" \
	-e TELEGRAM_CHAT_ID="group_ID"
```
## Without Docker

```bash
export TELEGRAM_TOKEN=insert_your_bot_token_here
export TELEGRAM_CHAT_ID=insert_your_group_ID_here

apt install python3-pip
pip3 install -r requirements.txt
chmod +x alertmanager_receiver.py

./alertmanager_receiver.py
```

# Tokens <a name="tokens"></a>

In order to receive alerts on the Telegram channel you have chosen, you must create retrieve your chat ID

In the same way, you also need to create a Telegram Bot API and retrieve its token. It is this bot that will manage the alerts and display them in your channel.


# Alertmanager integration <a name="alertmanager-integration"></a>

To link your API with alertmanager you should edit the `alertmanager.yml` file from alertmanager prometheus part.

```yaml
receivers:
  - name: 'telegram'
    webhook_configs:
    - url: 'http://api-telegram-alertmanager-hostname'

```

The API will retrieve the description part of the `prometheus.rules.yaml` file, so you must write down your alerts information there on prometheus side.

You should be able to see your beautiful and well-integrated alerts showing up on your own Telegram channel thereafter.
