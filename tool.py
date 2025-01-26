import os
import itertools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tqdm import tqdm
from dotenv import load_dotenv
import requests

# ASCII Art Header and Quote
def display_header():
    print(r"""
::=+******##************===--:::::::::::::::::::::::------::------====
::-=****#*###**********=======**+===========--:::::-------:----------=
:::==#########*****====-=+*#**#%%**+*+=+===++==---:----=-------------=
::::=+#####%####*#**++**==+****%%%%%%#**#***+++++----==--------------=
::::-=*#%#%%%###*%%#%%%%#**=***#%%%%%%%#***+****#*=-=====------------=
:::::==#%%%%%#*=+*%%%@@%*#%********%###*##****%#***======-----------==
--:::-=+##%%%*=+%%@%%%%#%%%#*+=-::-=*###****#*#%%%%*======-------=--==
==--::-=*####==*%%%%%##*%#*=-:::.::::-=+**#***#%%%%%*=====------=-=-==
*+=::::=+*###+==*###+====-::.........::==**####%%%%%%*+====--=-===-===
*+=-::--+******+---::::::::..........::-=*###*##%%%%%*++=====-==-=====
#*=-----=***+++::::::::::::::::.....:::-=++**##%%%%%##++==============
#**===========::::::::::::::::::::::::::-==+**#%%%%%%**+==============
###*======--:-:::::::::::::::::::::::::::==++**%%%%%##*++=============
###**++===-::---:::::::::::::::::::::::::-==+**##%%%#%**++============
#*#*#**+==--===-:::::::::::::::::::::::::::-=+*******%#**++===========
######*++=+++=---:::::-==========-::::::::::==+**=::-+#***++++++======
%%%%%#*+==++**=======+***#%%%%%*==--::::::::-====::===::=***+**++====+
%%%%%%*=====***####******##%%##*+======:::::-===-=****=:::-*+++=======
%%%%%%*=====**%%%%%%##+==*%%%%#%%%**+==-:::::::::-*****==--=+==-=====+
%%%%%%*======###%%@@%%*::=*%%#***==--::::::::::-::=*++**=-=++=----===+
%%%%%%*======#%%%%%%%%=:::==*%%##*+-:::::::----::--::=#*===#+=-::--===
%%%%%%*+====+#%%#%%%%%-::::--=***+===--:------::::::+%**+=*#*==----===
%%%%%%#++===+#%%**###*-::::--======---=----::::::=+##*#***##*+==----==
%@%@@%%*+++++#%%%****+::::::-==++====-===---:::--=##%%****%%#**+======
@%%@@@%**+++**%%%%***+=------=++**========-:-----=%%%##**==+#%%*+==---
@@%@@%%#***+****##*#**%##%%%%====**+=======-=====#%%###**==-=+%%#*==--
@@%@@%%%***+==++=+*%##*%%%#*=---===++==+========*@%##%#**++====+**+==-
@@%@%@%%***======*%@%**%%%#+==-==****+=+*****+**%%#%%##***+**+========
@%%%%%%%#**+====%@@@@%%##**%%%%#%%%%#**+******%%##%%%###%#***=========
%%%%%%#%#***==*%@@@@@@%*-*@%%*=====+**++***#%%*##%%%%#*%%%%#***+++====
%%##*********%@@@@@@@@+==%##*##*******++**%%####%%%%##*%%%%##******+==
##***+**++*%%@@@@@@@@@%%%%%%%%%%%*******%%%%%%%%%%%#*##%%%%%###******+
#***+++***%@@@@@@@@@@@@@@@%%%%#******#%%%%%%%%%%%%%###%%%%%%%#####****
##******#%@@@@@@@@@@@@@@@@@%%%%##%%%%@@%%%%%%%%%%%%%#%@%%%%%%%######**
%#*****%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%#%@%%%%%%%####****
%%#**#%@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%#%@@%%%%%%%##*##**
%##*%%@@@%%%%%%%%%%@%@@@@@@@@@@@@@@%%%@@@@@%%%%%%%%%%%@@@%%%%%########
####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@%%%%@%%%%%%@@@@%%%%%%%%%%%%%
###*#%%%%%%%%####*********#%@@@@@%@@@@@@@@%%%@@@@%%%%@@@@@%%%%%%%%%%%%
###*******+**+*************%@@@@%@@@%%%@@@%@%@@@@@%%%@@@@%%%%%%%%%%%@@
%###***********************%@@@@@@@@@%%%%@@@@@@@@@%%%@@@@@%%%%%%@@@@@@
%%%#********************###@@@@@%%@@@@%%%%%@@@@@@@@%%@@@@%%%%%%@@@@@@@
%%%%#***#*******######%#%%%@@@@@@%%@@@@@%%%%%@@@@@@%%@@@%%%%@@@@@@@@@@
%%%%#############%%%%%%%%%@%%%@@@@%%@@@@@@%%%%@@@@@%%@@@@%@@@@@@@@@@@@
%%%%%%%%%%%%%%%%%%%%%%%%@@%@@@@@@@@%%@@@@@@%%%%@@@@@%@@@@@@@@@@@@@@@@@
%@%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
%@%%%%%%%%%%%@%%%%%%%%%%@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
%%%@%@%%%%%%%%@%@%%%%%@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@%@%%%%%%%%%%@%@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@%@%@@%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@
@%@%@%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@
%%%%%%%%%%%%%%%#%%@@@@@@@@@@@@@@@@@@@@@%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@
%%%%%%%%%%######%%@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

""")
    print("\n\"The only way to deal with an unfree world is to become so absolutely free that your very existence is an act of rebellion.\"\n")

