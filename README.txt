INSIGHT DATA ENGINEERING PROJECT: Daniel Child

This project seeks to test a configuration that would make it possible to stream
data from prototype self-driving cars. Data is supposed to run to a RabbitMQ broker,
and depending on whether the data has an error flag set to 1 (done internally by
the car), log records are routed from the broker to either a "normal" data table
or an "error" data table. On the RabbitMQ consumer end, data is then sent to a
timestamp-optimized version of Postgres known as TimescaleDB.

Code and resources are in one of four categories (and corresponding directories):
-- RABBIT (for data generation, rabbit producers, and rabbit consumers)
-- TIMESCALEDB (for inserting data into TimescaleDB)
-- TEST (for individual unit tests)
-- SEED (for seed data used in data generation)

Note that import links were broken when organizing the data for github.
Broken links could be fixed by using import sys followed by a description of the 
path, so that it would be possible to travel up one directory and back down another.
Unfortunately, 'project time' has ended.

e.g. 
import sys
sys.path.append(~/INSIGHT_DE_PROJECT/<DIRECTORY>)
from <DIRECTORY> import <THE MODULE IN QUESTION>

How to use:
(1) First you need to set up the TimescaleDB database with the correct fields. 
    (See the records produced by data generator.) Be sure to include a primary key serial field.
    Also be sure to create a hypertable (see TimescaleDB instructions).

(2) Run the RabbitMQ  error consumer and normal consumer. These consume normal and error messages
    from the producer.

(3) Run the producer. To do this, choose either run_rabbit_run.py or run_rabbit_races.py.
    For the latter, you can specify multiple data batch sizes as command line arguments.
    The former lets you specify the data size (chunks) as well as the number of records 
    in the batch.

(4) Seed data of different sizes is provided in the SEED folder. Choose whichever
    message size you want to test. run_rabbit_run.py makes this easy to do.


