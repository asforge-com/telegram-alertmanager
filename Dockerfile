FROM python:3.6

ADD alertmanager_receiver.py /
ADD requirements.txt /

RUN pip3 install -r requirements.txt

CMD [ "python", "./alertmanager_receiver.py" ]
