import mysql.connector
from mysql.connector import Error
import pandas as pd
import Config

def execute_list_query(connection, query, values):
    cursor = connection.cursor()
    try:
        cursor.executemany(query, values)
        connection.commit()
        print('success!!')
    except Error as err:
        print(f"Error: '{err}'")


sql = '''
    INSERT INTO teacher (teacher_id, first_name, last_name, language_1, language_2, dob, tax_id, phone_no) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''

val = [
    (7, 'Hank', 'Dodson', 'ENG', None, '1991-12-23', 11111, '+491772345678'),
    (8, 'Sue', 'Perkins', 'MAN', 'ENG', '1976-02-02', 22222, '+491443456432')
]


connection = Config.create_server_connection(
    'localhost', 'root', 'Ro@mysql@081', 'python_integration')
execute_list_query(connection, sql, val)

# The resemblance to the '%s' placeholder for a string in python is just coincidental 
# (and frankly, very confusing), we want to use '%s' for all data types (strings, ints, dates, etc) 
# with the MySQL Python Connector. 
