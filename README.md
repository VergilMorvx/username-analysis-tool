# Username Analysis Tool

A Python tool designed to generate comprehensive username variations and perform Google dorking using Selenium or SerpAPI. This tool is useful for researchers, ethical hackers, and anyone needing to search variations of usernames efficiently.

## Features
- Generate username variations based on character substitutions and structural changes (e.g., `.` and `_` additions).
- Perform Google dorking on generated variations.
- Save results to a text file for future reference.

## Requirements
- Python 3.7+
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) (compatible with your Chrome version)
- A [SerpAPI](https://serpapi.com/) key (if using SerpAPI for dorking)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/VergilMorvx/username-analysis-tool.git
   cd username-analysis-tool
   ```

2. **Install Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit the `.env` file to include your SerpAPI key and the path to ChromeDriver:
     ```env
     SERPAPI_KEY=your_serpapi_api_key
     CHROME_DRIVER_PATH=/path/to/chromedriver
     ```

   **Note**: Make sure the `CHROME_DRIVER_PATH` matches the location of the downloaded ChromeDriver.

## How to Get a SerpAPI Key
1. Go to [SerpAPI](https://serpapi.com/).
2. Create an account or log in.
3. Navigate to the API key section in your dashboard.
4. Copy your API key and paste it into the `.env` file under `SERPAPI_KEY`.

## How to Get ChromeDriver
1. Visit [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/).
2. Check your Google Chrome version:
   - Open Chrome, go to `Settings > About Chrome`, and note the version number.
3. Download the ChromeDriver version matching your Chrome version.
4. Extract the file and place it in a directory (e.g., `/usr/local/bin` or `C:\chromedriver\`).
5. Add the path to your `.env` file under `CHROME_DRIVER_PATH`.

## Usage

1. **Run the Tool**:
   ```bash
   python tool.py
   ```

2. **Choose an Option**:
   - **Option 1**: Find dorks for a single username.
   - **Option 2**: Generate username variations and save them to a file.
   - **Option 3**: Generate variations and dork for all of them.

3. **Follow Prompts**:
   - Enter the username you want to analyze.
   - Select the desired platforms (e.g., Instagram, Facebook) or choose "All".
   - If generating variations, you can customize character replacements or blacklist certain patterns.

## Example Output

Here’s an example of variations generated for the username `vergilmorvx`:
```
Generated 80 variations:
- vergilmorvx
- vergil_morvx
- v3rgilmorvx
- vergilmorvx.
...
```

Dorking results will be saved in a text file named `<username>_results.txt`.

## Known Limitations
- **SerpAPI Usage**:
  - The script supports SerpAPI for dorking but has not been fully tested as it consumes the free monthly quota quickly. Use with caution.
- **Username Length**:
  - Generating variations may struggle with very long usernames, potentially leading to fewer variations than expected.
- **Dorking Accuracy**:
  - Dorking relies on Google search results, and CAPTCHA challenges may appear when using Selenium.

## Contributing
Feel free to submit issues or pull requests to enhance the tool.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

