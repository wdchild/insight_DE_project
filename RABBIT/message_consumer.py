import pika
import sys
from message_unpacker import *
from insert_car_rec import *

class MessageConsumer():

    def __init__(self, topic):
        print('Creating a message consumer with topic \'{}\' ... {}'.format(topic, self))
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='<HOST>'))
            channel = connection.channel()
            channel.exchange_declare(exchange='car_logs', exchange_type='direct')
            result = channel.queue_declare(exclusive=True)
            queue_name = result.method.queue
            channel.queue_bind(exchange='car_logs', queue=queue_name, routing_key=topic)
            print(' ... Waiting for logs. To exit press CTRL+C')
            channel.basic_consume(callback, queue=queue_name, no_ack=True)
            channel.start_consuming()
        except Exception as err:
            print('MESSAGE CONSUMER ERROR:\n{}'.format(err))

def callback(ch, method, properties, body):
    print(" ... channel: {}".format(ch))
    print(" ... routing key: {}".format(method.routing_key))
    print(" ... body is: {}".format(body))
    unpacker = MessageUnpacker()
    # for testing, just unpacking string represented messages (with numerica data as data)
    dict_record = unpacker.unpack_string_to_dict(body)
    print(dict_record)
    dest_table = ''
    if method.routing_key == 'error':
    	dest_table = 'error_data'
    else:
        dest_table = 'normal_data'
    print('WANT TO INSERT RECORD HERE:\n')
    insert_car_data(dest_table, dict_record)
