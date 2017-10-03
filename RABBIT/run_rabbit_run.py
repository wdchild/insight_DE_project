from data_generator import *
from message_packager import *
from message_producer import *
from datetime import datetime

num_recs = input('How many records do you want to run? ')
data_size = str(input('Pick a data size (1, 5, 10, 50, 100, 500, 1000, 5000, 10000 kB) '))
print('Will process {} records in {} kB chunks'.format(num_recs, data_size))

''' By deciding in advance how many records you are sending, it is easier
    to determine how long it took for messages to go through each part of the pipe '''
NUM_TEST_RECORDS = int(num_recs)

''' You set a source file of your choosing. Different "chunks of numbers" have been generated.'''
DATA_SOURCE = data_size + '_kB_chunk.txt'

''' Create an artificial data generator for testing purposes.
    each record produced by the data generator contains a unique (artificial)
    message tag that makes it easy to check for missing messages later down the pipeline.'''
generator = DataGenerator(DATA_SOURCE)

''' Create a message packager to package data correctly depending on the type of data being
    sent. Thi could be numeric, image, and so forth.'''
packager = MessagePackager()

''' Create a producer that connects to the RabbitMQ server and opens a channel '''
producer = MessageProducer()

# Now start producing messages for consumption by the consumer
start_time = datetime.now()
for x in range(NUM_TEST_RECORDS):
    car_data_rec = generator.create_record() # in the form of a dictionary

    ''' In real life, message_body would take different forms depending on the type of packaging
        performed. Here packaging as a string for test purposes.'''
    message_body = packager.package_data_as_string(car_data_rec) 

    ''' Routing is based on data status (normal or error). Note that other forms of routing would
        be possible (e.g. by sensor type, or by a combination of routes)'''
    routing = packager.detect_error_status(car_data_rec)
    producer.send_message(message_body, routing) # status will tell where the message should go

# figure out how long it took
end_time = datetime.now()
time_elapsed = end_time - start_time
print('Running {} records with data {} took: {}'\
      .format(NUM_TEST_RECORDS, generator.data_source, time_elapsed))
print('Start time was: {}'.format(start_time))
print('End time was: {}'.format(end_time))
print('Compare with end time on consumer / timescale write end.')
