import requests
import sys
import argparse
import logging # NEW: Import the logging module

# --- NEW: Configure Logging ---
# Sets up basic logging. Messages will go to the console.
# DEBUG: Most detailed info, typically for debugging.
# INFO: General information about script progress.
# WARNING: Something unexpected happened, but script can continue.
# ERROR: A specific error occurred, usually means a function failed.
# CRITICAL: A serious error, usually means the application cannot continue.
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
# You can change level=logging.INFO to logging.DEBUG to see more detailed messages

def display_comic_info(comic_data, is_latest=False):
    """
    Helper function to display comic details in a consistent format.
    """
    comic_num = comic_data.get('num')
    comic_title = comic_data.get('title')
    comic_alt_text = comic_data.get('alt')
    comic_img_url = comic_data.get('img')

    header = "--- Latest XKCD Comic ---" if is_latest else f"--- XKCD Comic #{comic_num} ---"

    print(f"\n{header}")
    print(f"Number: {comic_num}")
    print(f"Title: {comic_title}")
    print(f"Alt Text (Hover-over): {comic_alt_text}")
    print(f"Image URL: {comic_img_url}")
    print(f"Permalink: https://xkcd.com/{comic_num}/")
    print("-------------------------\n")


def get_latest_xkcd():
    """
    Fetches and displays details of the latest XKCD comic.
    """
    url = "https://xkcd.com/info.0.json"

    logging.info("Attempting to fetch the latest XKCD comic.") # Changed from print to logging.info

    try:
        response = requests.get(url)
        response.raise_for_status()

        comic_data = response.json()
        display_comic_info(comic_data, is_latest=True) # Using the new helper function

    except requests.exceptions.RequestException as e:
        logging.error(f"Network or HTTP error fetching latest comic: {e}") # Changed from print to logging.error
        sys.exit(1)

    except ValueError:
        logging.error("JSON decode error: Could not decode response for latest comic from XKCD API. Response might not be valid JSON.") # Changed from print to logging.error
        sys.exit(1)

def get_specific_xkcd(comic_num):
    """
    Fetches and displays details of a specific XKCD comic by its number.
    Handles cases where the comic number might not exist.
    """
    # This validation is still useful, but logging replaces print for errors
    if not isinstance(comic_num, int) or comic_num <= 0:
        logging.error(f"Invalid input: Comic number '{comic_num}' must be a positive integer.")
        sys.exit(1)

    url = f"https://xkcd.com/{comic_num}/info.0.json"

    logging.info(f"Attempting to fetch XKCD comic number {comic_num}.") # Changed from print to logging.info

    try:
        response = requests.get(url)
        response.raise_for_status()

        comic_data = response.json()
        display_comic_info(comic_data, is_latest=False) # Using the new helper function

    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            logging.error(f"Comic not found: XKCD comic number {comic_num} does not exist or you provided an invalid number.")
        else:
            logging.error(f"HTTP error fetching comic {comic_num}: {e}")
        sys.exit(1)

    except requests.exceptions.RequestException as e:
        logging.error(f"Network or HTTP error fetching comic {comic_num}: {e}")
        sys.exit(1)

    except ValueError:
        logging.error(f"JSON decode error: Could not decode response for comic {comic_num} from XKCD API. Response might not be valid JSON.")
        sys.exit(1)

# Main execution block using argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A CLI tool to fetch XKCD comics."
    )

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "--latest",
        action="store_true",
        help="Fetch the latest XKCD comic."
    )

    group.add_argument(
        "--comic",
        type=int,
        help="Fetch a specific XKCD comic by its number (e.g., --comic 614)."
    )

    args = parser.parse_args()

    if args.latest:
        get_latest_xkcd()
    elif args.comic is not None:
        get_specific_xkcd(args.comic)