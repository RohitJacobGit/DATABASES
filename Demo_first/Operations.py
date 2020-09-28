import Config
import pandas as pd

connection = Config.create_server_connection('localhost', 'root', 'Ro@mysql@081', 'python_integration')
#query = 'SELECT * FROM course'
query = """SELECT course.course_id, course.course_name, course.language, client.client_name, client.address
FROM course
JOIN client
ON course.client = client.client_id
WHERE course.in_school = FALSE
"""
data_retrieved = Config.read_table(connection, query)
data_retrieved_list = []

for result in data_retrieved:
    # print(result)
    #result = list(result)
    data_retrieved_list.append(result)

# print(data_retrieved_list)

data_retrieved_dataframe = pd.DataFrame(data_retrieved_list, columns=[
                                        "course_id", "course_name", "language", "client_name", "address"])

print(data_retrieved_dataframe)


update = """
UPDATE client 
SET address = '23 Fingiertweg, 14534 Berlin' 
WHERE client_id = 101;
"""

connection = Config.create_server_connection(
    'localhost', 'root', 'Ro@mysql@081', 'python_integration')
Config.execute_query(connection, update)


delete_course = """
DELETE FROM course 
WHERE course_id = 20;
"""

connection = Config.create_server_connection(
    'localhost', 'root', 'Ro@mysql@081', 'python_integration')
Config.execute_query(connection, delete_course)


