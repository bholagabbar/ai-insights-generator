# Fireflies Transcript Splitter


## Overview

This repository provides a Python script that takes a Fireflies transcript in JSON format or otherwise, splits it into several parts, and prepares the split parts for analysis and extraction of large information using ChatGPT or other similar models. The script breaks down the transcript into manageable chunks, allowing for easier processing and analysis.

## Features

- Splits Fireflies transcript in JSON format or regular text into smaller parts
- Outputs each part as a separate text file while also printing it out onto the console with well demarcated output lines

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

4. Run the script optionally with a JSON file as an argument. If you don't have the input file, you can run it as is and it prompts you paste the text:

   ```shell
   python split_transcript.py your_transcript.json
   ```
   or
   ```shell
   python split_transcript.py
   ```
6. The script will create an output folder with the same name as the JSON file (without the file extension). Inside this folder, you will find the split text files. It also prints the output to the console

7. Store business sensitive prompts etc in the `.prompts` file which is gitignored

8. Use GPT to analyse the transcript outputs using the prompts

## Additional Usage Notes

* #### Pushing to git when global config is set for another user
  * `git config --local user.name ""`
  * `git config --local user.email ""`
  * Store token in `.githubinfo` along with potentially other git information
  * `git push https://bholagabbar@github.com/bholagabbar/fireflies-transacript-splitter` and enter password

## License

This project is licensed under the [MIT License](LICENSE).
