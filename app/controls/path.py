output = f'static/audio/{timestamp}.txt'
output = os.path.join(os.getcwd(), 'app', 'static', 'audio', f'{timestamp}.mp3')

def save_text_to_file(text, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print(f'Text saved to {file_path}')
    except Exception as e:
        print(f'Error: {e}')

# Example usage:
text = "This is some example text."
file_path = "example.txt"
save_text_to_file(text, file_path)
