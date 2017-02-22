from flask import Flask, request
import RPi.GPIO as GPIO
import time


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
    if request.method == 'POST':
        print('turn led on')
        GPIO.output(18, 1)
    return 'on'


@app.route('/turnoff', methods=['GET', 'POST'])
def turnoff():
    print('recieved')
    if request.method == 'POST':
        print('turn led off')
        GPIO.output(18, 0)
    return 'off'


@app.route('/blink', methods=['GET', 'POST'])
def blink():
    print('recieved')
    if request.method == "POST":
        print('blink led')
        for x in range(0, 10): # blink for 10 seconds
            GPIO.output(18, 1)
            time.sleep(.5)
            GPIO.output(18, 0)
            time.sleep(.5)
            x += 1
    return 'blink'


@app.route('/getmac', methods=['GET', 'POST'])
def getmac():
    print('looking for mac adress\n')
    if request.method == 'POST':
        try:
            adress = open('/sys/class/net/' + 'wlan0' + '/address').read()
        except:
            adress = "00:00:00:00:00:00"
        print(adress[0:17])
        return adress[0:17]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
