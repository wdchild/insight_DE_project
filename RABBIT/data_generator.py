'''This method creates a data generator object that can either read records 
   from a file or generate (fictitious) "records" of data. The records can
   then be used to feed a message broker for testing purposes.'''

import datetime
import random

# Selects a random camera from within the range of existing cameras (1 ... n)
def random_camera (num_cameras):
    cam_num = str(random.randint(1, num_cameras))
    cam_ID = 'camera_' + cam_num
    return cam_ID

# Selects a random sensor from within the range of existing sensors (1 ... n)
def random_sensor (num_sensors):
    sen_num = str(random.randint(1, num_sensors))
    sen_ID = 'sensor_' + sen_num
    return sen_ID

# Selects a random device among all cameras and all sensors
def random_device (num_cams, num_sens):
    choice_flag = random.choice(['camera', 'sensor'])
    if choice_flag == 'camera':
        return random_camera(num_cams)
    return random_sensor(num_sens)

# Gets the type of data (image for cameras, number value for sensors)
def get_data_type (device_id):
    data_type = 'number' # assume a sensor
    if (device_id[:6] == 'camera'):
        data_type = 'image' # won't quibble about lidar vs. radar at this point
    return data_type

# Returns an error flag if the random value is below an error_percent threshold (e.g. 5%)
def determine_error_status (percent_errors):
    value = 100 * random.random()
    is_error = 0 # assume normal data
    if value < percent_errors:
        is_error = 1 # switch to abnormal data
    return is_error

# If there is an error, no data is returned for the record.
# If the record is deemed normal, then an image is appended to the data.
# This is where you'll get the image file.
def grab_image_data(error_flag):
    data = '' # assume an error
    if (error_flag == 0): # if normal data, we need an image (or number)
        source_path = 'lidar_one.jpg'
        f = open(source_path, 'rb')
        data = f.read()
    return data

def data_as_dict(fields, values):
    rec_as_dict = {}
    for f, v in zip (fields, values):
        rec_as_dict[f] = v
    return rec_as_dict

'''Separating this method because I may use something more sophisticated here later.'''
def grab_numeric_data(num_source_file):
    # SHOULD WRAP THIS IN A TRY STATEMENT IN CASE THE FILE IS MISSING
    with open(num_source_file, 'r') as fin:
        numeric_data = fin.read()
        if numeric_data.endswith('\n'): # remove \n from end if present
            numeric_data = numeric_data[:-1]
        return numeric_data

class DataGenerator():
    # Class variable
    ''' This class variable is used to generate sequential message numbers.
        These message numbers help make it easy to track whether messages are
        getting dropped somewhere along the pipeline.'''
    messages = 0

    ''' Source files for data generation are now passed in and stored as a property
        for reuse. data_source should be renamed once you start importing the image data,
        and the image data could then be stored as a separate property. If you wanted 
        different image data samples, you could store them differently (e.g. list).'''
    def __init__(self, source_file_name):
        self.data_source = source_file_name

    ''' This method creates everything in the record except the actual data itself.
        Separating the record parts in this way makes it possible to add different
        types of data (numeric, image, or nothing) depending on the data type and
        error status.'''
    def create_record_without_data(self):
        # increment the next message num from the class variable messages
        DataGenerator.messages += 1
        NUM_CAMERAS = 20 # set whatever you want depending on use case
        NUM_SENSORS = 10 # set whatever you want depending on use case
        PERCENT_ERRORS = 20 # setting high value (20%) to test routing; can reset later
        message_num = DataGenerator.messages # assigning to message_num for code clarity / brevity below
        time_stamp = str(datetime.datetime.now())
        car_id = "car_1" # temporarily only working with one car REFACTOR THIS APPROACH WITH METHOD
        device_id = random_device(NUM_CAMERAS, NUM_SENSORS)
        data_type = get_data_type(device_id)
        error_flag = determine_error_status(PERCENT_ERRORS)
        fields = ['message_num', 'time_stamp', 'car_id', 'device_id', 'data_type', 'error_flag']
        values = [message_num, time_stamp, car_id, device_id, data_type, error_flag]
        partial_record = data_as_dict(fields, values)
        return partial_record

    # This method appends numeric data to the partial data record, completing a "numeric record"
    def append_numeric_data(self, partial_record):
        if partial_record['error_flag'] == 0: # no error, so append numbers
            partial_record['data'] = grab_numeric_data(self.data_source)
        else:
            partial_record['data'] = None
        return partial_record # which is now complete :)

    def create_record(self):
        # increment the next message num from the class variable messages
        record = self.create_record_without_data()

        # once you work out image conversion issue, append different types of
        # data here depending on the device type (sensor vs camera)
        # for testing right now, just append a bunch of numbers
        self.append_numeric_data(record)

        return record

