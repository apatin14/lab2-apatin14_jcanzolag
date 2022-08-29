import matplotlib.animation as animation
import matplotlib.pyplot as matPlot
from dotenv import load_dotenv
from random import randint
from random import random
import os
import pika

load_dotenv()

sensorFigure = matPlot.figure()

figureAxis = sensorFigure.add_subplot(1, 1, 1)
figureAxis.set_ylabel('Temperature (CM)')
figureAxis.set_xlabel('Time (Seg)')
figureAxis.set_title('TeT Lab2')
temperature = randint(16, 40)

xAxisData, yAxisData = [], []


def filldata(i):
    datos = temperature + (1/(1/random()))

    print(datos)
    senddata(str(datos))
    xAxisData.append(i)
    yAxisData.append(datos)
    figureAxis.plot(xAxisData, yAxisData)


def senddata(body):

    credentials = pika.PlainCredentials(
        os.environ['MQTTUSER'], os.environ['MQTTPASSWORD'])
    conectionparamenter = pika.ConnectionParameters(
        os.environ['MQTTSERVER'], os.environ['MQTTPORT'], '/', credentials)
    connection = pika.BlockingConnection(conectionparamenter)
    channel = connection.channel()
    channel.exchange_declare(
        exchange=os.environ['EXCHANGE'], exchange_type=os.environ['EXCHANGE_TOPIC'], durable=True)
    channel.basic_publish(
        exchange=os.environ['EXCHANGE'], routing_key=os.environ['ROUTING_KEY'], body=body)
    print("Sended data to Message Mananger")
    connection.close()


while True:
    ani = animation.FuncAnimation(
        sensorFigure, filldata, interval=1000)
    matPlot.show()
