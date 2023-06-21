import sys
import json

def create_text_files(text_data, max_words_per_file):
    # Split the text into chunks of maximum specified words
    words = text_data.split()
    chunks = [words[i:i+max_words_per_file] for i in range(0, len(words), max_words_per_file)]
    
    # Create separate text files for each chunk
    for i, chunk in enumerate(chunks):
        file_name = f"output_{i+1}.txt"
        with open(file_name, 'w') as file:
            file_content = ' '.join(chunk)
            file.write(file_content)

        # Print the content to the console
        print("\n\n======== OUTPUT {} ===========\n\n{}\n\n".format(i+1, file_content))

    print(f"{len(chunks)} files created.")

def process_json(json_data):
    # Load JSON data
    sentences = [item['sentence'] for item in json_data]
    return ' '.join(sentences)

def main():
    text_data = None
    if len(sys.argv) < 2:
        print("No file provided. Please enter the text:")
        text_data = input()
    else:
        json_file = sys.argv[1]
        try:
            with open(json_file) as file:
                json_data = json.load(file)
                text_data = process_json(json_data)
        except FileNotFoundError:
            print(f"File not found: {json_file}")
            print("Please enter the text:")
            text_data = input()
        except json.JSONDecodeError:
            print(f"Invalid JSON file: {json_file}. Treating as plain text.")
            with open(json_file) as file:
                text_data = file.read()

    # Specify the maximum number of words per file
    max_words = 2000

    # Create text files
    create_text_files(text_data, max_words)

if __name__ == "__main__":
    main()
