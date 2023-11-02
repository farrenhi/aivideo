import requests
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
from monsterapi import client
from model import *

# test_text = 'His compassionate nature and ability to bridge divides endeared him to the nation. Lincoln''s tragic assassination in 1865 only cemented his legacy, leaving an indelible mark on the American psyche.'

def text_to_image(text_part, request_id):
    # Initialize the client with your API key
    api_key = os.getenv('monster_api_key')  # Replace 'your-api-key' with your actual Monster API key
    monster_client = client(api_key)

    # Define the model and input data
    model = 'sdxl-base'  # Replace with the desired model name
    input_data = {
        'prompt': text_part,
        'negprompt': 'deformed, bad anatomy, disfigured, poorly drawn face',
        'samples': 1,
        'steps': 50,
        'aspect_ratio': 'landscape',
        'guidance_scale': 7.5,
        'seed': 2414,
        'style': 'photographic'
    }

    # Use the generate method to retrieve the generated content
    response = monster_client.generate(model, input_data)

    # Handle the response from the API
    if 'error' in response:
        print('Error:', response['error'])
        return "error"
    else:
        generated_content = response.get('output')
        print(response)
        print('Generated content:', generated_content)
        image_link_to_database(generated_content[0], request_id)



### need to figure out request_id
    
# data output format:
# {'output': ['https://processed-model-result.s3.us-east-2.amazonaws.com/9ddb42e8-cf35-4d91-b6fd-e0235fbd59ca_0.png', 
# 'https://processed-model-result.s3.us-east-2.amazonaws.com/9ddb42e8-cf35-4d91-b6fd-e0235fbd59ca_1.png']}