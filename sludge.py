import os
import requests
import psycopg2


try:
    with psycopg2.connect('postgresql://uqncvrehjtrbtpjg:nokerbqermgsvnej@5.161.119.174:8004/cvuugpihdcqkhmnv') as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM bands')
            mybands = cursor.fetchall()

            for band in mybands:
                    sql = """ INSERT INTO userbands (user_id, band_id, band_name, band_selected) VALUES (%s, %s, %s, %s)"""
                    cursor.execute(sql, (1, band[0], band[1], True))
                    conn.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print(f"An error occurred: {error}")
