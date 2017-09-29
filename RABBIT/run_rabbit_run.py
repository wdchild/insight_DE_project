import time
from data_generator import *
from message_packager import *
from message_producer import *

''' Create an artificial data generator for testing purposes.
    each record produced by the data generator contains a unique (artificial)
    message tag that makes it easy to check for missing messages later down the pipeline.'''
generator = DataGenerator()

''' Create a message packager to package data correctly depending on the type of data being
    sent. Thi could be numeric, image, and so forth.'''
packager = MessagePackager()

''' Create a producer that connects to the RabbitMQ server and opens a channel '''
producer = MessageProducer()

NUM_TEST_RECORDS = 1000 # SET WHAT YOU WANT HERE

# Now start producing messages for consumption by the consumer
start_time = time.time()
for x in range(NUM_TEST_RECORDS):
    car_data_rec = generator.create_record() # in the form of a dictionary

    ''' In real life, message_body would take different forms depending on the type of packaging
        performed. Here packaging as a string for test purposes.'''
    message_body = packager.package_data_as_string(car_data_rec) # for testing, a string representation of data
    routing = packager.detect_error_status(car_data_rec) # routing is based on data status (normal or error)
    # note that other forms of routing would be possible (e.g. by sensor type, or by a combination of routes)
    producer.send_message(message_body, routing) # status will tell where the message should go

# figure out how long it took
end_time = time.time()
time_elapsed = end_time - start_time
print('Running {} records took: {}'.format(NUM_TEST_RECORDS, time_elapsed))
