# import pprint
import google.generativeai as palm
# import requests
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.

def prompt_to_text(prompt):
    palm.configure(api_key=os.getenv('palm_api_key'))
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    # print(model)

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=200,
    )

    print("GPT:", completion.result)
    
    words_count = count_words(completion.result)
    print("words count:", words_count)
    
    return completion.result

def count_words(statement):
    words = statement.split()
    return len(words)
