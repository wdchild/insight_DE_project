#!/usr/bin/env python3
from data_generator import *
from message_packager import *
import time
import sys

dg = DataGenerator()
packager = MessagePackager()

start_time = time.time()

for x in range(1):
    # data generator prepares a record taking the form of a python dictionary
    rec_as_dict = dg.create_record()

    # message packager packages it as a string
    rec_as_str = packager.package_data_as_string(rec_as_dict)
    status = packager.detect_error_status(rec_as_dict)
    message = packager.package_message(status, rec_as_str)
    print('data error status is {}'.format(status))

    # packager can also package as json (can Rabbit handle json?)
    json_rec = packager.package_data_as_JSON(rec_as_dict)
    unpacked = json.loads(json_rec)

    # for images, will need to serialize with pickle (can Rabbit handle this?)
    pickled_rec = packager.package_data_with_pickle(rec_as_dict)
    unpickled = pickle.loads(pickled_rec)

    # check the record size (for transfer rate metrics)
    print('dictionary size {} type {}\n'.format(sys.getsizeof(rec_as_dict), type(rec_as_dict)))
    print('string size {} type {}\n'.format(sys.getsizeof(rec_as_str), type(rec_as_str)))
    print('json size {} type {}\n'.format(sys.getsizeof(json_rec), type(json_rec)))
    print('unpacked size {} type {}\n'.format(sys.getsizeof(unpacked), type(unpacked)))
    print('pickled size {} type {}\n'.format(sys.getsizeof(pickled_rec), type(pickled_rec)))
    print('unpickled size {} type {}\n'.format(sys.getsizeof(unpickled), type(unpickled)))

    # show the message
    print(message)

end_time = time.time()
time_elapsed = end_time - start_time
print('Process took {} to complete'.format(time_elapsed))

