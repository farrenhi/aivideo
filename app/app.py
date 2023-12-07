from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.

import boto3
from datetime import datetime
from werkzeug.utils import secure_filename
import time

### Connection Pool
import mysql.connector.pooling
from make2 import *
from multi_make import *
from models.uploadtos3 import *
import asyncio
import cProfile

app = Flask(
    __name__,
    static_folder = "static",
    static_url_path = "/static",
)

@app.route("/") # , methods=["GET"]
def index():
    return render_template("index.html")
    # return "index page!"

@app.route('/api/shooting', methods=['POST'])
async def get_attractions():
    ### code box
    # code = request.args.get('code', '')
    # if code != os.getenv('website_code'):
    #     print("entered code:", code)
    #     return jsonify("error code!")
    
    prompt = request.args.get('keyword', '')
    prompt = prompt + ' and explain between 75 to 100 words.'
    print(prompt)
    
    ### comment out when testing
    # output_file_path, video_filename, request_id = make_video(prompt)
    
    output_file_path, video_filename, request_id = run_threads(prompt)
    cloudfront_link = upload_to_s3_and_get_cloudfront_link(output_file_path, video_filename, request_id)
    ###
    
    # await asyncio.sleep(3)
    # cloudfront_link = "https://login-aws-docker.s3.us-west-2.amazonaws.com/video_20231106_132728.mp4"
   
    response = {
        "data": cloudfront_link,
        # "data_backup": output_file_path,
    }
    
    return jsonify(response)

# def get_attractions():
#     code = request.args.get('code', '')
#     if code != os.getenv('website_code'):
#         print("entered code:", code)
#         return jsonify("error code!")
    
#     prompt = request.args.get('keyword', '')
#     prompt = prompt + ' and explain between 75 to 100 words.'
#     print(prompt)
    
#     ### comment out when testing
#     # output_file_path, video_filename, request_id = make_video(prompt)
#     # cloudfront_link = upload_to_s3_and_get_cloudfront_link(output_file_path, video_filename, request_id)
#     ##
    
#     cloudfront_link = "https://login-aws-docker.s3.us-west-2.amazonaws.com/video_20231106_132728.mp4"

#     time.sleep(3)
    
#     response = {
#         "data": cloudfront_link,
#         "data_backup": output_file_path,
#     }
    
#     return jsonify(response)

# run server
app.run(host="0.0.0.0", port=3003, debug=True)
