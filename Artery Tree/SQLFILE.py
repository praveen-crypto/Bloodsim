import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        # print("Connection to SQLite DB successful")
    except Error as e:
        return str(e)

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        # print("Query executed successfully")
    except Error as e:
        return str(e)

def execute_many_query(connection, query, query_list):
    cursor = connection.cursor()
    try:
        cursor.executemany(query, query_list)
        connection.commit()
        # print("Query executed successfully")
    except Error as e:
        return str(e)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        return str(e)


if __name__ == "__main__":
    import os.path
    c = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    path = os.path.join("DBS", "bloodsim.sqlite")
    connection = create_connection(path)
    query = """Update STENO set state = ? where id = ?"""
    query_list = [(c[0], 0), (c[1], 1), (c[2], 2), (c[3], 3), (c[4], 4), (c[5], 5), (c[6], 6), (c[7], 7), (0, 8), (0, 9),
                 (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18), (0, 19)]
    execute_many_query(connection, query, query_list)
    print ('UPDATED')
    # query = """ CREATE TABLE IF NOT EXISTS STENO (state BOOLEAN CHECK (state IN (0,1)),
    # val INTEGER NOT NULL); """

    # query = """ DROP TABLE STENO """
    # query = """ INSERT INTO STENO (state,val) VALUES(1, 0),(1, 0),(1, 0),(1, 0),(1, 0),(1, 0),(1, 0),(1, 0),(1, 0) """
    query = 'SELECT state FROM STENO'
    # execute_query(connection, query)
    # """ SELECT state FROM STENO   """

    state = execute_read_query(connection, query)
    print(state)






