"""
测试emq-消费者
@author me
"""
import paho.mqtt.client as mqtt
import time


class Consumer(object):

    def get_time(self):
        """
    获取时间
    """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    def on_subscribe(self, client, userdata, mid, granted_qos):
        """
        开始时订阅 callback
        :param userdata:
        :param mid:
        :param granted_qos:
        :return:
        """
        print(self.get_time(), "Begin subscribe topic with ", mid)

    def on_message(self, client, userdata, message):
        """
        接收消息 callback
        :param userdata:
        :param message:
        :return:
        """
        print(self.get_time(), " Received message '" + str(message.payload) + "' on topic '" +
              message.topic + "' with QoS " + str(message.qos))

    def on_connect(self, client, userdata, flags, rc):
        """
        连接时的 callback
        :param client:
        :param userdata:
        :param flags:
        :param rc:
        :return:
        """
        print(self.get_time(), "[consumer]Connected with result code " + str(rc))
        if rc == 0:
            sub_result = client.subscribe("chat")
            print(self.get_time(), "Connected with result is (status,mid)", sub_result)
        else:
            print(self.get_time(), " connect failed")

    def run(self):
        # 4就是MQTT3.1.1
        emq_client = mqtt.Client(client_id="emqttd_2019")
        emq_client.on_connect = self.on_connect
        # emq_client.on_disconnect = self.on_disconnect
        emq_client.on_message = self.on_message
        emq_client.on_subscribe = self.on_subscribe
        # 设置用户密码，如果没有设置用户，这里可以省略
        emq_client.username_pw_set('wrd2', "123456")
        emq_client.connect("2001:da8:270:2021::34", 1883, keepalive=60)
        emq_client.loop_forever()


if __name__ == "__main__":
    consumer = Consumer()
    consumer.run()