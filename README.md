# VCard Generator
This Python script generates VCard files (.vcf) for individuals based on user input. The script supports both Serbian and English languages and organizes the generated files into language-specific folders.
Features

    Multilingual Support: Create VCards with properly formatted data for both Serbian and English languages.

    Automated URL and Email Generation: Automatically convert Serbian characters in URLs and email addresses for consistency.

    Dynamic Folder Structure: VCard files are saved in language-specific folders (/en for English and /sr for Serbian) on the user's desktop.

    User-Friendly: The script guides the user through the input process for essential data such as full name, title, and image URL.

Requirements

    Python 3.x
    Requests library (pip install requests)

Usage

    Run the script.
    Enter the requested information, including full name, title in Serbian and English, and image URL.
    The script will generate VCard files and save them to the appropriate language folder on the desktop.

Getting Started
Installation

    Clone the repository:

    bash

git clone https://github.com/your-username/vcard-generator.git

Navigate to the project directory:

bash

cd vcard-generator

Install the required libraries:

bash

    pip install -r requirements.txt

Usage

Run the script:

bash

python generator.py

Follow the prompts to enter the required information.
Contribution

Feel free to contribute by opening issues or pull requests.
License

This project is licensed under the MIT License - see the LICENSE file for details.
