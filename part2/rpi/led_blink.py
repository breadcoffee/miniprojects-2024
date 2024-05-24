# led_blink.py
# Red led
import RPi.GPIO as GPIO
import time

red_pin = 4
blue_pin = 5
green_pin = 6

GPIO.setmode(GPIO.BCM) # GPIO.Board 도 있음
GPIO.setup(red_pin, GPIO.OUT) # 4번핀 출력
GPIO.setup(blue_pin, GPIO.OUT) # 5번핀 출력
GPIO.setup(green_pin, GPIO.OUT) # 6번핀 출력

try:
    while(True):
        GPIO.output(red_pin, False)
        GPIO.output(blue_pin, False)
        GPIO.output(green_pin, False)
        time.sleep(1) # 모두 꺼짐

        GPIO.output(red_pin, True)
        GPIO.output(blue_pin, False)
        GPIO.output(green_pin, False)
        time.sleep(1) # 빨강

        GPIO.output(red_pin, False)
        GPIO.output(blue_pin, True)
        GPIO.output(green_pin, False)
        time.sleep(1) # 파랑

        GPIO.output(red_pin, False)
        GPIO.output(blue_pin, False)
        GPIO.output(green_pin, True)
        time.sleep(1) # 초록

        GPIO.output(red_pin, True)
        GPIO.output(blue_pin, True)
        GPIO.output(green_pin, True)
        time.sleep(1) # 흰색
except KeyboardInterrupt:
    GPIO.cleanup()