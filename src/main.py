#!/usr/bin/env python3
"""
Instagram to Etsy Automation - Main Workflow

This script orchestrates the entire workflow for:
1. Acquiring images from Instagram
2. Processing and optimizing images for print
3. Creating products on Printify
4. Publishing to Etsy
5. Managing listings and discovery
"""

import os
import sys
import logging
import argparse
import time
from typing import List, Dict, Any, Optional
from pathlib import Path
import json

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('instagram_to_etsy.log')
    ]
)
logger = logging.getLogger(__name__)

# Add project root to sys.path
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Import modules from project
from src import config
from src.phase1_acquisition.instagram_scraper import InstagramScraper, process_instagram_posts
from src.phase1_acquisition.image_filter import ImageFilter, ImageContentFilter
from src.phase1_acquisition.enhanced_content_filter import EnhancedContentFilter
from src.phase2_processing.image_processor import ImageProcessor
from src.phase3_pod_integration.printify_api import PrintifyAPI
from src.phase5_search_discovery import SearchDiscovery
# Etsy API not needed if only using Printify which automatically posts to Etsy

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Instagram to Etsy Automation')
    
    parser.add_argument('--workflow', '-w', type=str, default='full',
                        choices=['full', 'acquisition', 'processing', 'pod', 'etsy', 'discovery'],
                        help='Workflow to run')
                        
    parser.add_argument('--search-query', '-q', type=str,
                        help='Search query for discovery workflow')
    
    parser.add_argument('--input-dir', '-i', type=str, default='data/raw',
                        help='Input directory for images (used when skipping acquisition)')
    
    parser.add_argument('--output-dir', '-o', type=str, default='data/processed',
                        help='Output directory for processed images')
    
    parser.add_argument('--instagram-user', '-u', type=str,
                        help='Instagram username to scrape (overrides config)')
    
    parser.add_argument('--limit', '-l', type=int, default=10,
                        help='Maximum number of images to process')
    
    parser.add_argument('--skip-upload', '-s', action='store_true',
                        help='Skip uploading to Printify/Etsy')
    
    # Content filtering options
    parser.add_argument('--content-filter', '-cf', action='store_true', 
                        help='Enable content-based filtering with Google Vision API')
                        
    parser.add_argument('--filter-terms', '-ft', type=str,
                        help='Comma-separated list of content terms to filter by (e.g. "sunset,mountains,nature")')
                        
    parser.add_argument('--landscape-only', '-lo', action='store_true', default=False,
                        help='Filter for landscape images only')
    
    # Enhanced filtering options
    parser.add_argument('--enhanced-filter', '-ef', action='store_true', default=True,
                        help='Enable enhanced content filtering with video detection and quality scoring')
                        
    parser.add_argument('--content-categories', '-cc', type=str,
                        help='Comma-separated list of content categories (e.g. "landscape,sunset,water,nature")')
                        
    parser.add_argument('--min-quality-score', '-mqs', type=float,
                        help='Minimum quality score (0.0-1.0) for enhanced filtering')
                        
    parser.add_argument('--min-category-score', '-mcs', type=float,
                        help='Minimum category match score (0.0-1.0) for enhanced filtering')
                        
    parser.add_argument('--min-overall-score', '-mos', type=float,
                        help='Minimum overall score (0.0-1.0) for enhanced filtering')
    
    parser.add_argument('--debug', '-d', action='store_true',
                        help='Enable debug logging')
    
    return parser.parse_args()

def ensure_directories(args):
    """Ensure required directories exist."""
    os.makedirs(args.input_dir, exist_ok=True)
    os.makedirs(args.output_dir, exist_ok=True)
    os.makedirs('data/metadata', exist_ok=True)
    os.makedirs('logs', exist_ok=True)

