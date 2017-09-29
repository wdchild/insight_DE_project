#!/usr/bin/python

import psycopg2
import time


# Constructs the INSERT statement for Postgres depending on the destination table.
# Insertion conforms to one of the "safe" approaches recommended.
def construct_sql_stmt(dest_table):
    print('In construct_sql_stmt dest_table is {}'.format(dest_table))
    insert_stmt = ''
    if dest_table == "normal_data":
        print('Entering normal_data branch.')
        insert_stmt = """
                    INSERT into
                        normal_data
                        (message_num, time_stamp, car_id, device_id, data_type, error_flag, data)
                    VALUES
                        (%(message_num)s, %(time_stamp)s, %(car_id)s, %(device_id)s, %(data_type)s, %(error_flag)s, %(data)s)
                    """
    elif dest_table == "error_data":
        print('Entering error_data branch.')
        insert_stmt = """
                    INSERT into
                        error_data
                        (message_num, time_stamp, car_id, device_id, data_type, error_flag, data)
                    VALUES
                        (%(message_num)s, %(time_stamp)s, %(car_id)s, %(device_id)s, %(data_type)s, %(error_flag)s, %(data)s)
                    """
    else:
        print('ERROR: unknown table destination!!!') # convert to try / except
        insert_stmt = None
    print('Selected insert statment:\n'.format(insert_stmt))
    return insert_stmt

# This method flexibly allows you to insert data into either table
def insert_car_data(dest_table, dict_rec):
    sql = construct_sql_stmt(dest_table)
    print('In insert_car_data sql statement is {}'.format(sql))

    if sql is not None:
        try:
            conn=psycopg2.connect(dbname="<DB NAME>", \
                                  user="<USER NAME>", \
                                  password="<PASSWORD>", \
                                  host="<HOST>", \
                                  port="<PORT>")
            print("Opened database successfully.")
            cur = conn.cursor()
            print('cursor is {}'.format(cur))
            print('INSERTING DATA:  {}'.format(dict_rec))
            cur.execute(sql, dict_rec)
            conn.commit()
            conn.close()

        except psycopg2.Error as e:
            print(e)

