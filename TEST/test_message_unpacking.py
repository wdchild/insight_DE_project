# Simply tests that message unpacker works properly
from message_unpacker import *

data_as_string = '1;2017-09-29 03:42:08.638426;car_1;sensor_8;number;0;13049871230948710329487130948123409812734019283741098374012987341023984130984712309481720398471034987\n'

unpacker = MessageUnpacker()

data_as_dict = unpacker.unpack_string_to_dict(data_as_string)
print(data_as_dict)
