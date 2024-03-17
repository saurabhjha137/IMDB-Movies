# IMDb Top Movies Scraper

This Python script scrapes data from the IMDb Top Movies chart and saves it in JSON format.

## Requirements

- Python 3
- BeautifulSoup4
- Requests

## Setup

1. Clone this repository to your local machine.
2. Create a virtual environment:
    ```
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```
        source venv/bin/activate
        ```
4. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the `imdb_scraper.py` script:
    ```
    python imdb_scraper.py
    ```
2. The script will scrape data from the IMDb website and save it in a file named `movies.json` in the current directory.

