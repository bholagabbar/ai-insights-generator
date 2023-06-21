import sys
import json

def create_text_files(json_data, max_words_per_file):
    # Load JSON data
    sentences = [item['sentence'] for item in json_data]
    
    # Join all sentences into a single string
    text = ' '.join(sentences)
    
    # Split the text into chunks of maximum specified words
    words = text.split()
    chunks = [words[i:i+max_words_per_file] for i in range(0, len(words), max_words_per_file)]
    
    # Create separate text files for each chunk
    for i, chunk in enumerate(chunks):
        file_name = f"output_{i+1}.txt"
        with open(file_name, 'w') as file:
            file.write(' '.join(chunk))

    print(f"{len(chunks)} files created.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <json_file>")
        return

    json_file = sys.argv[1]

    try:
        with open(json_file) as file:
            json_data = json.load(file)
    except FileNotFoundError:
        print(f"File not found: {json_file}")
        return
    except json.JSONDecodeError:
        print(f"Invalid JSON file: {json_file}")
        return

    # Specify the maximum number of words per file
    max_words = 3500

    # Create text files
    create_text_files(json_data, max_words)

if __name__ == "__main__":
    main()

