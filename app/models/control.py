def split_text_into_prompts(text, num_prompts):
    # Split the text into sentences
    sentences = text.split('. ')
    print("total sentences: ", len(sentences))
    
    # Calculate the number of sentences per prompt
    sentences_per_prompt = round(len(sentences) / num_prompts)
    print("sentences_per_picture: ", sentences_per_prompt)
    
    # Initialize a list to store the prompts
    prompts = []
    
    # Iterate through the prompts
    for i in range(num_prompts):
        start_idx = i * sentences_per_prompt
        end_idx = (i + 1) * sentences_per_prompt
        prompt = '. '.join(sentences[start_idx:end_idx]) + '.'
        prompts.append(prompt)
    return prompts

# text = """
# Once upon a time, there was a beautiful snow white princess. She was the fairest of them all, and the King was madly in love with her. He wanted her to be his Queen, but there was one problem. No one could find an adequate answer to his question, 'what do you see when you look in the mirror'. She was frightened by the question, but there was no way to escape it. In a panic, she ran away from the castle and was never seen again. The snow white princess was a mystery, and the King never found the answer to his question.
# """
# print(split_text_into_prompts(text, 3))