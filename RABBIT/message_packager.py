'''CLASS message_packager

   The data generator class creates records in the form of a Python dictionary.
   One field in that record is 'data', its value beingthe data being conveyed. However, 
   depending on where the data originated from (lidar camera, GPS sensor, radar camera, 
   and so forth) the nature of that data will be different. Sometimes it is in the form of an image,  
   other times it is just numbers.

   As it turns out, the body (content) of a RabbitMQ message can only be a string or a 
   stream of bytes. Things like Python dictionaries are not hashable. So this class is designed
   to "package" the message in a way that makes it compatible with RabbitMQ.

   In the case of numeric data, it could be sent as a string, or the dictionary could be pickled,
   or it could be serialized using JSON dumps.

   Encapsulating the "packaging" aspect into this class makes it easier to pick and choose the
   way you want to package the messages without having to rewrite the data code. The packaging method
   can therefore be chosen as a function of the data type (e.g. lidar, radar, numeric, GPS). Separating
   the packaging methods also makes it possible to flexibly handle new types of data that may be generated 
   in the future.'''

import pickle
import json

class MessagePackager():

    def __init__(self):
        print('Generating a message packager.')

    def detect_error_status(self, dict_record):
        if dict_record['error_flag'] == 1:
            return 'error'
        return 'normal'

    def package_data_as_string(self, dict_record):
        FIELD_DELIMITER = ';'
        RECORD_DELIMITER = '\n'
        # print('Packaging record as string.')
        fields = ['message_num', 'time_stamp', 'car_id', 'device_id', 'data_type', 'error_flag']

        # There's a more elegant (.join) way to do this, but you need to return strings for
        # the numeric values, which complicates join. Need to refactor this later when (if) you have time.
        # REFACTOR WHEN YOU HAVE TIME

        string_rec = ''
        string_rec += str(dict_record['message_num']) + FIELD_DELIMITER
        string_rec += dict_record['time_stamp'] + FIELD_DELIMITER
        string_rec += dict_record['car_id'] + FIELD_DELIMITER
        string_rec += dict_record['device_id'] + FIELD_DELIMITER
        string_rec += dict_record['data_type'] + FIELD_DELIMITER
        string_rec += str(dict_record['error_flag']) + FIELD_DELIMITER
        if dict_record['data'] == None: # error flag was 0, so no data
            string_rec += ''
        else:
            string_rec += str(dict_record['data']) # NOTE: must be numeric for this to work as string!
        string_rec += RECORD_DELIMITER
        return string_rec

    def package_data_as_JSON(self, dict_record):
        # print('Packaging record as JSON.')
        json_rec = json.dumps(dict_record)
        return json_rec

    def package_data_with_pickle(self, dict_record):
        print('Packaging with pickle.')
        pickled_rec = pickle.dumps(dict_record)
        return pickled_rec

    def package_message(self, status, body):
        return (status, body)




