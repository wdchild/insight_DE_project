#!/usr/bin/env python3

from data_generator import *
import time
import sys

DATA_SOURCE_FILE = '1000_kB_chunk.txt'
dg = DataGenerator(DATA_SOURCE_FILE)

start_time = time.time()

for x in range(1):
    # data generator prepares a record taking the form of a python dictionary
    rec_as_dict = dg.create_record()
    print(rec_as_dict)
    print('dictionary size {} type {}\n'.format(sys.getsizeof(rec_as_dict), type(rec_as_dict)))


end_time = time.time()
time_elapsed = end_time - start_time
print('Process took {} to complete'.format(time_elapsed))
