import pika

params = pika.URLParameters('amqps://yfunjwyl:sQec8gfKBkduocgGxh_PY8ajSuXimivU@seal.lmq.cloudamqp.com/yfunjwyl')
connection = pika.BlockingConnection(params)
channel = connection.channel()


channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)

print('Started consuming')
channel.start_consuming()
channel.close()