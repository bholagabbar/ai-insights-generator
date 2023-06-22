from dotenv import load_dotenv
load_dotenv()

import os
import sys
import json
import openai
import requests
from typing import List, Tuple, Dict

# Init chatgpt bot
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read JSON config
with open('config.json') as file:
    app_config = json.load(file)

# Build text prompts from config

def process_fireflies_json_transcript(json_data):
    # Load JSON data
    sentences = [item['sentence'] for item in json_data]
    return ' '.join(sentences)


def gpt_call(messages: List[Dict[str, str]]):
    # Call GPT with large model
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-16k',
        messages=messages
    )
    answer = response["choices"][0]["message"]["content"]
    return answer

def get_insights(text_data):
    # Get insights from GPT
    idea = app_config['idea']
    system_personality = app_config['personality']
    insights_prompt = idea +  app_config['insights'] + text_data
    messages=[
        {"role": "system", "content": system_personality},
        {"role": "user", "content": insights_prompt}
    ]
    return gpt_call(messages)

def get_recommendations(text_data, insights_response):
    # Get recommendations from GPT
    idea = app_config['idea']
    system_personality = app_config['personality']
    insights_prompt = idea +  app_config['insights'] + text_data
    recommendation_prompt = app_config['recommendations']
    messages=[
        {"role": "system", "content": system_personality},
        {"role": "user", "content": idea + " " + insights_prompt},
        {"role": "assistant", "content": insights_response},
        {"role": "user", "content": recommendation_prompt}
    ]
    return gpt_call(messages)

def generate_output(input_text, insights, recs):
    file_name = f"output.txt"

    # Print insights and output to stdout
    output_text = f"\n\n======== INSIGHTS ========\n\n{insights}\n\n======== RECOMMENDATIONS ========\n\n{recs}"
    print(output_text)

    # Write everything to file
    output_text += f"\n\n======== INPUT TEXT ========\n\n{input_text}\n\n ======== END ========\n\n"
    with open(file_name, 'w') as file:
        file.write(output_text)

def get_data_from_link(json_file_or_url):
    try:
        print("Accessing URL...")
        response = requests.get(json_file_or_url, verify=False)
        response.raise_for_status()
        json_data = response.json()
        text_data = process_fireflies_json_transcript(json_data)
        print("Data retrieved from URL successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while accessing URL: {json_file_or_url}")
        print(e)
        sys.exit(1)
    except (json.JSONDecodeError, ValueError):
        print(f"Invalid JSON data at URL: {json_file_or_url}. Treating as plain text.")
        text_data = response.text

    return text_data

def main():
    text_data = None

    # Parse input
    if len(sys.argv) < 2:
        print("Please enter the text or URL hosting it:")
        text_data = input()
        if text_data.startswith("http://") or text_data.startswith("https://"):
            text_data = get_data_from_link(text_data)
    else:
        json_file_or_url = sys.argv[1]
        if json_file_or_url.startswith("http://") or json_file_or_url.startswith("https://"):
            text_data = get_data_from_link(json_file_or_url)
        else:
            try:
                with open(json_file_or_url) as file:
                    json_data = json.load(file)
                    text_data = process_fireflies_json_transcript(json_data)
            except FileNotFoundError:
                print(f"File not found: {json_file_or_url}")
                print("Please enter the text:")
                text_data = input()
            except json.JSONDecodeError:
                print(f"Invalid JSON file: {json_file_or_url}. Treating as plain text.")
                with open(json_file_or_url) as file:
                    text_data = file.read()

    if text_data is None:
        print("No text data provided. Please enter the text:")
        text_data = input()

    # Generate insights
    print("generating insights...")
    insights_response = get_insights(text_data)
    print("insights generated, now generating recommendations...")
    
    # Generate recommendations
    recommendations_response = get_recommendations(text_data, insights_response)
    print("recommendations generated, printing output...")

    # Print final output
    generate_output(text_data, insights_response, recommendations_response)
    print("Process completed.")

if __name__ == "__main__":
    main()
