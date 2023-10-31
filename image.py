import requests
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
from monsterapi import client
from model import *

prompt1 = "George Washington (February 22, 1732 – December 14, 1799) was an American military officer, statesman, and Founding Father who served as the first president of the United States from 1789 to 1797."

prompt2 = 'Washington did not have the formal education his elder brothers received at Appleby Grammar School in England, but he did attend the Lower Church School in Hartfield. He learned mathematics, trigonometry, and land surveying, and became a talented draftsman and mapmaker. By early adulthood, he was writing with "considerable force" and "precision".'

prompt3 = "The full Virginia Regiment joined Washington at Fort Necessity the following month with news that he had been promoted to command of the regiment and colonel upon the regimental commander's death."

# Initialize the client with your API key
api_key = os.getenv('monster_api_key')  # Replace 'your-api-key' with your actual Monster API key
monster_client = client(api_key)

# Define the model and input data
model = 'txt2img'  # Replace with the desired model name
input_data = {
    'prompt': prompt3,
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
else:
    generated_content = response.get('output')
    print(response)
    print('Generated content:', generated_content)
    # image_link_to_database(generated_content[0], request_id)

### need to figure out request_id
    
# data output format:
# {'output': ['https://processed-model-result.s3.us-east-2.amazonaws.com/9ddb42e8-cf35-4d91-b6fd-e0235fbd59ca_0.png', 
# 'https://processed-model-result.s3.us-east-2.amazonaws.com/9ddb42e8-cf35-4d91-b6fd-e0235fbd59ca_1.png']}