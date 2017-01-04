from flask import Flask
import RPi.GPIO as GPIO
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

app = Flask(__name__)


@app.route('/')
def test():
    return 'Hello... World...'


@app.route('/turnon/')
def turnon():
    GPIO.output(18, 1)
    return


@app.route('/turnoff/')
def turnoff():
    GPIO.output(18, 0)
    return


@app.route('/blink/')
def blink():
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
