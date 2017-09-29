'''This class contains the message producer that will be publishing the the RabbitMQ exchange.
   Messages are generated by a data generated and given to the producer to send. The speed
   at which messages are generated will be controlled by parameters passed in to the data generator. '''

import pika
import sys

# the position of error flag within a data record
ERROR_FLAG_POSITION = 5

class MessageProducer():

    def __init__(self):
        print('Creating a message producer ... {}'.format(self))
        try:
            print('Establishing a connection for producer ...\n')
            # host could be localhost or some remote address where rabbit server exists
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='<HOST>'))
            # print('Connection: {}'.format(self.connection))
            self.channel = self.connection.channel()
            # print('Channel: {}'.format(self.channel))
            self.channel.exchange_declare(exchange='car_logs', exchange_type='direct')
        except:
            print('MESSAGE PRODUCER ERROR')

    # If the first value in the tuple is 0, data is normal, else (1) indicates error
    @classmethod
    def get_message_flag(self, message):
        if message[0] == 0:
            return 'normal'
        return 'error'

    @classmethod
    def send_message(self, data_rec, record_health):
        # print('Sending message with flag: {}'.format(record_health))
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='<HOST>''))
        # print('Connection: {}'.format(self.connection))
        self.channel = self.connection.channel()
        # print('Channel: {}'.format(self.channel))
        self.channel.exchange_declare(exchange='car_logs', exchange_type='direct')
        self.channel.basic_publish(exchange='car_logs',\
                      routing_key=record_health,\
                      body=data_rec)