# Load environment variables
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")

if not SERPAPI_KEY:
    print("Error: SERPAPI_KEY is missing in your .env file.")
    exit(1)

if not CHROME_DRIVER_PATH or not os.path.isfile(CHROME_DRIVER_PATH):
    print("Error: Invalid CHROME_DRIVER_PATH in your .env file.")
    exit(1)

# Save Results to File
def save_results_to_file(username, results):
    with open(f"{username}_results.txt", "w", encoding="utf-8") as txt_file:
        for variation, queries in results.items():
            txt_file.write(f"Username Variation: {variation}\n")
            for query, links in queries.items():
                txt_file.write(f"  Query: {query}\n")
                for link in links:
                    txt_file.write(f"    - {link}\n")
            txt_file.write("\n")
    print(f"Results saved to {username}_results.txt")

def save_variations_to_file(username, variations):
    with open(f"{username}_results.txt", "w", encoding="utf-8") as txt_file:
        for variation in variations:
            txt_file.write(f"{variation}\n")
    print(f"Variations saved to {username}_results.txt")

# Google Dork using SerpAPI
def google_dork_search_selenium(variations, selected_queries, language):
    # Configure Selenium Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--headless")  # Optional: Headless mode for running without UI
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    base_url = f"https://www.google.com/?hl={language}"
    queries = {
        "1": 'site:instagram.com intext:"{username}"',
        "2": 'site:facebook.com intext:"{username}"',
        "3": 'site:linkedin.com intext:"{username}"',
        "4": 'site:pastebin.com "{username}"',
        "5": '"{username}" filetype:pdf',
        "6": '"{username}" filetype:doc',
        "7": '"{username}" "gmail.com"',
        "8": '"{username}" site:*.com',
    }

    all_results = {}

    for username in tqdm(variations, desc="Dorking for all variations with Selenium"):
        user_results = {}
        for query_id in selected_queries:
            query = queries[query_id].format(username=username)
            print(f"\nSearching for: {query}")
            driver.get(base_url)

            try:
                # Enter the query into the search box
                search_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "q"))
                )
                search_box.clear()
                search_box.send_keys(query)
                search_box.send_keys(Keys.RETURN)

                # Wait for results or handle CAPTCHA
                try:
                    links = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tF2Cxc a"))
                    )
                    user_results[query] = [link.get_attribute("href") for link in links][:5]  # Limit to 5 results
                except TimeoutException:
                    if "sorry" in driver.current_url or "captcha" in driver.page_source.lower():
                        print("\nCAPTCHA detected. Please solve it manually.")
                        input("Press Enter after solving the CAPTCHA to continue...")
                    else:
                        print(f"Timeout waiting for results for query: {query}")
            except Exception as e:
                print(f"An error occurred for query '{query}': {e}")

        all_results[username] = user_results

    driver.quit()
    return all_results


