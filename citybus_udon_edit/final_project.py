import sys
from PyQt5.QtWidgets import QWidget , QApplication , QMainWindow , QMessageBox
from PyQt5.QtCore import *
from citybus_udon_ui import Ui_city_bus
from alert import Ui_alert
import time
import RPi.GPIO as GPIO
import paho.mqtt.publish as publish
import sqlite3
from datetime import datetime

# conn = sqlite3.connect('citybus_udon.db')

money = 29
end_time = 0
state = 0
price_user = 15
time_sleep_mqtt = 0
end_time_alert = 0

hostname = "103.86.49.233"
port = 1883
auth = {
    'username':'mymqtt',
    'password':'0932398390'
}


GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def coin_add_money(channel):
    global money
    money += 1

def bank_add_money(channel):
    global money
    money += 10

GPIO.add_event_detect(27 , GPIO.FALLING , callback = bank_add_money , bouncetime=60)
GPIO.add_event_detect(22 , GPIO.FALLING , callback = coin_add_money , bouncetime=50)

def send_mqtt():
    global hostname , port , auth , money

    try:
        publish.single("mynew/test", money , hostname = hostname , port  = port , auth = auth)
    except:
        date_time = datetime.now()
        # print(money)
        # print(date_time)
        with sqlite3.connect("C:/Users/Natchaipon/Desktop/citybus_udon_edit/citybus_udon.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO citybus_table (money , time) VALUES (? , ?)", (money , date_time))
            con.commit()
        con.close()

        # date_time = datetime.now()
        # data_insert = (money , date_time)
        # conn.execute("INSERT INTO citybus_table (money , time) VALUES (? , ?)" , data_insert);
        # conn.commit()
        # conn.close()

class alert(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_alert() 
        self.ui.setupUi(self)
alert

class MyApp(QMainWindow):
    def __init__(self , parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_city_bus()
        self.ui.setupUi(self)
        self.ui.studen.clicked.connect(self.studen_button)
        self.ui.people.clicked.connect(self.people_button)

        self.timer = QTimer()
        self.timer.setInterval(2)
        self.timer.timeout.connect(self.maim_task)
        self.timer.start()
        
    def maim_task(self):
        global money , price_user , end_time , state , end_time_alert , alert

        time_now = time.time() * 1000
        
#        print(f'{money} -- {end_time} -- {state} -- {price_user} -- {time_now}')

        money_user = price_user - money
        
        if money_user >= 0:
            self.ui.display.display(money_user)
            print(f'if------> {money_user}')
        else:
            self.ui.display.display(0)
            print(f'else------> {money_user}')

        if money > 0 and state == 0:
            print("start time")
            end_time = time_now + (20 * 1000)
            state = 1

        # -5 >= 15 & 1 ==  1
        elif money >= price_user and state == 1:
#            print("success")
#            self.ui.display.display(0)
            time.sleep(3)
            print(money)
            # send data to mqtt
            # publish.single("mynew/test", money , hostname = hostname , port  = port , auth = auth)
            send_mqtt()
            alert.show()
            end_time_alert = time_now + (5 * 1000)
            state = 0
            money = 0
            end_time = 0
            price_user = 0
            

        elif time_now >= end_time_alert and end_time_alert > 0:
            alert.close()
            end_time_alert = 0


        if time_now >= end_time and state == 1 and end_time != 0:
            print("end time")
            # send data to mqtt
            # publish.single("mynew/test", money , hostname = hostname , port = port , auth = auth)
            send_mqtt()
            money = 0
            end_time = 0
            state = 0
            price_user = 0
            
    
    def studen_button(self):
        # print("studen")
        global money , price_user , end_time , state
        global hostname , port , auth
        
        if money > 0:
            # publish.single("mynew/test", money , hostname = hostname , port = port , auth = auth)
            send_mqtt()

        price_user = 15
        self.ui.display.display(price_user)
        money = 0
        end_time = 0
        state = 0

    def people_button(self):
        # print("people")
        global money , price_user , end_time , state
        global hostname , port , auth

        if money > 0:
            # publish.single("mynew/test", money , hostname = hostname , port = port , auth = auth)
            send_mqtt()
            
        price_user = 20
        self.ui.display.display(price_user)
        money = 0
        end_time = 0
        state = 0

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    e = MyApp()
    alert = alert()
    sys.exit(app.exec_())

