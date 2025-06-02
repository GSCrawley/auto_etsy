from apify_client import ApifyClient
from .. import config # Use relative import for config within the src package

# TODO: After user provides APIFY_API_TOKEN in .env, this check can be more robust
# or integrated into a main execution flow.
if not config.APIFY_API_TOKEN:
    print("Error: APIFY_API_TOKEN not found. Please set it in your .env file.")
    # Depending on execution context, might want to raise an exception or exit


def initialize_apify_client():
    """Initializes and returns the ApifyClient with the API token."""
    if not config.APIFY_API_TOKEN:
        raise ValueError("APIFY_API_TOKEN is not configured.")
    return ApifyClient(config.APIFY_API_TOKEN)

def run_instagram_scraper_for_profiles(client: ApifyClient, profile_urls: list[str], max_posts_per_profile: int = 100):
    """
    Runs the apify/instagram-scraper Actor to fetch posts from a list of Instagram profile URLs.

    Args:
        client: An initialized ApifyClient instance.
        profile_urls: A list of Instagram profile URLs to scrape.
        max_posts_per_profile: Maximum number of recent posts to retrieve from each profile.

    Returns:
        The Actor run object containing details about the scraping run, or None if an error occurs.
    """
    if not profile_urls:
        print("No profile URLs provided to scrape.")
        return None

    print(f"Starting Instagram scrape for profiles: {', '.join(profile_urls)}. Max posts per profile: {max_posts_per_profile}")
    
    actor_input = {
        "directUrls": profile_urls,
        "resultsType": "posts", # We want the post details
        "resultsLimit": max_posts_per_profile, # Max posts from each URL provided in directUrls
        # "searchLimit" and "searchType" are not primary for direct URL scraping of profiles.
        # Other useful params could be: "isUserTaggedFeedURL", "isUserReelFeedURL", "onlyPostsNewerThan"
    }

    try:
        # Ensure you have the correct Actor ID if it's not the generic one or if you're using a specific version
        actor = client.actor("apify/instagram-scraper") 
        run = actor.call(run_input=actor_input, wait_for_finish=300) # Wait up to 5 minutes for potentially larger scrapes
        print(f"Scraping run for profiles finished. Run ID: {run.get('id')}, Dataset ID: {run.get('defaultDatasetId')}")
        return run
    except Exception as e:
        print(f"Error running Instagram scraper for profiles {profile_urls}: {e}")
        return None

def get_scraped_data(client: ApifyClient, run_id: str):
    """
    Fetches items from the dataset produced by an Actor run.

    Args:
        client: An initialized ApifyClient instance.
        run_id: The ID of the Actor run.

    Returns:
        A list of items from the dataset, or None if an error occurs.
    """
    if not run_id:
        print("Error: No run_id provided to fetch scraped data.")
        return None
        
    print(f"Fetching dataset for run ID: {run_id}...")
    try:
        dataset_items = client.dataset(run_id).list_items().items
        print(f"Successfully fetched {len(dataset_items)} items from dataset {run_id}.")
        return dataset_items
    except Exception as e:
        print(f"Error fetching dataset items for run ID {run_id}: {e}")
        return None

# Example usage (for testing this module directly)
if __name__ == '__main__':
    import sys
    import os
    import importlib

    # Determine project root (assuming this script is in src/phase1_acquisition)
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

    # Add project root to sys.path to allow importing 'src.config'
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)

    # Load .env file from project root
    dotenv_path = os.path.join(PROJECT_ROOT, '.env')
    if os.path.exists(dotenv_path):
        from dotenv import load_dotenv
        print(f"Loading .env file from: {dotenv_path}")
        load_dotenv(dotenv_path=dotenv_path)
    else:
        print(f"Warning: .env file not found at {dotenv_path}. Environment variables might not be set.")

    # Now import src.config - it should pick up .env variables if loaded
    try:
        from src import config as test_config
        # If .env was loaded after config.py was first implicitly compiled,
        # we might need to reload it to ensure it sees the .env variables.
        importlib.reload(test_config)
    except ImportError as e:
        print(f"Error importing src.config: {e}. Ensure script is run from project root or PYTHONPATH is set.")
        sys.exit(1)

    if not test_config.APIFY_API_TOKEN:
        print("APIFY_API_TOKEN not set. Please ensure it's in your .env file in the project root and loaded correctly.")
    else:
        print("APIFY_API_TOKEN loaded successfully.")
        apify_client = initialize_apify_client() # Will use test_config internally
        
        target_profiles = test_config.INSTAGRAM_TARGET_PROFILES
        if not target_profiles:
            print("No INSTAGRAM_TARGET_PROFILES configured in .env. Please add at least one profile URL to test.")
            # Example: target_profiles = ["https://www.instagram.com/instagram/"] # A default for testing if none provided
            sys.exit(1)

        print(f"Target Instagram profiles for scraping: {target_profiles}")
        print(f"Note: CV Content Descriptions Filter (for later use): {test_config.CV_CONTENT_DESCRIPTIONS_FILTER}")
        
        # Scrape the specified profiles
        # For testing, we can scrape one profile at a time or all together if the actor supports multiple directUrls
        # The apify/instagram-scraper's 'directUrls' parameter accepts an array of URLs.
        
        print(f"\n--- Testing scraper for profiles: {target_profiles} ---")
        # Pass the list of profiles directly
        scraper_run = run_instagram_scraper_for_profiles(apify_client, profile_urls=target_profiles, max_posts_per_profile=10) # Limit to 10 posts per profile for testing
        
        if scraper_run and scraper_run.get('defaultDatasetId'):
            dataset_id = scraper_run['defaultDatasetId']
            print(f"Scraping finished. Dataset ID for profiles {target_profiles}: {dataset_id}")
            items = get_scraped_data(apify_client, run_id=dataset_id)
            if items:
                print(f"Successfully fetched {len(items)} total items. First item details:")
                first_item = items[0]
                print(f"  Item Owner Username: {first_item.get('ownerUsername', 'N/A')}") # Helpful to see which profile it came from if multiple
                print(f"  ID: {first_item.get('id')}")
                print(f"  Type: {first_item.get('type')}")
                print(f"  Short Code: {first_item.get('shortCode')}")
                caption = str(first_item.get('caption', 'N/A'))
                print(f"  Caption: {caption[:100]}{'...' if len(caption) > 100 else ''}")
                print(f"  Post URL: {first_item.get('url')}")
                print(f"  Image URL (displayUrl): {first_item.get('displayUrl')}")
                if 'images' in first_item and first_item['images']:
                    print(f"  Image URL (from images[0]): {first_item['images'][0]}") # Often the same as displayUrl for single image posts
            elif items == []:
                print(f"No items found in the dataset for profiles {target_profiles}. The scraper might not have found any posts or the profiles are private/empty.")
            else:
                print(f"Failed to fetch items for profiles {target_profiles}.")
        else:
            print(f"Scraper run for profiles {target_profiles} did not produce a dataset ID or failed.")
