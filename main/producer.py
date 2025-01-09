# amqps://yfunjwyl:sQec8gfKBkduocgGxh_PY8ajSuXimivU@seal.lmq.cloudamqp.com/yfunjwyl

import pika, json

params = pika.URLParameters('amqps://yfunjwyl:sQec8gfKBkduocgGxh_PY8ajSuXimivU@seal.lmq.cloudamqp.com/yfunjwyl')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)

