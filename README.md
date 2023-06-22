```markdown
# ai-insights-generator

## Overview

This script processes longer customer research calls, such as transcripts from [fireflies ai](https://fireflies.ai/), breaking them into manageable chunks and generating insights and recommendations for each chunk.

It also provides an aggregated set of insights and recommendations for the entire research.

The script utilizes the OpenAI API to interact with GPT and generate comprehensive summaries, recommendations, and analysis.

## Features

- Long Research Document Processing: The script efficiently handles long research documents, breaking them into smaller, manageable chunks.
- Chunk-wise Insights and Recommendations: It applies extractive summarization techniques to derive insights and recommendations for each chunk of the research document.
- Aggregated Insights and Recommendations: The script provides an aggregated set of insights and recommendations for the entire research.
- ChatGPT Integration: It utilizes ChatGPT or similar models to generate comprehensive summaries and analysis for each chunk and the entire research document.

Feel free to use this updated version as needed for your README.

## Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/fireflies-transcript-splitter.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Place your transcript document in the same directory as the script. Ensure you have a `.env` file derived from `.env.sample` and place your OpenAI key there.

4. Customize the prompts and configurations in the `config.json` file according to your specific requirements. This file is ignored by Git to ensure privacy of business-sensitive information.

5. Run the script optionally with the research document file as an argument. If you don't have the input file, you can run it as is, and it will prompt you to paste the text:

   ```shell
   python split_transcript.py your_research_document.txt
   ```
   or
   ```shell
   python split_transcript.py
   ```

6. The script will split the research document into smaller parts, generate insights and recommendations for each part, and provide an aggregated set of insights and recommendations for the entire research.

7. The output will be saved as separate text files for each part, and the insights and recommendations will be printed to the console.

8. Use the generated insights, recommendations, and analysis to gain valuable insights, make informed decisions, and enhance your research.

## Additional Usage Notes

* #### Pushing to Git When Global Config Is Set for Another User
  * `git config --local user.name ""`
  * `git config --local user.email ""`
  * Store token in `.githubinfo` along with potentially other Git information
  * `git push https://github.com/your-username/fireflies-transcript-splitter.git` and enter the password/token when prompted

## License

This project is licensed under the [MIT License](LICENSE).
```

Please review the README and make any necessary modifications based on your specific project requirements and preferences.