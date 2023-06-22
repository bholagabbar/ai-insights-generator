from dotenv import load_dotenv
load_dotenv()

import os
import sys
import json
import random
from typing import List, Tuple
from lwe import ApiBackend as ChatGpt

# Specify the maximum number of words per file
MAX_WORDS_FOR_PART = 2000

# Read JSON config
with open('config.json') as file:
    app_config = json.load(file)

# Extract config
idea = app_config['idea']
prompts_first = app_config['prompts']['first']
prompts_next = app_config['prompts']['next']
prompt_aggregate = app_config['prompts']['aggregate'][0]

# Init chatgpt bot
gpt = ChatGpt()


def gpt_call(input_text):
    # Call chat gpt
    success, response, message = gpt.ask(input_text)
    if success:
        print(f"chatgpt response is {response}")
        return response
    else:
        raise RuntimeError(message)

def generate_insights_for_summary(prompt, summary) -> str:
    try:
        response = gpt_call(prompt + " " + summary)
        return response
    except Exception as e:
        print(f"Error getting insights from gpt: {e}")
        return ""

def process_json(json_data):
    # Load JSON data
    sentences = [item['sentence'] for item in json_data]
    return ' '.join(sentences)

def get_insights_for_chunks(text_data):
    # Split the text into chunks of maximum specified words
    words = text_data.split()
    chunks = [words[i:i+MAX_WORDS_FOR_PART] for i in range(0, len(words), MAX_WORDS_FOR_PART)]
    if len(chunks[-1]) < 500:
        chunks[-2] += chunks[-1]
        chunks.pop()

    print(f"Total chunks: {len(chunks)}")

    # Initialize aggregated insights
    aggregated_insights = ""

    # Get insights for each chunk
    for i, chunk in enumerate(chunks):
        chunk_content = ' '.join(chunk)

        # Select prompt
        if i == 0:
            prompt = idea + " " + random.choice(prompts_first)
        else:
            prompt = random.choice(prompts_next)

        # Get insights
        insights = generate_insights_for_summary(prompt, chunk_content)

        # Append insights to aggregated insights
        aggregated_insights += insights + "\n"

        # Append to output file
        write_output_with_insights(i+1, insights, chunk_content)

        print(f"chunk {i+1} processed.")

    print(f"{len(chunks)} chunks processed.")

    # Generate aggregate insights
    aggregate_insights = generate_insights_for_summary(prompt_aggregate, aggregated_insights)

    # Write the aggregate insights to a separate file
    write_output_with_insights("aggregate", aggregate_insights, "")
    print(f"Aggregate insights generated.")


def write_output_with_insights(num, insights, output):
    if num == "aggregate":
        file_name = "output_aggregate_insights.txt"
    else:
        file_name = f"output_w_insights_{num}.txt"

    output_text = f"\n\n======== {num} ===========\n\n{output}\n\n======== INSIGHTS ========\n\n{insights}\n\n"
    print(f"\n======== INSIGHTS {num}========")
    print(insights)

    with open(file_name, 'w') as file:
        file.write(output_text)

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

    # Generate insights for each chunk
    get_insights_for_chunks(text_data)

    # Print final output
    print("Process completed.")

if __name__ == "__main__":
    main()
