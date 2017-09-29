'''CLASS message_unpacker

   Message bodies sent through RabbitMQ may take various forms. They were packed
   accordingly by the message_packager.

   This class reverses the process. Currently, only implemented for message bodies
   represented as strings, but could also handle various image formats in a real use
   situation

   Encapsulating the "unpacking" aspect into this class makes it easier to extend the
   functionality of methods needed for unpacking data as a function of the data types 
   (e.g. lidar, radar, numeric, GPS) that are packaged by message_packager.
'''
import pickle
import json

class MessageUnpacker():

    def __init__(self):
        print('Generating message unpacker...')

    # Unpacks messages that were packaged as a field-delimited (';') string representation
    def unpack_string_to_dict(self, incoming_values):
        FIELD_DELIMITER = ';'
        fields = ['message_num', 'time_stamp', 'car_id', 'device_id', 'data_type', 'error_flag', 'data']
        values = incoming_values.split(FIELD_DELIMITER)

        record_as_dict = {}
        # print('Fields: {}'.format(fields))
        # print('Values: {}'.format(values))

        for f, v in zip(fields, values):
            record_as_dict[f] = v
        record_as_dict['data'] = record_as_dict['data'].strip('\n') # artifact of message body
        # print(record_as_dict)

        return record_as_dict 

    # Unpacks messages that were packaged as JSON
    def unpack_json_to_dict(self, incoming_json):
        record_as_dict = json.loads(incoming_json)
        return record_as_dict

    # Unpacks messages that were pickled
    def unpickle_to_dict(self, pickled_message):
        record_as_dict = pickle.loads(pickled_message)
        return record_as_dict


