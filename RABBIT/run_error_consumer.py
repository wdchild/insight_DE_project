from message_consumer import *

# Create the message consumer for data records flagged with errors...
mc_errors = MessageConsumer(topic='error')

# Note that the producer and each consumer need to be started up from another terminal.
