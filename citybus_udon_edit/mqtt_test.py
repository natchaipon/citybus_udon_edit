import time
import paho.mqtt.publish as publish
import random
import sqlite3

money = 0

hostname = "103.86.49.233"
port = 1883
auth = {
    'username':'mymqtt',
    'password':'0932398390'
}



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

while True:
    money = random.randint(0, 100)
    send_mqtt()
    time.sleep(5)
