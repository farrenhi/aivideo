from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.

import boto3
from datetime import datetime
from werkzeug.utils import secure_filename

### Connection Pool
import mysql.connector.pooling

app = Flask(
    __name__,
    static_folder = "static",
    static_url_path = "/static",
)

@app.route("/") # , methods=["GET"]
def index():
    return render_template("index.html")
    # return "index page!"


@app.route('/api/attractions', methods=['GET'])
def get_attractions():
    keyword = request.args.get('keyword', '')
    print(keyword)
    return jsonify(keyword)


# # Initialize S3 client
# s3 = boto3.client(
#     "s3",
#     aws_access_key_id = os.getenv('s3_access'),
#     aws_secret_access_key = os.getenv('s3_secret'),
# )

# # RDS
# app.secret_key = os.getenv('app_secret_key') # session would need this!
# rds_db_config = {'host': os.getenv('rds_host'), 
#                  'port': 3306, 
#                  'user': os.getenv('rds_user'), 
#                  'password': os.getenv('rds_password'), 
#                  'database': os.getenv('rds_database')}
# rds_connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool_rds", pool_size=5, **rds_db_config)

# run server
app.run(host="0.0.0.0", port=3000, debug=True)
