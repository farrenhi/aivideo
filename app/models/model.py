from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
import mysql.connector.pooling

# db_config = {
#             'host': os.getenv('host'), 
#             'host': 'host.docker.internal', # for docker run on local PC
#             'port': os.getenv('port'),
#             'user': os.getenv('user'), 
            
#             'password': os.getenv('password'), 
#             'database': os.getenv('database'),
#             }

db_config = {
            'host': os.getenv('rds_host'), 
            'port': os.getenv('rds_port'), 
            'user': os.getenv('rds_user'), 
            
            'password': os.getenv('rds_password'), 
            'database': os.getenv('rds_database')
            }

try:
    connection = mysql.connector.connect(**db_config)
    print("Successfully connected to MySQL server")
except Exception as e:
    print(f"Error connecting to MySQL server: {e}")

# print(db_config['database'])

# Create a connection pool
connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

# Functions to execute a query using a connection from the pool
def execute_query_create(query, data=None):
    connection = connection_pool.get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, data)
        connection.commit()
        # return True
        return cursor.lastrowid
    except Exception as e:
        connection.rollback()
        print("Error:", e)
        return False
    finally:
        cursor.close()
        connection.close()

def execute_query_create_many(query, data=None):
    connection = connection_pool.get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.executemany(query, data)
        connection.commit()
        # return True
        return cursor.lastrowid
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

def request_to_database(topic_prompt):
    '''write user-input-topic-prompt into SQL database'''
    query = "INSERT INTO request (prompt) VALUES (%s)"
    data = (topic_prompt, )
    # execute_query_create(query, data)
    # return
    last_inserted_id = execute_query_create(query, data)
    return last_inserted_id

# def generative_text_to_database(text_part, request_id):
#     '''this function would write text into SQL database'''
#     query = "INSERT INTO statement (text_part, request_id) VALUES (%s, %s)"
#     data = (text_part, request_id)
#     execute_query_create(query, data)

def generative_text_to_database(texts, request_id):
    '''this function would write text into SQL database'''
    query = "INSERT INTO statement (text_part, request_id) VALUES (%s, %s)"
    data = [(text, request_id) for text in texts]
    execute_query_create_many(query, data)

def image_link_to_database(link, story_flow_number, request_id):
    '''this function would write image link into SQL database'''
    query = "INSERT INTO image (web_link, story_flow_number, request_id) VALUES (%s, %s, %s)"
    data = (link, story_flow_number, request_id)
    execute_query_create(query, data)
    
def grab_image(request_id):
    '''Given request_id, we should get image links'''
    query = "SELECT web_link FROM image WHERE request_id = (%s)"
    data = (request_id,)
    # print(execute_query_read(query, data))
    links = [item['web_link'] for item in execute_query_read(query, data)]
    return links

def save_video_filename_database(filename, request_id):
    '''write video filename to database'''
    query = "INSERT INTO video (filename, request_id) VALUES (%s, %s)"
    data = (filename, request_id)
    execute_query_create(query, data)

def generate_cloudfront_link(distribution_domain, object_key):
    return f"https://{distribution_domain}/{object_key}"

def videolink_to_sql(cloudfront_link, request_id):
    '''write video cloudfront_link to database'''
    query = "INSERT INTO cloudfront (cloudfront_link, request_id) VALUES (%s, %s)"
    data = (cloudfront_link, request_id)
    execute_query_create(query, data)