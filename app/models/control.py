def split_text_into_prompts(text, num_prompts):
    # Split the text into sentences
    text = text.replace("\n", "")
    cleaned_text = text.replace(". ", ".")
    
    # print(cleaned_text)
    sentences = cleaned_text.split('.')
    print("total sentences: ", len(sentences))
    
    # Calculate the number of sentences per prompt
    sentences_per_prompt = round(len(sentences) / num_prompts)
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

# text = """
# Once upon a time, there was a young girl named Cinderella who lived with her stepmother and two stepsisters. Her stepmother was a cruel woman who made Cinderella do all the chores and treated her like a servant. Cinderella's stepsisters were also very mean to her and made fun of her for being poor and wearing rags.

# One day, a ball was announced at the palace. All the young women in the kingdom were invited, including Cinderella's stepsisters. Cinderella was very excited to go to the ball, but her stepmother refused to let her. She said that Cinderella was too dirty and ragged to attend 
# such a grand event.

# Cinderella was heartbroken. She went to her room and cried. Suddenly, her fairy godmother appeared. She waved her magic wand and transformed Cinderella's rags into a beautiful ball gown. She gave Cinderella a pair of glass slippers and told her that she would have to leave the ball by midnight, or the magic would wear off.

# Cinderella went to the ball and danced with the prince all night long. The prince was smitten with Cinderella and didn't want her to leave. However, Cinderella remembered the fairy godmother's warning and rushed out of the palace at midnight. As she ran down the steps, one of her glass slippers fell off.

# The next day, the prince went from house to house, looking for the woman who fit the glass slipper. When he came to Cinderella's house, her stepsisters tried to hide her, but the prince found her. Cinderella put on the glass slipper and it fit perfectly. The prince and Cinderella were married and lived happily ever after.
# """
# a = split_text_into_prompts(text, 3)

# print(repr(a[0]))
# print(repr(a[1]))
# print(repr(a[2]))
# split_text_into_prompts(text, 3)