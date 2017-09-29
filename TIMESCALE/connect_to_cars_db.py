#!/usr/bin/python

import psycopg2

try:
    conn=psycopg2.connect(dbname="<DB NAME>", \
                          user="<USER NAME>", \
                          password="<PASSWORD>", \
                          host="<HOST>", \
                          port="<PORT>")
    print("Opened database successfully.")

except psycopg2.Error as e:
    print(e)