def run_acquisition_phase(args) -> List[str]:
    """
    Run the Instagram acquisition phase with improved content filtering.
    
    Args:
        args: Command line arguments
        
    Returns:
        List of downloaded image paths
    """
    logger.info("Starting Instagram acquisition phase")
    
    # Determine profile URLs based on username or config
    if args.instagram_user:
        profile_urls = [f"https://www.instagram.com/{args.instagram_user}/"]
        logger.info(f"Using Instagram profile from arguments: {args.instagram_user}")
    else:
        profile_urls = config.INSTAGRAM_TARGET_PROFILES.split(',') if isinstance(config.INSTAGRAM_TARGET_PROFILES, str) else config.INSTAGRAM_TARGET_PROFILES
        logger.info(f"Using Instagram profiles from config: {profile_urls}")
    
    if not profile_urls:
        raise ValueError("No Instagram profiles provided in args or config")
        
    # Set up content filtering if enabled
    content_filter_terms = None
    if args.filter_terms:
        content_filter_terms = [term.strip() for term in args.filter_terms.split(',') if term.strip()]
        logger.info(f"Using custom content filter terms: {content_filter_terms}")
    elif hasattr(config, 'CV_CONTENT_DESCRIPTIONS_FILTER') and config.CV_CONTENT_DESCRIPTIONS_FILTER:
        # Handle both string and list configurations
        if isinstance(config.CV_CONTENT_DESCRIPTIONS_FILTER, str):
            content_filter_terms = [term.strip() for term in config.CV_CONTENT_DESCRIPTIONS_FILTER.split(',') if term.strip()]
        else:
            # Already a list
            content_filter_terms = config.CV_CONTENT_DESCRIPTIONS_FILTER
        logger.info(f"Using content filter terms from config: {content_filter_terms}")
        
    # Create base directory
    os.makedirs(args.input_dir, exist_ok=True)
    
    # Set up enhanced filtering parameters
    content_categories = None
    if args.content_categories:
        content_categories = [cat.strip() for cat in args.content_categories.split(',') if cat.strip()]
        logger.info(f"Using custom content categories: {content_categories}")
    
    # Process Instagram posts with direct function call for more flexibility
    logger.info(f"Starting Instagram scraping with enhanced filtering. Limit: {args.limit} posts")
    processed_posts = process_instagram_posts(
        profile_urls=profile_urls,
        max_posts=args.limit,
        landscape_only=args.landscape_only,
        min_landscape_ratio=1.2,  # Default landscape ratio
        base_dir=args.input_dir,
        use_gcs=hasattr(config, 'USE_GCS') and config.USE_GCS,
        content_filter_terms=content_filter_terms,
        use_content_filter=args.content_filter,
        use_enhanced_filtering=args.enhanced_filter,
        content_categories=content_categories,
        min_quality_score=args.min_quality_score,
        min_category_score=args.min_category_score,
        min_overall_score=args.min_overall_score
    )
    
    if not processed_posts:
        logger.warning("No posts were processed from Instagram.")
        return []
        
    # Extract image paths from processed posts
    image_paths = []
    for post in processed_posts:
        local_path = post.get('local_path')
        if local_path and os.path.exists(local_path):
            image_paths.append(local_path)
            # Log content filtering results if available
            if 'content_filter_results' in post:
                filter_results = post['content_filter_results']
                matched_terms = filter_results.get('matched_filters', [])
                if matched_terms:
                    logger.info(f"Image {os.path.basename(local_path)} matched content terms: {matched_terms}")
    
    logger.info(f"Acquisition complete. {len(image_paths)} images acquired with filtering.")
    
    # Write summary to file
    summary_path = os.path.join(args.input_dir, 'acquisition_summary.json')
    with open(summary_path, 'w') as f:
        summary = {
            'total_posts_processed': len(processed_posts),
            'images_acquired': len(image_paths),
            'landscape_only': args.landscape_only,
            'content_filtering': args.content_filter,
            'content_filter_terms': content_filter_terms,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        json.dump(summary, f, indent=2)
        
    return image_paths

def run_processing_phase(image_paths: List[str], args) -> Dict[str, Any]:
    """
    Run the image processing phase.
    
    Args:
        image_paths: List of image paths to process
        args: Command line arguments
        
    Returns:
        Dictionary with processing results
    """
    logger.info("Starting image processing phase")
    
    # Check if USE_GCS is defined in config, otherwise default to False
    use_gcs = hasattr(config, 'USE_GCS') and config.USE_GCS
    processor = ImageProcessor(use_gcs=use_gcs)
    
    # Process images
    results = processor.batch_process_images(
        image_paths=image_paths,
        size_categories=['small', 'medium', 'large'],
        materials=['fine_art_paper', 'canvas', 'photo_paper'],
        fit_method='contain',
        base_dir='data'
    )
    
    logger.info(f"Processing complete. Processed {results['summary']['successful']} images successfully.")
    return results

def run_discovery_phase(args) -> Dict[str, Any]:
    """
    Run the search discovery phase to find relevant content.
    
    Args:
        args: Command line arguments
        
    Returns:
        Dictionary with discovery results
    """
    logger.info("Starting search discovery phase")
    
    # Get search query from args or use a default
    search_query = args.search_query or "beautiful landscape photography nature"
    
    # Initialize search discovery
    discovery = SearchDiscovery(base_dir='data')
    
    # Run discovery process
    try:
        logger.info(f"Running content discovery with query: {search_query}")
        results = discovery.discover_content(
            search_query=search_query, 
            max_results=args.limit,
            min_quality_score=0.7
        )
        
        if results and results.get('results'):
            logger.info(f"Discovery complete. Found {results.get('returned_results', 0)} relevant images.")
            
            # Process the best images from discovery results
            top_images = []
            for result in results.get('results', []):
                if 'local_path' in result and os.path.exists(result['local_path']):
                    top_images.append(result['local_path'])
            
            logger.info(f"Selected {len(top_images)} top images for processing.")
            return {
                'image_paths': top_images,
                'results': results
            }
        else:
            logger.warning("No relevant content found in discovery phase.")
            return {'image_paths': [], 'results': {}}
            
    except Exception as e:
        logger.error(f"Error in discovery phase: {e}", exc_info=True)
        return {'image_paths': [], 'results': {}, 'error': str(e)}

def run_pod_integration_phase(processing_results: Dict[str, Any], args) -> List[Dict[str, Any]]:
    """
    Run the Print-on-Demand integration phase.
    
    Args:
        processing_results: Results from the processing phase
        args: Command line arguments
        
    Returns:
        List of created product information
    """
    logger.info("Starting Print-on-Demand integration phase")
    
    if args.skip_upload:
        logger.info("Skipping upload to Printify (--skip-upload flag set)")
        return []
    
    printify = PrintifyAPI()
    
    # Verify connection to Printify
    try:
        shops = printify.get_shops()
        if not shops:
            logger.error("No shops found in Printify account")
            return []
        logger.info(f"Connected to Printify. Found {len(shops)} shops.")
    except Exception as e:
        logger.error(f"Failed to connect to Printify: {e}")
        return []
    
    # Find wall art blueprints
    wall_art_blueprints = printify.find_wall_art_blueprints()
    if not wall_art_blueprints:
        logger.error("No wall art blueprints found in Printify catalog")
        return []
    
    # Use the first blueprint and its first provider for simplicity
    # In a real implementation, you would want to select the best option
    blueprint = wall_art_blueprints[0]
    providers = printify.get_print_providers(blueprint['id'])
    if not providers:
        logger.error(f"No print providers found for blueprint {blueprint['id']}")
        return []
    
    provider = providers[0]
    
    # Create products for each successfully processed image
    created_products = []
    
    for image_path, result in processing_results['results'].items():
        if not result.get('success', False):
            continue
        
        # Find the best variant for this image
        variants = result.get('variants', {})
        if not variants:
            logger.warning(f"No variants found for {image_path}. Skipping.")
            continue
        
        # Use medium size on fine art paper as default
        if 'medium' in variants and '16x20' in variants['medium']:
            best_variant = variants['medium']['16x20'].get('fine_art_paper', {})
            variant_path = best_variant.get('local_path')
            
            if not variant_path or not os.path.exists(variant_path):
                logger.warning(f"Best variant file not found for {image_path}. Skipping.")
                continue
            
            # Extract image metadata for the title and description
            metadata = result.get('original_metadata', {})
            location = metadata.get('location', 'Beautiful Location')
            hashtags = metadata.get('hashtags', [])
            
            # Create a title and description
            title = f"Fine Art Print - {location} - Landscape Photography Wall Art"
            description = f"Beautiful landscape photography print of {location}. "
            description += "Perfect for home decor, office spaces, or as a thoughtful gift. "
            description += "Printed on premium fine art paper with archival inks for vibrant colors and detail.\n\n"
            description += "Available in multiple sizes and materials to fit your space."
            
            # Create tags from hashtags
            tags = [tag.replace('#', '') for tag in hashtags[:13]]  # Etsy allows up to 13 tags
            tags.extend(['wall art', 'landscape photography', 'fine art print', 'home decor'])
            tags = list(set(tags))[:13]  # Ensure uniqueness and limit
            
            try:
                # Create and publish the product
                result = printify.create_and_publish_product(
                    image_path=variant_path,
                    title=title,
                    description=description,
                    blueprint_id=blueprint['id'],
                    print_provider_id=provider['id'],
                    tags=tags,
                    price_multiplier=2.5,  # 2.5x the base cost
                    publish=True  # Automatically publish to Etsy
                )
                
                if result.get('success', False):
                    logger.info(f"Successfully created and published product for {image_path}")
                    created_products.append(result)
                else:
                    logger.error(f"Failed to create product for {image_path}: {result.get('error')}")
                    
            except Exception as e:
                logger.error(f"Error creating product for {image_path}: {e}")
    
    logger.info(f"Print-on-Demand integration complete. Created {len(created_products)} products.")
    return created_products

def run_workflow(args):
    """Run the selected workflow."""
    logger.info(f"Starting workflow: {args.workflow}")
    
    # Ensure directories exist
    ensure_directories(args)
    
    # Track workflow metrics
    start_time = time.time()
    metrics = {
        'images_acquired': 0,
        'images_processed': 0,
        'products_created': 0,
        'listings_published': 0,
        'errors': 0
    }
    
    try:
        # Acquisition phase
        if args.workflow in ['full', 'acquisition']:
            image_paths = run_acquisition_phase(args)
            metrics['images_acquired'] = len(image_paths)
        else:
            # If skipping acquisition, use existing images in the input directory
            image_paths = [
                os.path.join(args.input_dir, f) 
                for f in os.listdir(args.input_dir) 
                if f.endswith(('.jpg', '.jpeg', '.png'))
            ]
            logger.info(f"Skipping acquisition. Using {len(image_paths)} existing images.")
        
        # Processing phase
        if args.workflow in ['full', 'processing']:
            processing_results = run_processing_phase(image_paths, args)
            metrics['images_processed'] = processing_results['summary']['successful']
        else:
            logger.info("Skipping processing phase.")
            processing_results = {'results': {path: {'success': True, 'original_path': path} for path in image_paths}}
        
        # Print-on-Demand integration phase
        if args.workflow in ['full', 'pod']:
            created_products = run_pod_integration_phase(processing_results, args)
            metrics['products_created'] = len(created_products)
            metrics['listings_published'] = sum(1 for p in created_products if p.get('published', False))
        else:
            logger.info("Skipping POD integration phase.")
        
        # Etsy management phase
        if args.workflow in ['full', 'etsy']:
            logger.info("Etsy management handled through Printify integration.")
        
        # Search discovery phase
        if args.workflow in ['full', 'discovery']:
            discovery_results = run_discovery_phase(args)
            discovered_images = discovery_results.get('image_paths', [])
            metrics['images_acquired'] += len(discovered_images)
            
            # If running just discovery workflow, process these images
            if args.workflow == 'discovery' and discovered_images:
                # Processing phase for discovered images
                processing_results = run_processing_phase(discovered_images, args)
                metrics['images_processed'] = processing_results['summary']['successful']
                
                # POD integration for discovered images
                if not args.skip_upload:
                    created_products = run_pod_integration_phase(processing_results, args)
                    metrics['products_created'] = len(created_products)
                    metrics['listings_published'] = sum(1 for p in created_products if p.get('published', False))
    
    except Exception as e:
        logger.error(f"Error in workflow: {e}", exc_info=True)
        metrics['errors'] += 1
    
    # Calculate execution time
    execution_time = time.time() - start_time
    metrics['execution_time'] = execution_time
    
    # Log workflow summary
    logger.info("Workflow complete.")
    logger.info(f"Images acquired: {metrics['images_acquired']}")
    logger.info(f"Images processed: {metrics['images_processed']}")
    logger.info(f"Products created: {metrics['products_created']}")
    logger.info(f"Listings published: {metrics['listings_published']}")
    logger.info(f"Errors: {metrics['errors']}")
    logger.info(f"Execution time: {execution_time:.2f} seconds")
    
    # Save metrics to file
    timestamp = int(time.time())
    metrics_path = f"data/metadata/workflow_metrics_{timestamp}.json"
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=2)
    
    return metrics

if __name__ == "__main__":
    args = parse_arguments()
    
    # Set log level
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug logging enabled")
    
    # Run the workflow
    metrics = run_workflow(args)
    
    # Exit with appropriate code
    sys.exit(0 if metrics['errors'] == 0 else 1)
