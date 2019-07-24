import paho.mqtt.client as mqtt
import json
import time


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("chat")
    client.publish("chat", json.dumps({"user": user, "say": "Hello,anyone!"})) #


# 接收到消息的回调方法
def on_message(client, userdata, msg):
    # print(msg.topic+":"+str(msg.payload.decode()))
    # print(msg.topic+":"+msg.payload.decode())
    payload = json.loads(msg.payload.decode())
    print(payload.get("user") + ":" + payload.get("say"))


if __name__ == '__main__':
    client = mqtt.Client(client_id="cnm")
    client.username_pw_set(username="wrd1", password="123456")  # 必须设置，否则会返回「Connected with result code 4」
    client.on_connect = on_connect
    client.on_message = on_message

    HOST = '2001:da8:270:2021::34'

    client.connect(HOST, 1883, 30)
    #client.loop_forever()

    user = input("请输入名称:")
    client.user_data_set(user)

    client.loop_start()

    while True:
        str = input()
        if str:
            client.publish("chat", json.dumps({"user": user, "say": str}))
            if str=="exit":
                print("Now we exit!\n")
                time.sleep(1)
                break;