def split_text_into_prompts(text, num_prompts):
    # Split the text into sentences
    text = text.replace("\n", "")
    cleaned_text = text.replace(". ", ".")
    print("pretreatment:", repr(cleaned_text))
    
    # print(cleaned_text)
    sentences = cleaned_text.split('.')
    total_sentences = len(sentences) - 1 # it has one more after .
    print("total sentences: ", total_sentences)
    
    # Calculate the number of sentences per prompt
    sentences_per_prompt = round(total_sentences / num_prompts)
    print("sentences_per_picture: ", sentences_per_prompt)
    
    # Initialize a list to store the prompts
    prompts = []
    
    # Iterate through the prompts
    for i in range(num_prompts):
        start_idx = i * sentences_per_prompt
        
        if i == num_prompts - 1:
            prompt = '. '.join(sentences[start_idx:])
        else:
            end_idx = (i + 1) * sentences_per_prompt
            prompt = '. '.join(sentences[start_idx:end_idx]) + '.'
        prompts.append(prompt)
          
    # for i in range(num_prompts):
    #     print(i)
    #     if i == num_prompts - 1:
    #         prompt = '. '.join(sentences[i:])
    #         prompts.append(prompt)
    #     # Construct the prompt by popping sentences from the list
    #     else:
    #         prompt = '. '.join(sentences[i: i + 1]) + '.'
    #         prompts.append(prompt)
    #     # Remove the used sentences from the list
    #     # sentences = sentences[i + 1:]
   
    return prompts

# text = """Once upon a time, there was a beautiful young woman named Snow White. Her stepmother, the Evil Queen, was very jealous of Snow White's beauty and poisoned her. Snow White fell into a deep sleep and was only saved when a prince came along and kissed her. The Evil Queen was then killed by lightning, and Snow White and the prince lived happily ever after."""
# a = split_text_into_prompts(text, 3)

# print(repr(a))
# print(repr(a[0]))
# print(repr(a[1]))
# print(repr(a[2]))
# # split_text_into_prompts(text, 3)