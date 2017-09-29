from message_consumer import *

# Create the message consumer for data records flagged as normal ...

mc_normal = MessageConsumer(topic='normal')

# Note that the producer and each consumer need to be started up from another terminal.