# Username Variation Generator
class UsernameVariationGenerator:
    def __init__(self, username, blacklist=None, custom_replacements=None):
        self.username = username
        self.blacklist = blacklist if blacklist else []
        self.replacements = {
            'a': ['a', '4', '@'],
            'e': ['e', '3'],
            'i': ['i', '1', '!'],
            'o': ['o', '0'],
            's': ['s', '5', '$'],
            'g': ['g', '9'],
            't': ['t', '7'],
        }
        self.special_chars = ['.', '_']

        # Add custom replacements
        if custom_replacements:
            for pair in custom_replacements:
                key, values = pair.split("-")
                self.replacements[key] = values.split(",")

    def generate_replacement_variations(self):
        def apply_replacements(char):
            return self.replacements.get(char.lower(), [char])

        replacement_options = [apply_replacements(char) for char in self.username]
        return map(''.join, itertools.product(*replacement_options))

    def generate_special_variations(self):
        variations = set()
        base = self.username.replace('.', '').replace('_', '')

        for i in range(len(base) + 1):
            for char in self.special_chars:
                variations.add(base[:i] + char + base[i:])
        return variations

    def generate_combined_variations(self):
        replacement_variations = list(self.generate_replacement_variations())
        special_variations = list(self.generate_special_variations())
        combined = set(replacement_variations + special_variations)

        combined = sorted(combined, key=lambda x: x != self.username)
        combined = [v for v in combined if not any(b in v for b in self.blacklist)]

        return combined

# Main Tool Logic
def main():
    display_header()
    print("=== Username Analysis Tool ===")
    print("1. Find Dorks for Username")
    print("2. Generate Variations for Username")
    print("3. Generate Variations and Dork for All")
    choice = input("Choose an option (1, 2, 3): ").strip()

    username = input("Enter the username: ").strip()

    if choice in {"1", "3"}:
        method = input("Use SerpAPI (1) or Selenium (2)? ").strip()

        if method not in {"1", "2"}:
            print("Invalid method. Exiting.")
            return

        options = {
            "1": "Instagram",
            "2": "Facebook",
            "3": "LinkedIn",
            "4": "Pastebin",
            "5": "PDFs",
            "6": "Docs",
            "7": "Emails",
            "8": "General Websites",
            "9": "All",
        }

        print("\nSelect platforms to search (e.g., 1,2,3):")
        for key, value in options.items():
            print(f"  {key}. {value}")

        selected = input("Enter your choice: ").split(",")
        if "9" in selected:
            selected = [key for key in options.keys() if key != "9"]

        if choice == "1":
            if method == "1":
                results = google_dork_search_serpapi([username], selected)
            else:
                language = input("Enter language (e.g., en, fr): ").strip()
                results = google_dork_search_selenium([username], selected, language)
            save_results_to_file(username, results)

        elif choice == "3":
            blacklist = input("Blacklist characters (comma-separated, leave blank if none): ").split(",") if input("Blacklist any characters? (y/n): ").strip().lower() == "y" else []
            custom_replacements = input("Custom replacements (format: char-new1,new2, leave blank if none): ").split(",") if input("Add custom replacements? (y/n): ").strip().lower() == "y" else []
            generator = UsernameVariationGenerator(username, blacklist, custom_replacements)
            variations = generator.generate_combined_variations()

            print(f"\nGenerated {len(variations)} variations:")
            for v in variations:
                print(v)

            if method == "1":
                results = google_dork_search_serpapi(variations, selected)
            else:
                language = input("Enter language (e.g., en, fr): ").strip()
                results = google_dork_search_selenium(variations, selected, language)
            save_results_to_file(username, results)

    elif choice == "2":
        blacklist = input("Blacklist characters (comma-separated, leave blank if none): ").split(",") if input("Blacklist any characters? (y/n): ").strip().lower() == "y" else []
        custom_replacements = input("Custom replacements (format: char-new1,new2, leave blank if none): ").split(",") if input("Add custom replacements? (y/n): ").strip().lower() == "y" else []
        generator = UsernameVariationGenerator(username, blacklist, custom_replacements)
        variations = generator.generate_combined_variations()

        print(f"Generated {len(variations)} variations:")
        for v in variations:
            print(v)
        save_variations_to_file(username, variations)

if __name__ == "__main__":
    main()
