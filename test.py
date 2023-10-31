from model import *


response = {'output': ['https://processed-model-result.s3.us-east-2.amazonaws.com/9ddb42e8-cf35-4d91-b6fd-e0235fbd59ca_0.png', 
'https://processed-model-result.s3.us-east-2.amazonaws.com/9ddb42e8-cf35-4d91-b6fd-e0235fbd59ca_1.png']}

generated_content = response.get('output')

# # save other picture
# link = 'https://processed-model-result.s3.us-east-2.amazonaws.com/feda1ed6-dcf5-476b-8594-54279a90d3ae_0.png'
# image_link_to_database(link, 1)

# image_link_to_database(generated_content[0], 1)

print(grab_image(1))