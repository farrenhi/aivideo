from model import *

def split_text_into_prompts(text, num_prompts):
    # Split the text into sentences
    sentences = text.split('. ')
    
    # Calculate the number of sentences per prompt
    sentences_per_prompt = len(sentences) // num_prompts
    
    # Initialize a list to store the prompts
    prompts = []
    
    # Iterate through the prompts
    for i in range(num_prompts):
        start_idx = i * sentences_per_prompt
        end_idx = (i + 1) * sentences_per_prompt
        prompt = '. '.join(sentences[start_idx:end_idx]) + '.'
        prompts.append(prompt)
    return prompts