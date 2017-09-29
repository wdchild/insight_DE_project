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

Need to fix:
- broken import links due to file reorganization


