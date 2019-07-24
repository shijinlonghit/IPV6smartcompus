
import paho.mqtt.client as mqtt
import json
import datetime
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("chat")
    client.publish("chat", json.dumps({"user": user, "say": "Hello,anyone!"}))


def on_message(client, userdata, msg):
    #print(msg.topic+":"+str(msg.payload.decode()))
    #print(msg.topic+":"+msg.payload.decode())
    payload = json.loads(msg.payload.decode())
    print(payload.get("user")+":"+payload.get("say"))


if __name__ == '__main__':
    client = mqtt.Client()
    client.username_pw_set("admin", "public")
    client.on_connect = on_connect
    client.on_message = on_message

    #
    #127.0.0.1
    HOST = '2001:da8:270:2021::34'  # 2001:da8:270:2021::34

    client.connect(HOST, 1883, 60)
    #client.loop_forever()

    user = 'py_timer'
    client.user_data_set(user)
    #string = '2014-01-08 11:59:58'

    client.loop_start()


    #while True:
    #    time1 = time.strftime('%Y-%m-%d %H:%M:%S')
    #    client.publish("chat", json.dumps({"user": user, "say": time1}))
    #    time.sleep(2)

    while True:
        str = input()
        if str:
            client.publish("chat", json.dumps({"user": user, "say": str}))
            if str=="exit":
                print("Don't want to play with you!\n");
                break;