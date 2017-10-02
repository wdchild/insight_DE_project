''' This script makes it easy to run a sries of tests on the RabbitMQ producer end.
    Here, one sets a "chunk of data" to use as the data portion of the messages
    being sent, and then runs a series of batches, each having a different number
    of messages in them (e.g. 1000, 10000, etc.). This gives one the ability to see
    whether Rabbit gets bogged down if there are longer streams of events being sent.
    Changing the size of the "chunk of data" enables you to also see the effect of
    message size.'''


import sys
from datetime import datetime
from data_generator import *
from message_packager import *
from message_producer import *


def run_one_batch(num_records, data_source_file):

    # Create a data generator
    generator = DataGenerator(data_source_file)

    # Create a message packager
    packager = MessagePackager()

    # Create a message producer
    producer = MessageProducer()

    # Now start producing messages for consumption by the consumer
    start_time = datetime.datetime.now()
    for x in range(num_records):
        car_data_rec = generator.create_record() # in the form of a dictionary

        # Test with string messages
        message_body = packager.package_data_as_string(car_data_rec)
        routing = packager.detect_error_status(car_data_rec)
        producer.send_message(message_body, routing)

    # figure out how long it took
    end_time = datetime.datetime.now()
    time_elapsed = end_time - start_time
    print('Running {} records containing {} took: {}'.format(num_records, generator.data_source, time_el$
    print('Start time was: {}'.format(start_time))
    print('End time was: {}'.format(end_time))
    print('Compare with end time on consumer / timescale write end.')


DATA_SOURCE_FILE = '100_kB_chunk.txt' # chane to whichever size you want to test
num_args = len(sys.argv) - 1
rec_batches_to_test = sys.argv[1:]
rec_batches_to_test = [int(i) for i in rec_batches_to_test]
print('{} races to run'.format(num_args))
print(rec_batches_to_test)

for num_recs in rec_batches_to_test:
    run_one_batch(num_recs, DATA_SOURCE_FILE)
