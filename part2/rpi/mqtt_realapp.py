# mqtt_realapp.py
# 온습도 센서 데이터 통신, RGB LED Setting
# MQTT -> json transfer
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import adafruit_dht
import board
import time
import datetime as dt
import json

red_pin = 4
blue_pin = 5
green_pin = 6
sensor_pin = 18

dev_id = "PKNU70"
loop_num = 0

## 초기화 시작
def onConnect(client, userdata, flags, reason_code, properties):
    print(f'Connected result code : {reason_code}')
    client.subscribe('pknu/rcv/')
    # RGB LED off
    GPIO.output(red_pin, GPIO.HIGH)
    GPIO.output(blue_pin, GPIO.HIGH)
    GPIO.output(green_pin, GPIO.HIGH)

def onMessage(client, userdata, msg):
    #print(f'{msg.topic} +{msg.payload}')
    # byte cond -> string
    # json ' -> " 
    value = json.loads(msg.payload.decode('utf-8').replace("'", '"'))
    res = value['control']
    # LED 컨트롤
    if(res == 'warning'):
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(blue_pin, GPIO.HIGH)
        GPIO.output(green_pin, GPIO.HIGH)
    elif(res == 'nomal'):
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(blue_pin, GPIO.HIGH)
        GPIO.output(green_pin, GPIO.LOW)
    elif(res == 'off'):
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(blue_pin, GPIO.HIGH)
        GPIO.output(green_pin, GPIO.HIGH)

GPIO.cleanup()
GPIO.setmode(GPIO.BCM) # GPIO.Board 도 있음

# LED
GPIO.setup(red_pin, GPIO.OUT) # 4번핀 출력
GPIO.setup(blue_pin, GPIO.OUT) # 5번핀 출력
GPIO.setup(green_pin, GPIO.OUT) # 6번핀 출력

# 온습도센서
GPIO.setup(sensor_pin, GPIO.IN) # 온습도 값을 받아옴
dhtDevice = adafruit_dht.DHT11(board.D18)

## 초기화 끝

## 실행 시작
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = onConnect # 접속 시 이벤트
mqttc.on_message = onMessage # 메세지 전송시

# 192.168.5.2 window ip
mqttc.connect('192.168.5.2', 1883, 60)

mqttc.loop_start()
while True:
    time.sleep(2) # DHT11 센서는 2초마다 갱신이 잘됨
    
    try:
        # 온습도 값을 받아서 MQTT로 전송
        temp = dhtDevice.temperature
        humid = dhtDevice.humidity
        #print(f'{loop_num} - Temp : {temp}℃ / Humid : {humid}%')

        origin_data = { 'DEV_ID' : dev_id,
                        'CURR_DT' : dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'TYPE' : 'TEMPHUMID',
                        'VALUE' : f'{temp}|{humid}'
                        } # dictionary data
        pub_data = json.dumps(origin_data, ensure_ascii=False)

        mqttc.publish('pknu/data/', pub_data)
        loop_num += 1
    except RuntimeError as ex:
        print(ex.args[0])
    except KeyboardInterrupt:
        break

mqttc.loop_stop()
dhtDevice.exit()
## 실행 끝