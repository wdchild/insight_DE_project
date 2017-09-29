#1/usr/bin/python

# This script creates two tables, one for error data and the other for
# normal data.
import psycopg2

try:
    conn=psycopg2.connect(dbname="<DB NAME>", \
                          user="<USER NAME>", \
                          password="<PASSWORD>", \
                          host="<HOST>", \
                          port="<PORT>")
    print("Opened database successfully.")
    cur = conn.cursor()
    print("Cursor is: {}".format(cur))

    # Create the table that will hold "normal" data.
    cur.execute('''CREATE TABLE normal_data (
                id serial PRIMARY KEY,
                message_num BIGINT,
                time_stamp TIMESTAMPTZ NOT NULL,
                car_id VARCHAR(25),
                device_id VARCHAR(25),
                data_type VARCHAR(25),
                error_flag SMALLINT,
                data  BYTEA
                );''')

    # Create the table that will hold "error" data.
    cur.execute('''CREATE TABLE error_data (
                id serial PRIMARY KEY,
                message_num BIGINT,
                time_stamp TIMESTAMPTZ NOT NULL,
                car_id VARCHAR(25),
                device_id VARCHAR(25),
                data_type VARCHAR(25),
                error_flag SMALLINT,
                data  BYTEA
                );''')

    conn.commit()
    conn.close()

except psycopg2.Error as e:
    print(e)
