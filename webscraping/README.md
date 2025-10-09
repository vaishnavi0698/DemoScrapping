Setup and run

1) Create and activate a virtual environment (macOS / zsh):

    /opt/homebrew/bin/python3 -m venv .venv
    source .venv/bin/activate

2) Install dependencies:

    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

3) Run the scraper:

    python scrapingbasics.py

Notes
- If you see 'externally-managed-environment' errors from pip, use the venv method above.
- The script prints the page title and up to 10 hrefs found on the page.
