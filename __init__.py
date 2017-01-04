from flask import Flask
import RPi.GPIO as GPIO
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

app = Flask(__name__)


@app.route('/')
def test():
    print('started on')
    return 'Hello... World...'


@app.route('/turnon', methods=['GET', 'POST'])
def turnon():
    print('recieved')
    if requests.method == 'POST':
        print('led should turn on')
        GPIO.output(18, 1)
    return 'penis'


@app.route('/turnoff/', methods=['GET', 'POST'])
def turnoff():
    print('recieved')
    if requests.method == 'POST':
        print('led should turn on')
        GPIO.output(18, 0)
    return 'balls'


@app.route('/blink/')
def blink():
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
