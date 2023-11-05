from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.

import boto3
from datetime import datetime
from werkzeug.utils import secure_filename

### Connection Pool
import mysql.connector.pooling
from make2 import *
from models.uploadtos3 import *

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
    prompt = request.args.get('keyword', '')
    print(prompt)
    
    output_file_path, video_filename, request_id = make_video(prompt)
    
    cloudfront_link = upload_to_s3_and_get_cloudfront_link(output_file_path, video_filename, request_id)
  
    ### to be changed to cloudfront_link
    response = {
    "data": output_file_path
    }
    
    return jsonify(response)

# run server
app.run(host="0.0.0.0", port=3000, debug=True)
