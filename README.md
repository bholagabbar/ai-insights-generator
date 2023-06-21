# Fireflies Transcript Splitter

## Overview

This repository provides a Python script that takes a Fireflies transcript in JSON format, splits it into several parts, and prepares the split parts for analysis and extraction of large information using ChatGPT or other similar models. The script breaks down the transcript into manageable chunks, allowing for easier processing and analysis.

## Features

- Splits Fireflies transcript in JSON format into smaller parts
- Outputs each part as a separate text file
- Maintains the context of the transcript by including preceding and following sentences in each split

## Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/fireflies-transcript-splitter.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Place your Fireflies transcript file (in JSON format) in the same directory as the script. You can download your transcript in JSON format from the fireflies call dashboard

4. Run the script with the JSON file as an argument:

   ```shell
   python split_transcript.py your_transcript.json
   ```

5. The script will create an output folder with the same name as the JSON file (without the file extension). Inside this folder, you will find the split text files.

6. Process and analyze the split parts as needed.

## License

This project is licensed under the [MIT License](LICENSE).
