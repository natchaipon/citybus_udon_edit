import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtCore import *
from citybus_udon1 import Ui_city_bus
import time
import RPi.GPIO as GPIO
import paho.mqtt.publish as publish

money = 0
end_time = 0
state = 0
price_user = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def coin_add_money(channel):
    global money
    money += 1

def bank_add_money(channel):
    global money
    money += 10

GPIO.add_event_detect(27 , GPIO.FALLING , callback = bank_add_money , bouncetime=10)
GPIO.add_event_detect(22 , GPIO.FALLING , callback = coin_add_money , bouncetime=50)


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_city_bus()
        self.ui.setupUi(self)

        self.ui.studen.clicked.connect(self.studen_button)
        self.ui.people.clicked.connect(self.people_button)
        # self.ui.lcdNumber.display()

        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
        

    def recurring_timer(self):
        global money
        global price_user
        global end_time
        global state
        
        hostname = "103.86.49.233"
        port = 1883
        auth = {
        'username':'mymqtt',
        'password':'0932398390'
        }

        time_now = time.time() * 1000

        if money > 0 and state == 0:
            print("start time")
            end_time = time_now + (20 * 1000)
            self.ui.studen.setEnabled(False)
            self.ui.people.setEnabled(False)
            state = 1
            
        if money >= 0:
            self.ui.display.display(price_user - money)
            print(f'{money} -- {end_time} -- {state} -- {price_user}')

        if money >= price_user and state == 1:
            print("success")
#            self.ui.display.display(0)
            time.sleep(3)
            print(money)
            # send data to mqtt
            publish.single("mynew/test", money , hostname = hostname , port  = port , auth = auth)
            money = 0
            end_time = 0
            state = 0
            price_user = 0
            self.ui.studen.setEnabled(True)
            self.ui.people.setEnabled(True)

        if time_now >= end_time and state == 1:
            print("end time")
            # send data to mqtt
            publish.single("mynew/test", money , hostname = hostname , port = port , auth = auth)
            print(money)
            
            self.ui.studen.setEnabled(True)
            self.ui.people.setEnabled(True)
            
            money = 0
            end_time = 0
            state = 0
            price_user = 0
    
        
    def studen_button(self):
        # print("studen")
        global price_user
        price_user = 15
        self.ui.display.display(price_user)

    def people_button(self):
        # print("people")
        global price_user
        price_user = 20
        self.ui.display.display(price_user)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    e = MyApp()
    sys.exit(app.exec_())


