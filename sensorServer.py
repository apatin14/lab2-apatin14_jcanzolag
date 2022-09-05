import matplotlib.animation as animation
import matplotlib.pyplot as matPlot
from dotenv import load_dotenv
import serial
import time
import os
import pika


load_dotenv()

serialData = serial.Serial(os.environ['ARDUINO_PORT'], 9600)
time.sleep(1)

sensorFigure = matPlot.figure()

figureAxis = sensorFigure.add_subplot(1, 1, 1)
figureAxis.set_ylabel('Proximity (CM)')
figureAxis.set_xlabel('Time (Seg)')
figureAxis.set_title('TeT Lab2')

xAxisData, yAxisData = [], []


def filldata(i):
    datos = float(serialData.readline())
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
        exchange=os.environ['EXCHANGE'], routing_key=os.environ['ROUTING_PROX_KEY'], body=body)
    print("Sended data to Message Mananger")
    connection.close()


while True:
    if (serialData.inWaiting() > 0):
        ani = animation.FuncAnimation(
            sensorFigure, filldata, interval=1000)
        matPlot.show()
