from bardapi import Bard
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.


### bard api key is from local cookies. it is unofficial chanel.
token = os.getenv('bard_api_key')
bard = Bard(token=token)
bard.get_answer("Please tell me the story of Snow White in 150 words.")['content']