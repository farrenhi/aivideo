from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.

# Connection Pool
import mysql.connector.pooling

# local parameters


db_config = {'host': os.getenv('host'), 
            'port': os.getenv('port'), 
            'user': os.getenv('user'), 
            'password': os.getenv('password'), 
            'database': os.getenv('database')}

# Create a connection pool
connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

# Functions to execute a query using a connection from the pool
def execute_query_create(query, data=None):
    connection = connection_pool.get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, data)
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        print("Error:", e)
        return False
    finally:
        cursor.close()
        connection.close()

def execute_query_read(query, data=None):
    # To request a connection from the pool, use its get_connection() method: 
    connection = connection_pool.get_connection() 
    cursor = connection.cursor(dictionary=True)
    
    mycursor = connection.cursor(dictionary=True)
    set_session_query = "SET SESSION group_concat_max_len = 1000000;"
    mycursor.execute(set_session_query)
    
    myresult = None
    try:
        cursor.execute(query, data)
        myresult = cursor.fetchall()
    except Exception as e:
        print("Error:", e)
        myresult = "error"
    finally:
        cursor.close()
        mycursor.close()
        connection.close()
        return myresult

def execute_query_update(query, data=None):
    connection = connection_pool.get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, data)
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        print("Error:", e)
        return False
    finally:
        cursor.close()
        connection.close()
        
        
def execute_query_delete(query, data=None):
    connection = rds_connection_pool.get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, data)
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        print("Error:", e)
        return False
    finally:
        cursor.close()
        connection.close()




def generative_text_to_database(text_part, request_id):
    '''this function would write text into SQL database'''
    query = "INSERT INTO statement (text_part, request_id) VALUES (%s, %s)"
    data = (text_part, request_id)
    execute_query_create(query, data)


def image_link_to_database(link, request_id):
    '''this function would write image link into SQL database'''
    query = "INSERT INTO image (web_link, request_id) VALUES (%s, %s)"
    data = (link, request_id)
    execute_query_create(query, data)
    
    
def grab_image(request_id):
    '''Given request_id, we should get image links'''
    query = "SELECT web_link  FROM image WHERE request_id = (%s)"
    data = (request_id,)
    # print(execute_query_read(query, data))
    links = [item['web_link'] for item in execute_query_read(query, data)]
    return links