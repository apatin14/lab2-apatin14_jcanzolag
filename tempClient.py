from random import random
from random import randint
import matplotlib.pyplot as matPlot
from dotenv import load_dotenv
import pika
import os
load_dotenv()

xAxisData, yAxisData = [], []
matshow = False


credentials = pika.PlainCredentials(
    os.environ['MQTTUSER'], os.environ['MQTTPASSWORD'])
conectionparamenter = pika.ConnectionParameters(
    os.environ['MQTTSERVER'], os.environ['MQTTPORT'], '/', credentials)
connection = pika.BlockingConnection(conectionparamenter)
channel = connection.channel()
queue_name = os.environ['QUEUE_ARDUINO_TEMP_NAME']
channel.exchange_declare(
    exchange=os.environ['EXCHANGE'], exchange_type=os.environ['EXCHANGE_TOPIC'], durable=True)
channel.queue_bind(exchange=os.environ['EXCHANGE'],
                   queue=queue_name, routing_key=os.environ['BINDING_PROX_KEY'])

print(' [*] Waiting for logs. To exit press CTRL+C')

def filldata(i, data):
    xAxisData.append(i)
    yAxisData.append(data)
    matPlot.plot(xAxisData, yAxisData)
    matPlot.title('TeT Lab2 Temperature Client')
    matPlot.xlabel('Time (Seg)')
    matPlot.ylabel('Temperature (CM)')
    matPlot.pause(0.25)


def callback(ch, method, properties, body):
    global matshow
    if not matshow:
        matPlot.show()
        matshow = True
    filldata(method.delivery_tag, float(body.decode()))
    print(" [x] %r:%r" % (method.delivery_tag, body.decode()))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

matPlot.show()
channel.start_consuming()
