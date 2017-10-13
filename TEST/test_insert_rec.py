import sys
sys.path.append("../TIMESCALE")
from insert_car_rec import *
import datetime

# This test should place one record in the error table and one record in the normal table.
test_rec_error={'message_num': '1', 'time_stamp': datetime.datetime.now(), 'car_id': '1', \
          'device_id': '2', 'data_type': 'lidar', 'error_flag': 1, 'data':''}

test_rec_normal={'message_num': '1', 'time_stamp': datetime.datetime.now(), 'car_id': '1', \
          'device_id': '2', 'data_type': 'lidar', 'error_flag': 0, 'data':''}

insert_car_data('error_data', test_rec_error)
insert_car_data('normal_data', test_rec_normal)
