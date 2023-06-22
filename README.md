# ai-insights-generator

Deployed on https://replit.com/@bholagabbar/ai-insights-generator . Fork the repl, change the configuration and it should be good to go

## Overview

This script accepts large input data, such as customer research calls or transcripts from various sources (eg from [fireflies ai](https://fireflies.ai/)), and generates insights and recommendations based on the provided data. It can handle input data from the following sources: HTTP(S) URLs, local files, or user input prompts. The script utilizes the OpenAI API to interact with the `gpt-3.5-turbo-16k` model and generate these insights and recommendations.

## Use Cases

- Customer Research Calls: Derive insights and focus areas from customer research calls or transcripts to drive startup success.
- Market Research: Analyze surveys, reports, and competitor data to generate insights for informed business decisions.
- User Feedback Analysis: Process support tickets, online reviews, and social media feedback to improve products/services.
- Strategy Development: Utilize industry reports, trends, and expert opinions to inform strategic decision-making.


## Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/bholagabbar/ai-insights-generator.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Run the script optionally research document file as an argument, or a link to a a transcript. If you don't have either, you can run it as is, and it will prompt you to paste the text or URL:

   ```shell
   python main.py
   ```
   or
   ```shell
   python main.py https://jsonkeeper.com/b/WKIV
   ```
   or
   ```shell
   python main.py your_research_document.txt
   ```

6. The insights and recommendations are printed on the screen, as well as saved to an output file

## Additional Usage Notes

* #### Pushing to Git When Global Config Is Set for Another User
  * `git config --local user.name ""`
  * `git config --local user.email ""`
  * Store token in `.githubinfo` along with potentially other Git information
  * `git push https://github.com/your-username/fireflies-transcript-splitter.git` and enter the password/token when prompted

## License

This project is licensed under the [MIT License](LICENSE).
