This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

## Additional Info

# Directory Structure
```
memory-bank/
  # Instagram to Etsy Print Shop Automation_ Current State & Next Steps.md
src/
  phase1_acquisition/
    __init__.py
    image_filter.py
    instagram_scraper.py
  phase2_processing/
    __init__.py
    image_processor.py
  phase3_pod_integration/
    __init__.py
    printify_api.py
  phase4_etsy_management/
    __init__.py
  phase5_search_discovery/
    __init__.py
    search_discovery.py
  utils/
    __init__.py
    gcs_storage.py
    image_utils.py
  config.py
  main.py
.gitignore
Instagram-to-Etsy-Print-Shop .md
README.md
repo-structure.md
requirements.txt
run.py
```

# Files

## File: memory-bank/# Instagram to Etsy Print Shop Automation_ Current State & Next Steps.md
````markdown
**\# Instagram to Etsy Print Shop Automation: Current State & Next Steps**

\#\# Current Status

✅ \_\_Project Structure\_\_: Well-organized with phase-based directories ✅ \_\_Configuration\_\_: Environment variables set up in \`.env\` and loaded via \`config.py\` ✅ \_\_Instagram Scraping\_\_: Basic implementation using Apify's Instagram scraper ✅ \_\_API Keys\_\_: Configured for Apify, GCS, Printify, and Etsy

**\#\# Missing Components**

**1\. \_\_Image Processing Pipeline\_\_: Convert scraped images to print-ready formats**  
**2\. \_\_Computer Vision Analysis\_\_: Filter/analyze images based on content**  
**3\. \_\_Printify Integration\_\_: Create products on Printify**  
**4\. \_\_Etsy Listing Management\_\_: Automate listing creation via Printify**  
**5\. \_\_End-to-end Workflow\_\_: Connect all components into a seamless pipeline**

**\#\# Implementation Plan**

Let's approach this systematically, focusing on building each component and connecting them:

**\#\#\# 1\. Complete Phase 1: Instagram Acquisition (Enhancement)**

\- Add filtering for landscape-oriented images  
\- Implement metadata extraction (hashtags, captions)  
\- Add image download functionality to local storage or GCS  
\- Implement basic CV filtering based on content descriptions

**\#\#\# 2\. Implement Phase 2: Image Processing**

\- Set up image enhancement pipeline (resolution, color, sharpness)  
\- Implement print format preparation  
\- Create size variants for different print options  
\- Add quality validation checks

**\#\#\# 3\. Develop Phase 3: Printify Integration**

\- Implement Printify API client  
\- Create product template configurations  
\- Build image upload functionality  
\- Implement product variant generation

**\#\#\# 4\. Complete Phase 4: Etsy Shop Management**

\- Connect Printify with Etsy shop (leveraging Printify's built-in Etsy integration)  
\- Implement automatic publishing to Etsy  
\- Add metadata generation for listings (titles, descriptions, tags)

**\#\#\# 5\. Create Main Orchestration Script**

\- Build a central workflow that connects all phases  
\- Implement error handling and logging  
\- Add configuration options for batch processing

**\#\# Immediate Next Steps**

**1\. Enhance the Instagram scraper to download images**  
**2\. Set up the image processing pipeline**  
**3\. Implement the Printify integration**  
**4\. Connect the components into a basic workflow**

\# Detailed Implementation Plan for Instagram to Etsy Automation

Great\! Let's break down the implementation plan into specific tasks with more technical details for each phase.

\#\# Phase 1 Enhancement: Instagram Acquisition & Image Download

\#\#\# 1.1. Enhance \`instagram\_scraper.py\` to download images

\- Add function to download images from URLs in scraped data  
\- Implement aspect ratio detection to filter landscape images  
\- Add functions to extract and store metadata (hashtags, captions, etc.)  
\- Create local storage structure for downloaded images

\#\#\# 1.2. Implement Google Cloud Storage integration

\- Create \`src/utils/gcs\_storage.py\` for GCS operations  
\- Implement functions to upload images to configured bucket  
\- Add metadata storage alongside images  
\- Include error handling for failed uploads

\#\#\# 1.3. Basic Computer Vision filtering

\- Create \`src/phase1\_acquisition/image\_filter.py\`  
\- Implement functions to analyze images using CV libraries  
\- Add content-based filtering based on CV\_CONTENT\_DESCRIPTIONS\_FILTER  
\- Return boolean indicating if image matches criteria

\#\# Phase 2: Image Processing Pipeline

\#\#\# 2.1. Image Enhancement

\- Create \`src/phase2\_processing/image\_processor.py\`  
\- Implement resolution checking and enhancement  
\- Add color correction and optimization functions  
\- Implement sharpening and noise reduction  
\- Add quality validation checks (min resolution, aspect ratio, etc.)

\#\#\# 2.2. Print Format Preparation

\- Create \`src/phase2\_processing/print\_formatter.py\`  
\- Implement functions to create multiple size variants  
\- Add format conversion (JPEG to TIFF/PNG)  
\- Include color profile management  
\- Create standardized naming convention for processed files

\#\#\# 2.3. Pipeline Orchestration

\- Create \`src/phase2\_processing/processing\_pipeline.py\`  
\- Implement sequential processing workflow  
\- Add batch processing capabilities  
\- Include progress tracking and reporting  
\- Implement error handling with retries

\#\# Phase 3: Printify Integration

\#\#\# 3.1. Printify API Client

\- Create \`src/phase3\_pod\_integration/printify\_client.py\`  
\- Implement authentication and API request handling  
\- Add functions for key Printify operations  
\- Include rate limiting and error handling

\#\#\# 3.2. Product Template Configuration

\- Create \`src/phase3\_pod\_integration/product\_templates.py\`  
\- Define product types (canvas prints, framed prints, etc.)  
\- Configure size variants and pricing  
\- Include material options and specifications  
\- Create blueprint mappings for different product types

\#\#\# 3.3. Product Creation Workflow

\- Create \`src/phase3\_pod\_integration/product\_creator.py\`  
\- Implement image upload to Printify  
\- Add functions to create products with variants  
\- Include metadata generation for listings  
\- Add functions to publish products to Etsy

\#\# Phase 4: Etsy Shop Management via Printify

\#\#\# 4.1. Etsy Metadata Generation

\- Create \`src/phase4\_etsy\_management/metadata\_generator.py\`  
\- Implement functions to create SEO-optimized titles  
\- Add description generation using image metadata  
\- Include tag creation based on image content  
\- Implement category selection logic

\#\#\# 4.2. Etsy Publishing via Printify

\- Create \`src/phase4\_etsy\_management/etsy\_publisher.py\`  
\- Implement functions to trigger Printify-to-Etsy publishing  
\- Add status checking for published listings  
\- Include error handling for failed publications  
\- Implement notification system for successful listings

\#\# Main Orchestration

\#\#\# 5.1. Workflow Orchestration

\- Create \`src/main.py\` as the entry point  
\- Implement end-to-end workflow that connects all phases  
\- Add configuration parsing and validation  
\- Include comprehensive error handling  
\- Implement logging throughout the pipeline

\#\#\# 5.2. Command Line Interface

\- Add command-line arguments for flexible operation  
\- Include options for running individual phases  
\- Add batch processing controls  
\- Implement verbosity levels for logging

\#\# Implementation Timeline

1\. \_\_Week 1: Instagram Acquisition Enhancement\_\_

   \- Day 1-2: Enhance Instagram scraper with image downloads  
   \- Day 3-4: Implement GCS integration  
   \- Day 5: Add basic CV filtering

2\. \_\_Week 2: Image Processing Pipeline\_\_

   \- Day 1-2: Implement image enhancement functions  
   \- Day 3-4: Add print format preparation  
   \- Day 5: Create processing pipeline orchestration

3\. \_\_Week 3: Printify Integration\_\_

   \- Day 1-2: Implement Printify API client  
   \- Day 3-4: Create product templates  
   \- Day 5: Build product creation workflow

4\. \_\_Week 4: Etsy Integration & Main Orchestration\_\_

   \- Day 1-2: Implement metadata generation  
   \- Day 3: Build Etsy publishing via Printify  
   \- Day 4-5: Create main orchestration and CLI
````

## File: src/phase1_acquisition/__init__.py
````python
# Phase 1: Instagram Acquisition package initialization
````

## File: src/phase1_acquisition/image_filter.py
````python
import os
import logging
from typing import List, Dict, Any, Optional, Tuple
from PIL import Image
import numpy as np
import json
import requests
from io import BytesIO

# Use Google Vision API for content detection if available
try:
    from google.cloud import vision
    from google.oauth2 import service_account
    GOOGLE_VISION_AVAILABLE = True
except ImportError:
    GOOGLE_VISION_AVAILABLE = False

from .. import config
from ..utils.image_utils import download_image

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ImageContentFilter:
    """Class for analyzing images and filtering based on content."""
    
    def __init__(self, use_google_vision: bool = True):
        """
        Initialize the image content filter.
        
        Args:
            use_google_vision: Whether to use Google Vision API for content detection.
                               Falls back to simpler methods if API is not available.
        """
        self.use_google_vision = use_google_vision and GOOGLE_VISION_AVAILABLE
        self.vision_client = None
        
        # Initialize Google Vision client if available and configured
        if self.use_google_vision:
            try:
                if config.GOOGLE_APPLICATION_CREDENTIALS:
                    credentials = service_account.Credentials.from_service_account_file(
                        config.GOOGLE_APPLICATION_CREDENTIALS
                    )
                    self.vision_client = vision.ImageAnnotatorClient(credentials=credentials)
                    logger.info("Google Vision API client initialized successfully.")
                else:
                    logger.warning("GOOGLE_APPLICATION_CREDENTIALS not set. Vision API will not be used.")
                    self.use_google_vision = False
            except Exception as e:
                logger.error(f"Error initializing Google Vision API client: {e}")
                self.use_google_vision = False
        
        # Get content filter list from config
        self.content_filters = config.CV_CONTENT_DESCRIPTIONS_FILTER or []
        if not self.content_filters:
            logger.warning("No content filters specified in config. All images will pass content filtering.")
            
        logger.info(f"Image content filter initialized. Using Google Vision: {self.use_google_vision}")
        logger.info(f"Content filters: {self.content_filters}")
        
    def analyze_image(self, image_path: str = None, image_url: str = None, image_data: bytes = None) -> Dict[str, Any]:
        """
        Analyze an image to detect its content.
        
        Args:
            image_path: Path to the local image file.
            image_url: URL of the image to analyze.
            image_data: Binary image data.
            
        Returns:
            A dictionary containing analysis results including:
            - labels: List of content labels detected in the image
            - objects: List of objects detected in the image
            - colors: List of dominant colors in the image
            - text: Text detected in the image
            - safe_search: Safe search annotations if available
        """
        # Ensure we have image data to analyze
        if image_data is None:
            if image_path:
                with open(image_path, 'rb') as f:
                    image_data = f.read()
            elif image_url:
                image_data = download_image(image_url)
                
        if not image_data:
            logger.error("No valid image data provided for analysis")
            return {}
            
        # Analyze with Google Vision if available
        if self.use_google_vision and self.vision_client:
            return self._analyze_with_google_vision(image_data)
        else:
            # Fallback to basic analysis using PIL
            return self._analyze_basic(image_data)
            
    def _analyze_with_google_vision(self, image_data: bytes) -> Dict[str, Any]:
        """
        Analyze image using Google Vision API.
        
        Args:
            image_data: Binary image data.
            
        Returns:
            Dictionary of analysis results.
        """
        try:
            # Create image object
            image = vision.Image(content=image_data)
            
            # Request features
            features = [
                vision.Feature(type_=vision.Feature.Type.LABEL_DETECTION),
                vision.Feature(type_=vision.Feature.Type.OBJECT_LOCALIZATION),
                vision.Feature(type_=vision.Feature.Type.IMAGE_PROPERTIES),
                vision.Feature(type_=vision.Feature.Type.TEXT_DETECTION),
                vision.Feature(type_=vision.Feature.Type.SAFE_SEARCH_DETECTION)
            ]
            
            # Send request
            response = self.vision_client.annotate_image({
                'image': image,
                'features': features
            })
            
            # Process response
            results = {}
            
            # Extract labels
            if response.label_annotations:
                results['labels'] = [
                    {
                        'description': label.description,
                        'score': label.score,
                        'topicality': label.topicality
                    } 
                    for label in response.label_annotations
                ]
                
            # Extract objects
            if response.localized_object_annotations:
                results['objects'] = [
                    {
                        'name': obj.name,
                        'score': obj.score,
                        'bounding_poly': [
                            {'x': vertex.x, 'y': vertex.y} 
                            for vertex in obj.bounding_poly.normalized_vertices
                        ]
                    }
                    for obj in response.localized_object_annotations
                ]
                
            # Extract colors
            if response.image_properties_annotation:
                results['colors'] = [
                    {
                        'color': {
                            'red': color.color.red,
                            'green': color.color.green,
                            'blue': color.color.blue
                        },
                        'score': color.score,
                        'pixel_fraction': color.pixel_fraction
                    }
                    for color in response.image_properties_annotation.dominant_colors.colors
                ]
                
            # Extract text
            if response.text_annotations:
                results['text'] = response.text_annotations[0].description if response.text_annotations else ""
                results['text_annotations'] = [
                    {
                        'description': text.description,
                        'bounding_poly': [
                            {'x': vertex.x, 'y': vertex.y}
                            for vertex in text.bounding_poly.vertices
                        ]
                    }
                    for text in response.text_annotations[1:]  # Skip the first one which is the full text
                ]
                
            # Extract safe search
            if response.safe_search_annotation:
                results['safe_search'] = {
                    'adult': vision.SafeSearchAnnotation.Likelihood.Name(response.safe_search_annotation.adult),
                    'medical': vision.SafeSearchAnnotation.Likelihood.Name(response.safe_search_annotation.medical),
                    'spoof': vision.SafeSearchAnnotation.Likelihood.Name(response.safe_search_annotation.spoof),
                    'violence': vision.SafeSearchAnnotation.Likelihood.Name(response.safe_search_annotation.violence),
                    'racy': vision.SafeSearchAnnotation.Likelihood.Name(response.safe_search_annotation.racy)
                }
                
            return results
            
        except Exception as e:
            logger.error(f"Error analyzing image with Google Vision: {e}")
            return {}
            
    def _analyze_basic(self, image_data: bytes) -> Dict[str, Any]:
        """
        Basic image analysis using PIL.
        
        Args:
            image_data: Binary image data.
            
        Returns:
            Dictionary with basic analysis results.
        """
        try:
            # Open image with PIL
            img = Image.open(BytesIO(image_data))
            
            # Extract basic properties
            results = {
                'format': img.format,
                'mode': img.mode,
                'width': img.width,
                'height': img.height,
                'aspect_ratio': img.width / img.height
            }
            
            # Extract dominant colors (simplified)
            img_small = img.resize((100, 100))
            if img_small.mode != 'RGB':
                img_small = img_small.convert('RGB')
                
            pixels = np.array(img_small)
            pixels = pixels.reshape(-1, 3)
            
            # Simple clustering to find dominant colors
            from sklearn.cluster import KMeans
            kmeans = KMeans(n_clusters=5)
            kmeans.fit(pixels)
            
            # Get the colors
            colors = []
            for center in kmeans.cluster_centers_:
                r, g, b = center.astype(int)
                colors.append({
                    'color': {'red': int(r), 'green': int(g), 'blue': int(b)},
                    'score': 0.0,  # Not available in this simple analysis
                    'pixel_fraction': 0.0  # Not available in this simple analysis
                })
                
            results['colors'] = colors
            
            # We don't have advanced capabilities like object detection without additional libraries
            results['labels'] = []
            results['objects'] = []
            results['text'] = ""
            
            return results
            
        except Exception as e:
            logger.error(f"Error performing basic image analysis: {e}")
            return {}
            
    def meets_content_criteria(self, image_path: str = None, image_url: str = None, 
                              image_data: bytes = None, analysis: Dict[str, Any] = None) -> Tuple[bool, List[str]]:
        """
        Check if an image meets the content criteria based on the content filters.
        
        Args:
            image_path: Path to the local image file.
            image_url: URL of the image.
            image_data: Binary image data.
            analysis: Pre-computed image analysis results.
            
        Returns:
            A tuple containing:
            - Boolean indicating if the image meets criteria
            - List of matched content labels explaining why it matches or doesn't match
        """
        # Get analysis if not provided
        if not analysis:
            analysis = self.analyze_image(image_path, image_url, image_data)
            
        if not analysis:
            logger.warning("No analysis results available. Cannot determine if image meets criteria.")
            return False, ["No analysis results available"]
            
        # If no content filters specified, all images pass
        if not self.content_filters:
            return True, []
            
        # Extract all labels and object names from the analysis
        all_labels = []
        
        # Add labels
        if 'labels' in analysis:
            all_labels.extend([label['description'].lower() for label in analysis['labels']])
            
        # Add object names
        if 'objects' in analysis:
            all_labels.extend([obj['name'].lower() for obj in analysis['objects']])
            
        # Check if any of the labels match our content filters
        matched_filters = []
        for content_filter in self.content_filters:
            content_filter_lower = content_filter.lower()
            for label in all_labels:
                if content_filter_lower in label or label in content_filter_lower:
                    matched_filters.append(f"{label} matches {content_filter}")
                    
        # If we have any matches, the image meets our criteria
        meets_criteria = len(matched_filters) > 0
        
        if meets_criteria:
            logger.info(f"Image meets content criteria. Matched filters: {matched_filters}")
        else:
            logger.info(f"Image does not meet content criteria. No matches found.")
            
        return meets_criteria, matched_filters
        
    def save_analysis_to_file(self, analysis: Dict[str, Any], output_path: str) -> bool:
        """
        Save image analysis results to a JSON file.
        
        Args:
            analysis: Image analysis results.
            output_path: Path to save the JSON file.
            
        Returns:
            True if saved successfully, False otherwise.
        """
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Write to file
            with open(output_path, 'w') as f:
                json.dump(analysis, f, indent=2)
                
            logger.info(f"Analysis saved to {output_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving analysis to {output_path}: {e}")
            return False

# ImageFilter class to match the import in main.py
class ImageFilter:
    """
    Wrapper class for ImageContentFilter that provides the functionality expected by main.py.
    """
    
    def __init__(self):
        """Initialize the image filter with default settings."""
        self.content_filter = ImageContentFilter()
        logger.info("ImageFilter initialized")
    
    def filter_images(self, image_paths: List[str],
                     min_width: int = 1200,
                     min_height: int = 1200,
                     aspect_ratio_range: Tuple[float, float] = (0.5, 2.0),
                     prefer_landscape: bool = True) -> List[str]:
        """
        Filter images based on dimensions, aspect ratio, and optionally content.
        
        Args:
            image_paths: List of paths to images.
            min_width: Minimum image width in pixels.
            min_height: Minimum image height in pixels.
            aspect_ratio_range: Tuple of (min_ratio, max_ratio) for filtering by aspect ratio.
            prefer_landscape: Whether to prioritize landscape-oriented images.
            
        Returns:
            Filtered list of image paths that meet the criteria.
        """
        filtered_paths = []
        
        for path in image_paths:
            try:
                # Open image to check dimensions
                with Image.open(path) as img:
                    width, height = img.size
                    aspect_ratio = width / height
                    
                    # Check dimensions
                    if width < min_width or height < min_height:
                        logger.info(f"Image {path} rejected: dimensions {width}x{height} below minimum {min_width}x{min_height}")
                        continue
                    
                    # Check aspect ratio
                    min_ratio, max_ratio = aspect_ratio_range
                    if aspect_ratio < min_ratio or aspect_ratio > max_ratio:
                        logger.info(f"Image {path} rejected: aspect ratio {aspect_ratio:.2f} outside range {min_ratio}-{max_ratio}")
                        continue
                    
                    # Check content if content filters are configured
                    if self.content_filter.content_filters:
                        meets_criteria, _ = self.content_filter.meets_content_criteria(image_path=path)
                        if not meets_criteria:
                            logger.info(f"Image {path} rejected: does not meet content criteria")
                            continue
                    
                    # Add to filtered list
                    filtered_paths.append(path)
                    logger.info(f"Image {path} accepted: dimensions {width}x{height}, aspect ratio {aspect_ratio:.2f}")
                    
            except Exception as e:
                logger.error(f"Error processing image {path}: {e}")
                continue
        
        # Sort filtered paths - put landscape images first if preferred
        if prefer_landscape and filtered_paths:
            filtered_paths.sort(key=lambda p: Image.open(p).size[0] / Image.open(p).size[1], reverse=True)
            
        logger.info(f"Filtered {len(image_paths)} images to {len(filtered_paths)} that meet criteria")
        return filtered_paths

# Example usage
if __name__ == "__main__":
    import sys
    import os
    
    # Determine project root
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    # Add project root to sys.path
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
        
    # Load .env file
    dotenv_path = os.path.join(PROJECT_ROOT, '.env')
    if os.path.exists(dotenv_path):
        from dotenv import load_dotenv
        print(f"Loading .env file from: {dotenv_path}")
        load_dotenv(dotenv_path=dotenv_path)
        
    # Get some sample images for testing
    data_dir = os.path.join(PROJECT_ROOT, 'data', 'original')
    os.makedirs(data_dir, exist_ok=True)
    
    # Create filter
    content_filter = ImageContentFilter()
    
    # Test with local images if available
    image_files = [f for f in os.listdir(data_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    if image_files:
        print(f"Testing with {len(image_files)} local images")
        for image_file in image_files[:3]:  # Test first 3 images
            image_path = os.path.join(data_dir, image_file)
            print(f"\nAnalyzing {image_file}...")
            
            # Analyze image
            analysis = content_filter.analyze_image(image_path=image_path)
            
            # Check if meets criteria
            meets_criteria, matched_filters = content_filter.meets_content_criteria(analysis=analysis)
            
            # Print results
            print(f"Image meets criteria: {meets_criteria}")
            if matched_filters:
                print(f"Matched filters: {matched_filters}")
                
            # Print some analysis details
            if 'labels' in analysis:
                print(f"Top 5 labels: {[label['description'] for label in analysis['labels'][:5]]}")
            if 'colors' in analysis:
                print(f"Dominant colors: {len(analysis['colors'])}")
            
            # Save analysis
            output_path = os.path.join(PROJECT_ROOT, 'data', 'metadata', f"{os.path.splitext(image_file)[0]}_analysis.json")
            content_filter.save_analysis_to_file(analysis, output_path)
    else:
        # Test with a sample URL if no local images
        test_url = "https://source.unsplash.com/1600x900/?landscape,nature"
        print(f"No local images found. Testing with URL: {test_url}")
        
        # Analyze image
        analysis = content_filter.analyze_image(image_url=test_url)
        
        # Check if meets criteria
        meets_criteria, matched_filters = content_filter.meets_content_criteria(analysis=analysis)
        
        # Print results
        print(f"Image meets criteria: {meets_criteria}")
        if matched_filters:
            print(f"Matched filters: {matched_filters}")
            
        # Print some analysis details
        if 'labels' in analysis:
            print(f"Top 5 labels: {[label['description'] for label in analysis['labels'][:5]]}")
        if 'colors' in analysis:
            print(f"Dominant colors: {len(analysis['colors'])}")
            
        # Save analysis
        output_path = os.path.join(PROJECT_ROOT, 'data', 'metadata', "sample_analysis.json")
        content_filter.save_analysis_to_file(analysis, output_path)
````

## File: src/phase2_processing/__init__.py
````python
# Phase 2: Image Processing package initialization
````

## File: src/phase2_processing/image_processor.py
````python
import os
import logging
import json
import time
from typing import Dict, Any, List, Tuple, Optional, Union
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import io
from pathlib import Path

from .. import config
from ..utils.image_utils import get_image_metadata
from ..utils.gcs_storage import GCSStorage

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Print size presets (width, height in inches)
PRINT_SIZES = {
    'small': {
        '8x10': (8, 10),
        '11x14': (11, 14),
        '12x16': (12, 16)
    },
    'medium': {
        '16x20': (16, 20),
        '18x24': (18, 24),
        '20x24': (20, 24)
    },
    'large': {
        '24x36': (24, 36),
        '30x40': (30, 40),
        '36x48': (36, 48)
    }
}

# Material presets with DPI requirements
MATERIAL_PRESETS = {
    'fine_art_paper': {
        'min_dpi': 300,
        'recommended_dpi': 360,
        'color_profile': 'sRGB',
        'format': 'TIFF'
    },
    'canvas': {
        'min_dpi': 240,
        'recommended_dpi': 300,
        'color_profile': 'sRGB',
        'format': 'TIFF'
    },
    'photo_paper': {
        'min_dpi': 300,
        'recommended_dpi': 300,
        'color_profile': 'sRGB',
        'format': 'JPEG'
    },
    'metal': {
        'min_dpi': 240,
        'recommended_dpi': 300,
        'color_profile': 'sRGB',
        'format': 'TIFF'
    },
    'acrylic': {
        'min_dpi': 300,
        'recommended_dpi': 360,
        'color_profile': 'sRGB',
        'format': 'TIFF'
    }
}

class ImageProcessor:
    """Class for processing and enhancing images for high-quality printing."""
    
    def __init__(self, use_gcs: bool = True):
        """
        Initialize the image processor.
        
        Args:
            use_gcs: Whether to use Google Cloud Storage for storing processed images.
        """
        self.use_gcs = use_gcs
        self.gcs = GCSStorage() if use_gcs else None
        
        if use_gcs and not self.gcs.is_available():
            logger.warning("GCS client not available. Falling back to local storage only.")
            self.use_gcs = False
            
        # Default enhancement parameters
        self.default_params = {
            'brightness': 1.0,    # 1.0 is original
            'contrast': 1.1,      # Slight contrast boost
            'color': 1.05,        # Slight color boost
            'sharpness': 1.2,     # Moderate sharpening
            'saturation': 1.05,   # Slight saturation boost
        }
        
        logger.info(f"Image processor initialized. Using GCS: {self.use_gcs}")
        
    def load_image(self, image_path: str) -> Optional[Image.Image]:
        """
        Load an image from a file path.
        
        Args:
            image_path: Path to the image file.
            
        Returns:
            A PIL Image object or None if loading fails.
        """
        try:
            img = Image.open(image_path)
            return img
        except Exception as e:
            logger.error(f"Error loading image from {image_path}: {e}")
            return None
            
    def enhance_image(self, img: Image.Image, params: Dict[str, float] = None) -> Image.Image:
        """
        Enhance an image using various adjustments.
        
        Args:
            img: PIL Image object to enhance.
            params: Dictionary of enhancement parameters:
                   - brightness: Brightness factor (1.0 is original)
                   - contrast: Contrast factor (1.0 is original)
                   - color: Color factor (1.0 is original)
                   - sharpness: Sharpness factor (1.0 is original)
                   - saturation: Saturation factor (1.0 is original)
                   
        Returns:
            Enhanced PIL Image object.
        """
        # Use default params if none provided
        if params is None:
            params = self.default_params
            
        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')
            
        # Apply brightness adjustment
        if 'brightness' in params:
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(params['brightness'])
            
        # Apply contrast adjustment
        if 'contrast' in params:
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(params['contrast'])
            
        # Apply color adjustment
        if 'color' in params:
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(params['color'])
            
        # Apply sharpness adjustment
        if 'sharpness' in params:
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(params['sharpness'])
            
        # Apply saturation adjustment (requires converting to HSV and back)
        if 'saturation' in params:
            # PIL doesn't have direct saturation adjustment
            # For more advanced saturation control, we would use OpenCV or similar
            pass
            
        return img
        
    def resize_for_print(self, img: Image.Image, 
                        print_size: Tuple[int, int], 
                        dpi: int = 300, 
                        fit_method: str = 'contain') -> Image.Image:
        """
        Resize an image for printing at a specific size and DPI.
        
        Args:
            img: PIL Image object to resize.
            print_size: Tuple of (width, height) in inches.
            dpi: Target dots per inch (resolution).
            fit_method: How to fit the image:
                       - 'contain': Resize to fit within the dimensions, maintaining aspect ratio.
                       - 'cover': Resize to cover the dimensions, maintaining aspect ratio (may crop).
                       - 'stretch': Stretch/squash to exactly match dimensions.
                       
        Returns:
            Resized PIL Image object.
        """
        # Calculate pixel dimensions based on print size and DPI
        target_width_px = int(print_size[0] * dpi)
        target_height_px = int(print_size[1] * dpi)
        
        # Get current image dimensions
        orig_width, orig_height = img.size
        orig_aspect = orig_width / orig_height
        target_aspect = target_width_px / target_height_px
        
        if fit_method == 'contain':
            # Resize to fit within the dimensions, maintaining aspect ratio
            if orig_aspect > target_aspect:
                # Image is wider than target aspect, constrain by width
                new_width = target_width_px
                new_height = int(new_width / orig_aspect)
            else:
                # Image is taller than target aspect, constrain by height
                new_height = target_height_px
                new_width = int(new_height * orig_aspect)
                
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            
            # Create a blank canvas of the target size
            canvas = Image.new('RGB', (target_width_px, target_height_px), color='white')
            
            # Paste the resized image centered on the canvas
            paste_x = (target_width_px - new_width) // 2
            paste_y = (target_height_px - new_height) // 2
            canvas.paste(resized_img, (paste_x, paste_y))
            
            return canvas
            
        elif fit_method == 'cover':
            # Resize to cover the dimensions, maintaining aspect ratio (may crop)
            if orig_aspect > target_aspect:
                # Image is wider than target aspect, constrain by height
                new_height = target_height_px
                new_width = int(new_height * orig_aspect)
            else:
                # Image is taller than target aspect, constrain by width
                new_width = target_width_px
                new_height = int(new_width / orig_aspect)
                
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            
            # Calculate crop coordinates
            left = (new_width - target_width_px) // 2
            top = (new_height - target_height_px) // 2
            right = left + target_width_px
            bottom = top + target_height_px
            
            # Crop to target size
            cropped_img = resized_img.crop((left, top, right, bottom))
            return cropped_img
            
        elif fit_method == 'stretch':
            # Simply stretch/squash to the target dimensions
            return img.resize((target_width_px, target_height_px), Image.LANCZOS)
            
        else:
            logger.warning(f"Unknown fit method: {fit_method}. Using 'contain'.")
            # Default to contain method
            return self.resize_for_print(img, print_size, dpi, 'contain')
            
    def apply_borders(self, img: Image.Image, 
                     border_width: Union[int, Tuple[int, int, int, int]] = 0, 
                     border_color: Tuple[int, int, int] = (255, 255, 255)) -> Image.Image:
        """
        Apply borders to an image.
        
        Args:
            img: PIL Image object.
            border_width: Border width in pixels. Can be a single int for equal borders,
                         or a tuple of (top, right, bottom, left) for different sides.
            border_color: RGB tuple for border color.
            
        Returns:
            PIL Image with borders.
        """
        # Get image dimensions
        width, height = img.size
        
        # Convert single int to tuple if needed
        if isinstance(border_width, int):
            border_width = (border_width, border_width, border_width, border_width)
            
        # Calculate new dimensions
        new_width = width + border_width[1] + border_width[3]
        new_height = height + border_width[0] + border_width[2]
        
        # Create new image with border color
        bordered_img = Image.new('RGB', (new_width, new_height), border_color)
        
        # Paste original image onto the new image with borders
        bordered_img.paste(img, (border_width[3], border_width[0]))
        
        return bordered_img
        
    def convert_to_print_format(self, img: Image.Image, 
                              format_name: str = 'TIFF', 
                              quality: int = 95) -> Tuple[bytes, str]:
        """
        Convert an image to a print-ready format.
        
        Args:
            img: PIL Image object.
            format_name: Target format ('TIFF', 'PNG', 'JPEG', etc.).
            quality: Quality level for formats that support it.
            
        Returns:
            Tuple of (image_data_bytes, file_extension).
        """
        # Ensure format is uppercase
        format_name = format_name.upper()
        
        # Map format to extension
        format_extensions = {
            'TIFF': '.tiff',
            'JPEG': '.jpg',
            'PNG': '.png',
            'BMP': '.bmp'
        }
        
        # Get file extension
        file_ext = format_extensions.get(format_name, f'.{format_name.lower()}')
        
        # Convert to bytes
        img_byte_arr = io.BytesIO()
        
        # Handle format-specific save options
        if format_name == 'JPEG':
            img.save(img_byte_arr, format=format_name, quality=quality)
        elif format_name == 'TIFF':
            img.save(img_byte_arr, format=format_name, compression='tiff_lzw')
        elif format_name == 'PNG':
            img.save(img_byte_arr, format=format_name, compress_level=int(quality / 10))
        else:
            img.save(img_byte_arr, format=format_name)
            
        img_byte_arr.seek(0)
        return img_byte_arr.getvalue(), file_ext
        
    def generate_print_variants(self, img: Image.Image, 
                               metadata: Dict[str, Any],
                               size_categories: List[str] = None,
                               materials: List[str] = None,
                               fit_method: str = 'contain',
                               base_dir: str = 'data',
                               base_filename: str = None) -> Dict[str, Dict[str, Dict[str, Any]]]:
        """
        Generate print variants for different sizes and materials.
        
        Args:
            img: PIL Image object.
            metadata: Original image metadata.
            size_categories: List of size categories to include ('small', 'medium', 'large').
            materials: List of materials to generate variants for.
            fit_method: How to fit the image ('contain', 'cover', 'stretch').
            base_dir: Base directory for output files.
            base_filename: Base filename for output files.
            
        Returns:
            Dictionary of generated variants with paths and metadata.
        """
        # Default values if not provided
        if size_categories is None:
            size_categories = ['small', 'medium', 'large']
            
        if materials is None:
            materials = list(MATERIAL_PRESETS.keys())
            
        if base_filename is None:
            base_filename = f"processed_image_{hash(img)}"
            
        # Create processed image directory if it doesn't exist
        processed_dir = os.path.join(base_dir, 'processed')
        os.makedirs(processed_dir, exist_ok=True)
        
        # Dictionary to store results
        results = {}
        
        # Track the best variant for each size
        best_variants = {}
        
        # Process each size category
        for size_cat in size_categories:
            results[size_cat] = {}
            
            if size_cat not in PRINT_SIZES:
                logger.warning(f"Unknown size category: {size_cat}. Skipping.")
                continue
                
            # Process each size in the category
            for size_name, size_inches in PRINT_SIZES[size_cat].items():
                results[size_cat][size_name] = {}
                
                # Process each material
                for material in materials:
                    if material not in MATERIAL_PRESETS:
                        logger.warning(f"Unknown material: {material}. Skipping.")
                        continue
                        
                    # Get material settings
                    mat_settings = MATERIAL_PRESETS[material]
                    dpi = mat_settings['recommended_dpi']
                    format_name = mat_settings['format']
                    
                    # Enhanced image (apply basic enhancements)
                    enhanced_img = self.enhance_image(img)
                    
                    # Resize for print
                    resized_img = self.resize_for_print(enhanced_img, size_inches, dpi, fit_method)
                    
                    # Convert to print format
                    img_data, file_ext = self.convert_to_print_format(resized_img, format_name)
                    
                    # Generate output filename
                    output_filename = f"{base_filename}_{size_name}_{material}{file_ext}"
                    output_path = os.path.join(processed_dir, output_filename)
                    
                    # Save locally
                    with open(output_path, 'wb') as f:
                        f.write(img_data)
                        
                    # Upload to GCS if enabled
                    gcs_path = None
                    if self.use_gcs:
                        gcs_path = f"processed/{output_filename}"
                        self.gcs.upload_file(output_path, gcs_path)
                        
                    # Calculate print resolution
                    actual_width, actual_height = resized_img.size
                    actual_width_inches, actual_height_inches = size_inches
                    actual_dpi_w = actual_width / actual_width_inches
                    actual_dpi_h = actual_height / actual_height_inches
                    
                    # Store variant details
                    variant_details = {
                        'local_path': output_path,
                        'gcs_path': gcs_path,
                        'size_inches': size_inches,
                        'size_pixels': (actual_width, actual_height),
                        'dpi': (actual_dpi_w, actual_dpi_h),
                        'material': material,
                        'format': format_name,
                        'fit_method': fit_method
                    }
                    
                    results[size_cat][size_name][material] = variant_details
                    
                    # Track best variant for this size (prefer higher DPI and better materials)
                    size_key = f"{size_cat}_{size_name}"
                    if size_key not in best_variants:
                        best_variants[size_key] = variant_details
                    else:
                        # Simple heuristic: prefer higher DPI
                        current_dpi = min(best_variants[size_key]['dpi'])
                        new_dpi = min(variant_details['dpi'])
                        if new_dpi > current_dpi:
                            best_variants[size_key] = variant_details
                            
        # Save metadata with variants
        metadata_path = os.path.join(base_dir, 'metadata', f"{base_filename}_print_variants.json")
        os.makedirs(os.path.dirname(metadata_path), exist_ok=True)
        
        metadata_dict = {
            'original_metadata': metadata,
            'variants': results,
            'best_variants': best_variants
        }
        
        with open(metadata_path, 'w') as f:
            json.dump(metadata_dict, f, indent=2)
            
        # Upload metadata to GCS
        if self.use_gcs:
            gcs_metadata_path = f"metadata/{base_filename}_print_variants.json"
            self.gcs.upload_file(metadata_path, gcs_metadata_path)
            
        return results
        
    def process_image(self, image_path: str, 
                     size_categories: List[str] = None,
                     materials: List[str] = None,
                     fit_method: str = 'contain',
                     enhancement_params: Dict[str, float] = None,
                     base_dir: str = 'data') -> Dict[str, Any]:
        """
        Process an image through the full pipeline.
        
        Args:
            image_path: Path to the input image.
            size_categories: List of size categories to include.
            materials: List of materials to generate variants for.
            fit_method: How to fit the image.
            enhancement_params: Custom enhancement parameters.
            base_dir: Base directory for output files.
            
        Returns:
            Dictionary with processing results and variant information.
        """
        # Load image
        logger.info(f"Processing image: {image_path}")
        img = self.load_image(image_path)
        if img is None:
            logger.error(f"Failed to load image: {image_path}")
            return {'success': False, 'error': 'Failed to load image'}
            
        # Get original metadata
        original_metadata = get_image_metadata(img)
        
        # Get base filename
        base_filename = os.path.splitext(os.path.basename(image_path))[0]
        
        # Apply enhancements
        enhanced_img = self.enhance_image(img, enhancement_params)
        
        # Generate print variants
        variants = self.generate_print_variants(
            enhanced_img,
            original_metadata,
            size_categories,
            materials,
            fit_method,
            base_dir,
            base_filename
        )
        
        # Build result
        result = {
            'success': True,
            'original_path': image_path,
            'original_metadata': original_metadata,
            'variants': variants
        }
        
        logger.info(f"Successfully processed image: {image_path}")
        
        return result
        
    def batch_process_images(self, image_paths: List[str], 
                           size_categories: List[str] = None,
                           materials: List[str] = None,
                           fit_method: str = 'contain',
                           enhancement_params: Dict[str, float] = None,
                           base_dir: str = 'data') -> Dict[str, Any]:
        """
        Process multiple images in batch.
        
        Args:
            image_paths: List of paths to input images.
            size_categories: List of size categories to include.
            materials: List of materials to generate variants for.
            fit_method: How to fit the image.
            enhancement_params: Custom enhancement parameters.
            base_dir: Base directory for output files.
            
        Returns:
            Dictionary with processing results for each image.
        """
        results = {}
        successful = 0
        failed = 0
        
        for path in image_paths:
            try:
                result = self.process_image(
                    path,
                    size_categories,
                    materials,
                    fit_method,
                    enhancement_params,
                    base_dir
                )
                
                results[path] = result
                if result.get('success', False):
                    successful += 1
                else:
                    failed += 1
                    
                logger.info(f"Processed {successful + failed}/{len(image_paths)} images")
            except Exception as e:
                logger.error(f"Error processing image {path}: {e}")
                results[path] = {
                    'success': False,
                    'error': str(e)
                }
                failed += 1
                
        # Create summary
        summary = {
            'total': len(image_paths),
            'successful': successful,
            'failed': failed,
            'success_rate': successful / len(image_paths) if len(image_paths) > 0 else 0
        }
        
        # Save batch processing summary
        timestamp = int(time.time())
        summary_path = os.path.join(base_dir, 'metadata', f"batch_processing_summary_{timestamp}.json")
        os.makedirs(os.path.dirname(summary_path), exist_ok=True)
        
        with open(summary_path, 'w') as f:
            json.dump({
                'summary': summary,
                'results': results
            }, f, indent=2)
            
        logger.info(f"Batch processing complete. Success rate: {summary['success_rate']:.2%}")
        
        return {
            'summary': summary,
            'results': results,
            'summary_path': summary_path
        }
````

## File: src/phase3_pod_integration/__init__.py
````python
# Phase 3: Print-on-Demand Integration package initialization
````

## File: src/phase3_pod_integration/printify_api.py
````python
import os
import json
import time
import logging
import requests
from typing import Dict, List, Any, Optional, Union, Tuple
from urllib.parse import urljoin

from .. import config

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Printify API Base URL
PRINTIFY_API_BASE = "https://api.printify.com/v1/"

class PrintifyAPI:
    """
    Class for interacting with the Printify API to create and publish products
    to print-on-demand services and Etsy.
    """
    
    def __init__(self, api_token: str = None, shop_id: str = None):
        """
        Initialize the Printify API client.
        
        Args:
            api_token: Printify API token. If None, loaded from config/environment.
            shop_id: Printify shop ID. If None, loaded from config/environment.
        """
        self.api_token = api_token or config.PRINTIFY_API_TOKEN
        self.shop_id = shop_id or config.PRINTIFY_SHOP_ID
        
        if not self.api_token:
            logger.error("Printify API token not provided. Cannot connect to Printify API.")
        else:
            logger.info("Printify API client initialized.")
            
        if not self.shop_id:
            logger.warning("Printify shop ID not provided. You'll need to specify shop_id for operations.")
            
        # Setup session for API requests
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
        # Cache for blueprints and print providers
        self._blueprints_cache = None
        self._print_providers_cache = {}
        
    def _make_request(self, method: str, endpoint: str, 
                     params: Dict[str, Any] = None, 
                     data: Dict[str, Any] = None, 
                     files: Dict[str, Any] = None,
                     retry_count: int = 3, 
                     retry_delay: float = 1.0) -> Dict[str, Any]:
        """
        Make a request to the Printify API with retry logic.
        
        Args:
            method: HTTP method ('GET', 'POST', 'PUT', etc.)
            endpoint: API endpoint (without the base URL)
            params: URL parameters
            data: Request body data
            files: Files to upload
            retry_count: Number of retries on failure
            retry_delay: Delay between retries (exponential backoff applied)
            
        Returns:
            Response data as dictionary
        """
        url = urljoin(PRINTIFY_API_BASE, endpoint)
        current_retry = 0
        
        while current_retry <= retry_count:
            try:
                if files:
                    # For file uploads, don't send JSON
                    headers = self.session.headers.copy()
                    headers.pop('Content-Type', None)
                    response = self.session.request(
                        method=method,
                        url=url,
                        params=params,
                        data=data,
                        files=files,
                        headers=headers,
                        timeout=30
                    )
                else:
                    # Standard JSON request
                    json_data = json.dumps(data) if data else None
                    response = self.session.request(
                        method=method,
                        url=url,
                        params=params,
                        data=json_data,
                        timeout=30
                    )
                
                # Handle rate limits
                if response.status_code == 429:
                    retry_after = int(response.headers.get('Retry-After', 60))
                    logger.warning(f"Rate limited by Printify API. Waiting {retry_after} seconds.")
                    time.sleep(retry_after)
                    current_retry += 1
                    continue
                    
                # Check for success
                response.raise_for_status()
                
                # Return JSON response if available
                if response.content:
                    return response.json()
                return {}
                
            except requests.exceptions.RequestException as e:
                # Handle retryable errors
                if current_retry < retry_count:
                    # Exponential backoff
                    sleep_time = retry_delay * (2 ** current_retry)
                    logger.warning(f"Request to {url} failed: {e}. Retrying in {sleep_time:.2f} seconds.")
                    time.sleep(sleep_time)
                    current_retry += 1
                else:
                    logger.error(f"Request to {url} failed after {retry_count} retries: {e}")
                    raise
                    
        # This should not be reached, but just in case
        raise RuntimeError(f"Failed to make request to {url} after {retry_count} retries")
        
    def get_shops(self) -> List[Dict[str, Any]]:
        """
        Get list of shops connected to the Printify account.
        
        Returns:
            List of shop dictionaries
        """
        logger.info("Getting list of shops from Printify")
        response = self._make_request('GET', 'shops.json')
        shops = response.get('data', [])
        logger.info(f"Found {len(shops)} shops")
        return shops
        
    def get_shop_info(self, shop_id: str = None) -> Dict[str, Any]:
        """
        Get information about a specific shop.
        
        Args:
            shop_id: Shop ID. If None, uses the default shop_id.
            
        Returns:
            Shop information dictionary
        """
        shop_id = shop_id or self.shop_id
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        logger.info(f"Getting information for shop {shop_id}")
        return self._make_request('GET', f'shops/{shop_id}.json')
        
    def get_blueprints(self, force_refresh: bool = False) -> List[Dict[str, Any]]:
        """
        Get list of available product blueprints (product types).
        
        Args:
            force_refresh: Whether to force a refresh of cached blueprints
            
        Returns:
            List of blueprint dictionaries
        """
        if self._blueprints_cache is None or force_refresh:
            logger.info("Getting product blueprints from Printify")
            response = self._make_request('GET', 'catalog/blueprints.json')
            self._blueprints_cache = response.get('data', [])
            logger.info(f"Found {len(self._blueprints_cache)} product blueprints")
            
        return self._blueprints_cache
        
    def get_blueprint_details(self, blueprint_id: int) -> Dict[str, Any]:
        """
        Get detailed information about a specific product blueprint.
        
        Args:
            blueprint_id: Blueprint ID
            
        Returns:
            Blueprint details dictionary
        """
        logger.info(f"Getting details for blueprint {blueprint_id}")
        return self._make_request('GET', f'catalog/blueprints/{blueprint_id}.json')
        
    def get_print_providers(self, blueprint_id: int, force_refresh: bool = False) -> List[Dict[str, Any]]:
        """
        Get list of print providers for a specific blueprint.
        
        Args:
            blueprint_id: Blueprint ID
            force_refresh: Whether to force a refresh of cached print providers
            
        Returns:
            List of print provider dictionaries
        """
        cache_key = str(blueprint_id)
        
        if cache_key not in self._print_providers_cache or force_refresh:
            logger.info(f"Getting print providers for blueprint {blueprint_id}")
            response = self._make_request('GET', f'catalog/blueprints/{blueprint_id}/print_providers.json')
            self._print_providers_cache[cache_key] = response.get('data', [])
            logger.info(f"Found {len(self._print_providers_cache[cache_key])} print providers for blueprint {blueprint_id}")
            
        return self._print_providers_cache[cache_key]
        
    def get_variants(self, blueprint_id: int, print_provider_id: int) -> List[Dict[str, Any]]:
        """
        Get list of variants for a specific blueprint and print provider.
        
        Args:
            blueprint_id: Blueprint ID
            print_provider_id: Print provider ID
            
        Returns:
            List of variant dictionaries
        """
        logger.info(f"Getting variants for blueprint {blueprint_id} and provider {print_provider_id}")
        endpoint = f'catalog/blueprints/{blueprint_id}/print_providers/{print_provider_id}/variants.json'
        response = self._make_request('GET', endpoint)
        variants = response.get('data', [])
        logger.info(f"Found {len(variants)} variants")
        return variants
        
    def get_shipping_info(self, blueprint_id: int, print_provider_id: int) -> Dict[str, Any]:
        """
        Get shipping information for a specific blueprint and print provider.
        
        Args:
            blueprint_id: Blueprint ID
            print_provider_id: Print provider ID
            
        Returns:
            Shipping information dictionary
        """
        logger.info(f"Getting shipping info for blueprint {blueprint_id} and provider {print_provider_id}")
        endpoint = f'catalog/blueprints/{blueprint_id}/print_providers/{print_provider_id}/shipping.json'
        return self._make_request('GET', endpoint)
        
    def upload_image(self, image_path: str, file_name: str = None) -> Dict[str, Any]:
        """
        Upload an image to Printify.
        
        Args:
            image_path: Path to the image file
            file_name: Name to use for the uploaded file. If None, uses the basename of image_path.
            
        Returns:
            Response containing the image information including ID
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
            
        if file_name is None:
            file_name = os.path.basename(image_path)
            
        logger.info(f"Uploading image {image_path} to Printify")
        
        with open(image_path, 'rb') as f:
            files = {
                'file': (file_name, f, 'image/jpeg')
            }
            
            shop_id = self.shop_id
            if not shop_id:
                raise ValueError("Shop ID is required for uploading images")
                
            endpoint = f'shops/{shop_id}/images.json'
            response = self._make_request('POST', endpoint, files=files)
            
            if 'id' in response:
                logger.info(f"Image uploaded successfully. Image ID: {response['id']}")
            else:
                logger.error(f"Failed to upload image. Response: {response}")
                
            return response
            
    def create_product(self, shop_id: str = None, product_data: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Create a new product on Printify.
        
        Args:
            shop_id: Shop ID. If None, uses the default shop_id.
            product_data: Product data dictionary including:
                - title: Product title
                - description: Product description
                - blueprint_id: Blueprint ID
                - print_provider_id: Print provider ID
                - variants: List of variant dictionaries
                - print_areas: Dictionary of print areas with image IDs
                
        Returns:
            Response containing the created product information
        """
        shop_id = shop_id or self.shop_id
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        if not product_data:
            raise ValueError("Product data is required")
            
        required_fields = ['title', 'description', 'blueprint_id', 'print_provider_id', 'variants', 'print_areas']
        for field in required_fields:
            if field not in product_data:
                raise ValueError(f"Missing required field in product data: {field}")
                
        logger.info(f"Creating product '{product_data['title']}' in shop {shop_id}")
        endpoint = f'shops/{shop_id}/products.json'
        response = self._make_request('POST', endpoint, data=product_data)
        
        if 'id' in response:
            logger.info(f"Product created successfully. Product ID: {response['id']}")
        else:
            logger.error(f"Failed to create product. Response: {response}")
            
        return response
        
    def update_product(self, shop_id: str, product_id: str, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an existing product on Printify.
        
        Args:
            shop_id: Shop ID
            product_id: Product ID
            product_data: Updated product data dictionary
            
        Returns:
            Response containing the updated product information
        """
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        if not product_id:
            raise ValueError("Product ID is required")
            
        logger.info(f"Updating product {product_id} in shop {shop_id}")
        endpoint = f'shops/{shop_id}/products/{product_id}.json'
        response = self._make_request('PUT', endpoint, data=product_data)
        
        if 'id' in response:
            logger.info(f"Product updated successfully. Product ID: {response['id']}")
        else:
            logger.error(f"Failed to update product. Response: {response}")
            
        return response
        
    def publish_product(self, shop_id: str, product_id: str, publish: bool = True) -> Dict[str, Any]:
        """
        Publish or unpublish a product to external marketplaces (e.g., Etsy).
        
        Args:
            shop_id: Shop ID
            product_id: Product ID
            publish: Whether to publish (True) or unpublish (False) the product
            
        Returns:
            Response containing the publish operation result
        """
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        if not product_id:
            raise ValueError("Product ID is required")
            
        action = "Publishing" if publish else "Unpublishing"
        logger.info(f"{action} product {product_id} in shop {shop_id}")
        
        endpoint = f'shops/{shop_id}/products/{product_id}/publish.json'
        data = {"publish": publish}
        response = self._make_request('POST', endpoint, data=data)
        
        status = "published" if publish else "unpublished"
        if response.get('status') == status:
            logger.info(f"Product {status} successfully")
        else:
            logger.error(f"Failed to {action.lower()} product. Response: {response}")
            
        return response
        
    def get_product(self, shop_id: str, product_id: str) -> Dict[str, Any]:
        """
        Get information about a specific product.
        
        Args:
            shop_id: Shop ID
            product_id: Product ID
            
        Returns:
            Product information dictionary
        """
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        if not product_id:
            raise ValueError("Product ID is required")
            
        logger.info(f"Getting information for product {product_id} in shop {shop_id}")
        endpoint = f'shops/{shop_id}/products/{product_id}.json'
        return self._make_request('GET', endpoint)
        
    def get_products(self, shop_id: str = None, page: int = 1, limit: int = 10) -> Dict[str, Any]:
        """
        Get list of products in a shop.
        
        Args:
            shop_id: Shop ID. If None, uses the default shop_id.
            page: Page number for pagination
            limit: Number of products per page
            
        Returns:
            Response containing the list of products
        """
        shop_id = shop_id or self.shop_id
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        logger.info(f"Getting products for shop {shop_id} (page {page}, limit {limit})")
        endpoint = f'shops/{shop_id}/products.json'
        params = {
            'page': page,
            'limit': limit
        }
        return self._make_request('GET', endpoint, params=params)
        
    def delete_product(self, shop_id: str, product_id: str) -> Dict[str, Any]:
        """
        Delete a product from Printify.
        
        Args:
            shop_id: Shop ID
            product_id: Product ID
            
        Returns:
            Response indicating success or failure
        """
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        if not product_id:
            raise ValueError("Product ID is required")
            
        logger.info(f"Deleting product {product_id} from shop {shop_id}")
        endpoint = f'shops/{shop_id}/products/{product_id}.json'
        return self._make_request('DELETE', endpoint)
        
    def create_order(self, shop_id: str, order_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new order on Printify.
        
        Args:
            shop_id: Shop ID
            order_data: Order data dictionary
            
        Returns:
            Response containing the created order information
        """
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        if not order_data:
            raise ValueError("Order data is required")
            
        logger.info(f"Creating order in shop {shop_id}")
        endpoint = f'shops/{shop_id}/orders.json'
        return self._make_request('POST', endpoint, data=order_data)
        
    def get_order(self, shop_id: str, order_id: str) -> Dict[str, Any]:
        """
        Get information about a specific order.
        
        Args:
            shop_id: Shop ID
            order_id: Order ID
            
        Returns:
            Order information dictionary
        """
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        if not order_id:
            raise ValueError("Order ID is required")
            
        logger.info(f"Getting information for order {order_id} in shop {shop_id}")
        endpoint = f'shops/{shop_id}/orders/{order_id}.json'
        return self._make_request('GET', endpoint)
        
    def get_orders(self, shop_id: str = None, page: int = 1, limit: int = 10) -> Dict[str, Any]:
        """
        Get list of orders in a shop.
        
        Args:
            shop_id: Shop ID. If None, uses the default shop_id.
            page: Page number for pagination
            limit: Number of orders per page
            
        Returns:
            Response containing the list of orders
        """
        shop_id = shop_id or self.shop_id
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        logger.info(f"Getting orders for shop {shop_id} (page {page}, limit {limit})")
        endpoint = f'shops/{shop_id}/orders.json'
        params = {
            'page': page,
            'limit': limit
        }
        return self._make_request('GET', endpoint, params=params)
        
    def cancel_order(self, shop_id: str, order_id: str) -> Dict[str, Any]:
        """
        Cancel an order on Printify.
        
        Args:
            shop_id: Shop ID
            order_id: Order ID
            
        Returns:
            Response indicating success or failure
        """
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        if not order_id:
            raise ValueError("Order ID is required")
            
        logger.info(f"Cancelling order {order_id} in shop {shop_id}")
        endpoint = f'shops/{shop_id}/orders/{order_id}/cancel.json'
        return self._make_request('POST', endpoint)
        
    def calculate_shipping(self, shop_id: str, shipping_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate shipping costs for an order.
        
        Args:
            shop_id: Shop ID
            shipping_data: Shipping calculation data including address and items
            
        Returns:
            Response containing shipping cost information
        """
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        if not shipping_data:
            raise ValueError("Shipping data is required")
            
        logger.info(f"Calculating shipping costs for shop {shop_id}")
        endpoint = f'shops/{shop_id}/orders/shipping.json'
        return self._make_request('POST', endpoint, data=shipping_data)

    def find_wall_art_blueprints(self) -> List[Dict[str, Any]]:
        """
        Find all blueprints related to wall art (posters, canvas, framed prints, etc.).
        
        Returns:
            List of wall art blueprint dictionaries
        """
        all_blueprints = self.get_blueprints()
        wall_art_blueprints = []
        
        # Keywords that indicate wall art products
        wall_art_keywords = [
            'poster', 'canvas', 'print', 'frame', 'wall', 'art', 'photo', 'picture',
            'artwork', 'painting', 'metal print', 'acrylic print'
        ]
        
        for blueprint in all_blueprints:
            title = blueprint.get('title', '').lower()
            if any(keyword in title for keyword in wall_art_keywords):
                wall_art_blueprints.append(blueprint)
                
        logger.info(f"Found {len(wall_art_blueprints)} wall art blueprints out of {len(all_blueprints)} total")
        return wall_art_blueprints
        
    def prepare_product_from_image(self, 
                                 image_path: str, 
                                 title: str, 
                                 description: str,
                                 blueprint_id: int,
                                 print_provider_id: int,
                                 variant_ids: List[int] = None,
                                 tags: List[str] = None,
                                 price_multiplier: float = 2.0) -> Dict[str, Any]:
        """
        Prepare product data for creating a product from an image.
        
        Args:
            image_path: Path to the image file
            title: Product title
            description: Product description
            blueprint_id: Blueprint ID
            print_provider_id: Print provider ID
            variant_ids: List of variant IDs to include. If None, all available variants are used.
            tags: List of tags for the product
            price_multiplier: Multiplier for setting the retail price based on the print cost
            
        Returns:
            Product data dictionary ready for create_product()
        """
        # Upload the image
        image_response = self.upload_image(image_path)
        if 'id' not in image_response:
            raise ValueError(f"Failed to upload image: {image_response}")
            
        image_id = image_response['id']
        
        # Get available variants
        all_variants = self.get_variants(blueprint_id, print_provider_id)
        if not all_variants:
            raise ValueError(f"No variants available for blueprint {blueprint_id} and provider {print_provider_id}")
            
        # Filter variants if specific IDs provided
        variants_to_use = all_variants
        if variant_ids:
            variants_to_use = [v for v in all_variants if v['id'] in variant_ids]
            if not variants_to_use:
                raise ValueError(f"None of the specified variant IDs were found")
                
        # Prepare variant data
        variants = []
        for variant in variants_to_use:
            # Calculate price (cost * multiplier)
            cost = float(variant['cost']) / 100  # Convert from cents to dollars
            price = round(cost * price_multiplier, 2)
            price_cents = int(price * 100)  # Convert back to cents
            
            variant_data = {
                'id': variant['id'],
                'price': price_cents,
                'is_enabled': True
            }
            variants.append(variant_data)
            
        # Get blueprint details to determine print areas
        blueprint_details = self.get_blueprint_details(blueprint_id)
        print_areas = {}
        
        # For simplicity, use the same image for all print areas
        for print_area in blueprint_details.get('print_areas', []):
            print_areas[print_area['id']] = {
                'placement': 'center',
                'images': [
                    {
                        'id': image_id,
                        'x': 0.5,
                        'y': 0.5,
                        'scale': 1.0,
                        'angle': 0
                    }
                ]
            }
            
        # Prepare product data
        product_data = {
            'title': title,
            'description': description,
            'blueprint_id': blueprint_id,
            'print_provider_id': print_provider_id,
            'variants': variants,
            'print_areas': print_areas
        }
        
        # Add tags if provided
        if tags:
            product_data['tags'] = tags
            
        return product_data
        
    def create_and_publish_product(self,
                                 image_path: str,
                                 title: str,
                                 description: str,
                                 blueprint_id: int,
                                 print_provider_id: int,
                                 variant_ids: List[int] = None,
                                 tags: List[str] = None,
                                 price_multiplier: float = 2.0,
                                 shop_id: str = None,
                                 publish: bool = True) -> Dict[str, Any]:
        """
        Create and optionally publish a product from an image in one operation.
        
        Args:
            image_path: Path to the image file
            title: Product title
            description: Product description
            blueprint_id: Blueprint ID
            print_provider_id: Print provider ID
            variant_ids: List of variant IDs to include
            tags: List of tags for the product
            price_multiplier: Multiplier for setting the retail price
            shop_id: Shop ID. If None, uses the default shop_id.
            publish: Whether to publish the product after creation
            
        Returns:
            Dictionary with created product information and publish status
        """
        shop_id = shop_id or self.shop_id
        if not shop_id:
            raise ValueError("Shop ID is required")
            
        # Prepare product data
        product_data = self.prepare_product_from_image(
            image_path=image_path,
            title=title,
            description=description,
            blueprint_id=blueprint_id,
            print_provider_id=print_provider_id,
            variant_ids=variant_ids,
            tags=tags,
            price_multiplier=price_multiplier
        )
        
        # Create the product
        create_response = self.create_product(shop_id=shop_id, product_data=product_data)
        if 'id' not in create_response:
            return {
                'success': False,
                'error': 'Failed to create product',
                'response': create_response
            }
            
        product_id = create_response['id']
        result = {
            'success': True,
            'product': create_response,
            'published': False
        }
        
        # Publish if requested
        if publish:
            publish_response = self.publish_product(shop_id=shop_id, product_id=product_id)
            result['publish_response'] = publish_response
            result['published'] = publish_response.get('status') == 'published'
            
        return result

# Example usage
if __name__ == "__main__":
    import sys
    import os
    from pprint import pprint
    
    # Determine project root
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    # Add project root to sys.path
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
        
    # Load .env file
    dotenv_path = os.path.join(PROJECT_ROOT, '.env')
    if os.path.exists(dotenv_path):
        from dotenv import load_dotenv
        print(f"Loading .env file from: {dotenv_path}")
        load_dotenv(dotenv_path=dotenv_path)
        
    # Create Printify API client
    printify = PrintifyAPI()
    
    # Get connected shops
    shops = printify.get_shops()
    print("\nConnected shops:")
    for shop in shops:
        print(f"  - {shop['title']} (ID: {shop['id']}, Platform: {shop['shop_type']})")
        
    # Find wall art blueprints
    wall_art_blueprints = printify.find_wall_art_blueprints()
    print("\nWall art blueprints:")
    for blueprint in wall_art_blueprints[:5]:  # Show first 5
        print(f"  - {blueprint['title']} (ID: {blueprint['id']})")
        
    if wall_art_blueprints:
        # Get details for the first wall art blueprint
        blueprint_id = wall_art_blueprints[0]['id']
        print(f"\nGetting details for blueprint ID {blueprint_id}...")
        blueprint_details = printify.get_blueprint_details(blueprint_id)
        print(f"Title: {blueprint_details['title']}")
        print(f"Description: {blueprint_details['description']}")
        
        # Get print providers for this blueprint
        print(f"\nGetting print providers for blueprint ID {blueprint_id}...")
        providers = printify.get_print_providers(blueprint_id)
        for provider in providers:
            print(f"  - {provider['title']} (ID: {provider['id']})")
````

## File: src/phase4_etsy_management/__init__.py
````python
# Phase 4: Etsy Management package initialization
````

## File: src/phase5_search_discovery/__init__.py
````python
# Phase 5: Search Discovery package initialization

from .search_discovery import SearchDiscovery, QueryAgent, RetrievalAgent, RerankerAgent, SummarizationAgent

__all__ = [
    'SearchDiscovery',
    'QueryAgent',
    'RetrievalAgent',
    'RerankerAgent',
    'SummarizationAgent'
]
````

## File: src/phase5_search_discovery/search_discovery.py
````python
"""
Instagram to Etsy Automation - Phase 5: Search Discovery

This module implements the Multi-agent Retrieval Protocol for intelligent content discovery,
search capabilities, and optimization of content acquisition from Instagram.

Components:
1. QueryAgent: Refines and optimizes search queries
2. RetrievalAgent: Executes searches against Instagram
3. RerankerAgent: Reranks and filters results for relevance
4. SummarizationAgent: Generates metadata for Etsy listings
"""

import os
import logging
import json
import time
from typing import List, Dict, Any, Optional, Tuple
import random

from .. import config
from ..phase1_acquisition.instagram_scraper import process_instagram_posts

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SearchDiscovery:
    """
    Implements the Multi-agent Retrieval Protocol for intelligent content discovery
    from Instagram and optimization for Etsy listing generation.
    """
    
    def __init__(self, base_dir: str = 'data'):
        """
        Initialize the search discovery system.
        
        Args:
            base_dir: Base directory for storing search results and metadata
        """
        self.base_dir = base_dir
        self.query_agent = QueryAgent()
        self.retrieval_agent = RetrievalAgent(base_dir=base_dir)
        self.reranker_agent = RerankerAgent()
        self.summarization_agent = SummarizationAgent()
        
        # Create directories for search results
        os.makedirs(os.path.join(base_dir, 'search'), exist_ok=True)
        os.makedirs(os.path.join(base_dir, 'search', 'results'), exist_ok=True)
        os.makedirs(os.path.join(base_dir, 'search', 'metadata'), exist_ok=True)
        
        logger.info("Search Discovery system initialized")
        
    def discover_content(self, 
                        search_query: str, 
                        max_results: int = 10,
                        min_quality_score: float = 0.7) -> Dict[str, Any]:
        """
        Execute the full discovery workflow to find relevant content on Instagram.
        
        Args:
            search_query: The user's search query or content requirements
            max_results: Maximum number of results to return
            min_quality_score: Minimum quality score for results
            
        Returns:
            Dictionary containing search results and metadata
        """
        logger.info(f"Starting content discovery for query: {search_query}")
        start_time = time.time()
        
        # Step 1: Query refinement
        refined_queries = self.query_agent.refine_query(search_query)
        logger.info(f"Generated {len(refined_queries)} refined queries")
        
        # Step 2: Content retrieval
        all_results = []
        for query in refined_queries:
            query_text = query['query']
            query_score = query['score']
            
            logger.info(f"Executing retrieval for query: {query_text} (score: {query_score:.2f})")
            results = self.retrieval_agent.retrieve_content(query_text)
            
            # Add query metadata to results
            for result in results:
                result['query_text'] = query_text
                result['query_score'] = query_score
                
            all_results.extend(results)
            
        logger.info(f"Retrieved {len(all_results)} total results across all queries")
        
        # Step 3: Reranking and filtering
        ranked_results = self.reranker_agent.rerank_results(all_results, search_query)
        
        # Filter by quality score
        filtered_results = [
            r for r in ranked_results 
            if r.get('quality_score', 0) >= min_quality_score
        ]
        
        # Limit to max_results
        top_results = filtered_results[:max_results]
        
        logger.info(f"After reranking and filtering: {len(top_results)} results meet quality threshold")
        
        # Step 4: Generate metadata
        for result in top_results:
            result['etsy_metadata'] = self.summarization_agent.generate_metadata(
                result, search_query
            )
            
        # Save search results
        timestamp = int(time.time())
        results_path = os.path.join(self.base_dir, 'search', 'results', f"search_{timestamp}.json")
        with open(results_path, 'w') as f:
            json.dump({
                'query': search_query,
                'timestamp': timestamp,
                'execution_time': time.time() - start_time,
                'total_results': len(all_results),
                'filtered_results': len(filtered_results),
                'returned_results': len(top_results),
                'results': top_results
            }, f, indent=2)
            
        logger.info(f"Search discovery complete. Results saved to {results_path}")
        
        return {
            'query': search_query,
            'total_results': len(all_results),
            'returned_results': len(top_results),
            'results': top_results,
            'results_path': results_path
        }

class QueryAgent:
    """
    Agent for refining and expanding user queries to optimize search results.
    Implements the Query Agent role from the Multi-agent Retrieval Protocol.
    """
    
    def __init__(self):
        """Initialize the query agent."""
        pass
        
    def refine_query(self, query: str) -> List[Dict[str, Any]]:
        """
        Refine and expand a user query into multiple search variations.
        
        Args:
            query: The original user query
            
        Returns:
            List of refined queries with relevance scores
        """
        # Simplified implementation - in production, this would use more sophisticated
        # NLP techniques or potentially call out to an LLM for query refinement
        
        # Extract main keywords
        keywords = [k.strip() for k in query.lower().split() if len(k.strip()) > 3]
        
        # Generate variations
        variations = [
            {'query': query, 'score': 1.0},  # Original query with highest score
        ]
        
        # Add Instagram-specific variations
        if 'landscape' in query.lower():
            variations.append({
                'query': f"beautiful landscape photography {' '.join(keywords[:2] if len(keywords) > 2 else keywords)}",
                'score': 0.9
            })
            variations.append({
                'query': f"scenic landscape views {' '.join(keywords[:2] if len(keywords) > 2 else keywords)}",
                'score': 0.85
            })
            
        if 'mountain' in query.lower():
            variations.append({
                'query': f"mountain peaks photography {' '.join(keywords[:2] if len(keywords) > 2 else keywords)}",
                'score': 0.9
            })
            
        if 'water' in query.lower() or 'lake' in query.lower() or 'ocean' in query.lower():
            variations.append({
                'query': f"water reflection photography {' '.join(keywords[:2] if len(keywords) > 2 else keywords)}",
                'score': 0.9
            })
            
        # Add some general high-performing searches
        variations.append({
            'query': f"fine art landscape photography {' '.join(keywords[:1] if keywords else '')}",
            'score': 0.8
        })
        variations.append({
            'query': f"professional nature photography {' '.join(keywords[:1] if keywords else '')}",
            'score': 0.75
        })
        
        # Ensure we have at least 3 query variations
        if len(variations) < 3:
            variations.append({
                'query': f"beautiful photography {' '.join(keywords)}",
                'score': 0.7
            })
            
        return variations

class RetrievalAgent:
    """
    Agent for retrieving content from Instagram based on refined queries.
    Implements the Retrieval Agent role from the Multi-agent Retrieval Protocol.
    """
    
    def __init__(self, base_dir: str = 'data'):
        """
        Initialize the retrieval agent.
        
        Args:
            base_dir: Base directory for storing retrieved content
        """
        self.base_dir = base_dir
        
    def retrieve_content(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve content from Instagram based on the query.
        
        Args:
            query: Search query
            max_results: Maximum number of results to retrieve
            
        Returns:
            List of retrieved content items
        """
        # Convert query to Instagram profile search
        # This is a simplified implementation - in production, this would
        # use more sophisticated techniques to find relevant Instagram profiles
        
        # For now, we'll use the configured profiles and pretend we're searching
        logger.info(f"Searching Instagram for content matching: {query}")
        
        # In a real implementation, this would search for profiles based on the query
        # For now, we'll use the configured profiles from config
        if not config.INSTAGRAM_TARGET_PROFILES:
            logger.warning("No Instagram profiles configured for retrieval")
            return []
            
        # Use a subset of configured profiles (simulating search results)
        profiles_to_search = config.INSTAGRAM_TARGET_PROFILES
        
        # Use the Instagram scraper to get posts
        try:
            posts = process_instagram_posts(
                profile_urls=profiles_to_search,
                max_posts=max_results * 2,  # Get more than we need for filtering
                landscape_only=True,
                base_dir=self.base_dir
            )
            
            # Extract relevant information and add retrieval metadata
            results = []
            for post in posts:
                # Add retrieval metadata
                post['retrieval_query'] = query
                post['retrieval_timestamp'] = time.time()
                post['initial_score'] = random.uniform(0.7, 1.0)  # Simplified scoring
                
                results.append(post)
                
            logger.info(f"Retrieved {len(results)} results from Instagram")
            return results
            
        except Exception as e:
            logger.error(f"Error retrieving content from Instagram: {e}")
            return []

class RerankerAgent:
    """
    Agent for reranking and filtering retrieved content based on relevance and quality.
    Implements the Reranker Agent role from the Multi-agent Retrieval Protocol.
    """
    
    def __init__(self):
        """Initialize the reranker agent."""
        pass
        
    def rerank_results(self, results: List[Dict[str, Any]], original_query: str) -> List[Dict[str, Any]]:
        """
        Rerank and filter results based on relevance to the original query.
        
        Args:
            results: List of retrieved content items
            original_query: The original user query
            
        Returns:
            Reranked list of content items
        """
        if not results:
            return []
            
        # Analyze query for keywords
        query_keywords = set(original_query.lower().split())
        
        # Score each result
        for result in results:
            # Start with the initial score from retrieval
            score = result.get('initial_score', 0.5)
            
            # Adjust based on query relevance
            if 'caption' in result:
                caption = result['caption'].lower() if result.get('caption') else ""
                caption_words = set(caption.split())
                
                # Calculate overlap between caption and query keywords
                overlap = query_keywords.intersection(caption_words)
                score += len(overlap) * 0.05
                
            # Adjust based on hashtags
            if 'hashtags' in result:
                hashtags = result.get('hashtags', [])
                for hashtag in hashtags:
                    if any(keyword in hashtag.lower() for keyword in query_keywords):
                        score += 0.03
                        
            # Adjust based on engagement metrics
            likes = result.get('likes', 0)
            comments = result.get('comments', 0)
            
            # Simple engagement score - more sophisticated in production
            engagement_score = min((likes + comments * 3) / 1000, 0.2)
            score += engagement_score
            
            # Prefer landscape images
            if result.get('is_landscape', False):
                score += 0.1
                
            # Adjust based on image quality if available
            if 'image_metadata' in result:
                metadata = result.get('image_metadata', {})
                
                # Higher resolution images get a boost
                width = metadata.get('width', 0)
                height = metadata.get('height', 0)
                resolution_score = min((width * height) / (1920 * 1080 * 4), 0.15)
                score += resolution_score
                
            # Cap the score at 1.0
            score = min(score, 1.0)
            
            # Add the quality score to the result
            result['quality_score'] = score
            
        # Sort by quality score
        ranked_results = sorted(results, key=lambda x: x.get('quality_score', 0), reverse=True)
        
        # Remove duplicates based on image similarity (simplified)
        # In production, this would use more sophisticated image similarity checks
        deduplicated_results = []
        seen_shortcodes = set()
        
        for result in ranked_results:
            shortcode = result.get('shortcode', '')
            
            if shortcode and shortcode not in seen_shortcodes:
                seen_shortcodes.add(shortcode)
                deduplicated_results.append(result)
                
        logger.info(f"Reranked {len(results)} results to {len(deduplicated_results)} deduplicated results")
        return deduplicated_results

class SummarizationAgent:
    """
    Agent for generating metadata and descriptions for Etsy listings.
    Implements the Summarization Agent role from the Multi-agent Retrieval Protocol.
    """
    
    def __init__(self):
        """Initialize the summarization agent."""
        pass
        
    def generate_metadata(self, content_item: Dict[str, Any], query: str) -> Dict[str, Any]:
        """
        Generate Etsy-optimized metadata for a content item.
        
        Args:
            content_item: The content item to generate metadata for
            query: The original search query
            
        Returns:
            Dictionary of Etsy-optimized metadata
        """
        # Extract existing metadata
        caption = content_item.get('caption', '')
        hashtags = content_item.get('hashtags', [])
        location = content_item.get('location', 'Beautiful Location')
        
        # Generate title
        title_keywords = [
            'Fine Art Print',
            'Landscape Photography',
            'Wall Art',
            'Home Decor',
            'Nature Print'
        ]
        
        # Use location if available
        if location and location != 'Beautiful Location':
            title = f"{location} - Fine Art Landscape Photography Print - Wall Art"
        else:
            # Extract potential title from caption
            caption_words = caption.split()[:10] if caption else []
            caption_excerpt = ' '.join(caption_words)
            
            # Fallback title
            title = f"Landscape Photography Wall Art Print - Fine Art Nature Print"
            
            # Use caption excerpt if it's substantial
            if len(caption_excerpt) > 20:
                title = f"{caption_excerpt} - Fine Art Landscape Print"
                
        # Generate description
        description = f"Beautiful landscape photography fine art print"
        
        if location and location != 'Beautiful Location':
            description += f" of {location}"
            
        description += ". Perfect for home decor, office spaces, or as a thoughtful gift. "
        description += "This premium quality print captures the beauty of nature with vibrant colors and exceptional detail.\n\n"
        
        # Add more details if we have a caption
        if caption and len(caption) > 30:
            description += f"About this image:\n{caption}\n\n"
            
        description += "Available in multiple sizes and materials to fit your space.\n\n"
        description += "• Printed on premium fine art paper with archival inks for vibrant colors and detail\n"
        description += "• Available as canvas prints and framed prints\n"
        description += "• Each print is made to order\n"
        description += "• Ships within 2-5 business days\n\n"
        description += "Note: Frame not included unless selected as an option."
        
        # Generate SEO tags
        tags = []
        
        # Add hashtags from Instagram (remove # symbol)
        hashtag_tags = [tag.replace('#', '').lower() for tag in hashtags]
        tags.extend(hashtag_tags[:5])  # Use up to 5 hashtags
        
        # Add standard tags
        standard_tags = [
            'landscape photography',
            'wall art',
            'fine art print',
            'home decor',
            'nature print',
            'photography print',
            'wall decor'
        ]
        
        # Add location-based tag if available
        if location and location != 'Beautiful Location':
            tags.append(location.lower())
            
        # Combine and deduplicate tags
        all_tags = list(set(tags + standard_tags))
        
        # Limit to 13 tags (Etsy maximum)
        final_tags = all_tags[:13]
        
        return {
            'title': title,
            'description': description,
            'tags': final_tags
        }
````

## File: src/utils/__init__.py
````python
# Utils package initialization
````

## File: src/utils/gcs_storage.py
````python
import os
import logging
from typing import Optional, Dict, Any, List
from google.cloud import storage
from google.oauth2 import service_account
from .. import config

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GCSStorage:
    def __init__(self):
        """Initialize GCS client using credentials from config."""
        try:
            # Check if credentials path is set
            if not config.GOOGLE_APPLICATION_CREDENTIALS:
                logger.warning("GCS credentials path not set. GCS operations will not work.")
                self.client = None
                self.bucket = None
                return
                
            # Check if credentials file exists
            if not os.path.exists(config.GOOGLE_APPLICATION_CREDENTIALS):
                logger.warning(f"GCS credentials file not found at {config.GOOGLE_APPLICATION_CREDENTIALS}. GCS operations will not work.")
                self.client = None
                self.bucket = None
                return
                
            # Initialize GCS client
            credentials = service_account.Credentials.from_service_account_file(
                config.GOOGLE_APPLICATION_CREDENTIALS
            )
            self.client = storage.Client(credentials=credentials, project=config.GCS_PROJECT_ID)
            
            # Get the bucket
            if not config.GCS_BUCKET_NAME:
                logger.warning("GCS bucket name not set. GCS operations will not work.")
                self.bucket = None
                return
                
            self.bucket = self.client.bucket(config.GCS_BUCKET_NAME)
            logger.info(f"Successfully initialized GCS client for bucket {config.GCS_BUCKET_NAME}")
        except Exception as e:
            logger.error(f"Error initializing GCS client: {e}")
            self.client = None
            self.bucket = None
            
    def is_available(self) -> bool:
        """Check if GCS client is available and properly configured."""
        return self.client is not None and self.bucket is not None
        
    def upload_file(self, source_file_path: str, destination_blob_name: str) -> bool:
        """
        Upload a file to GCS bucket.
        
        Args:
            source_file_path: Path to the local file to upload.
            destination_blob_name: Name to give the file in GCS.
            
        Returns:
            True if upload was successful, False otherwise.
        """
        if not self.is_available():
            logger.error("GCS client not available. Cannot upload file.")
            return False
            
        try:
            blob = self.bucket.blob(destination_blob_name)
            blob.upload_from_filename(source_file_path)
            logger.info(f"File {source_file_path} uploaded to {destination_blob_name}.")
            return True
        except Exception as e:
            logger.error(f"Error uploading file to GCS: {e}")
            return False
            
    def upload_from_string(self, data: str, destination_blob_name: str, content_type: str = 'text/plain') -> bool:
        """
        Upload data from a string to GCS bucket.
        
        Args:
            data: String data to upload.
            destination_blob_name: Name to give the file in GCS.
            content_type: MIME type of the data.
            
        Returns:
            True if upload was successful, False otherwise.
        """
        if not self.is_available():
            logger.error("GCS client not available. Cannot upload data.")
            return False
            
        try:
            blob = self.bucket.blob(destination_blob_name)
            blob.upload_from_string(data, content_type=content_type)
            logger.info(f"Data uploaded to {destination_blob_name}.")
            return True
        except Exception as e:
            logger.error(f"Error uploading data to GCS: {e}")
            return False
            
    def download_file(self, source_blob_name: str, destination_file_path: str) -> bool:
        """
        Download a file from GCS bucket.
        
        Args:
            source_blob_name: Name of the file in GCS.
            destination_file_path: Path to save the file locally.
            
        Returns:
            True if download was successful, False otherwise.
        """
        if not self.is_available():
            logger.error("GCS client not available. Cannot download file.")
            return False
            
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)
            
            blob = self.bucket.blob(source_blob_name)
            blob.download_to_filename(destination_file_path)
            logger.info(f"File {source_blob_name} downloaded to {destination_file_path}.")
            return True
        except Exception as e:
            logger.error(f"Error downloading file from GCS: {e}")
            return False
            
    def list_files(self, prefix: str = '') -> List[str]:
        """
        List files in the GCS bucket with the given prefix.
        
        Args:
            prefix: Prefix to filter files by.
            
        Returns:
            A list of file names in the bucket matching the prefix.
        """
        if not self.is_available():
            logger.error("GCS client not available. Cannot list files.")
            return []
            
        try:
            blobs = self.client.list_blobs(self.bucket, prefix=prefix)
            return [blob.name for blob in blobs]
        except Exception as e:
            logger.error(f"Error listing files in GCS: {e}")
            return []
            
    def file_exists(self, blob_name: str) -> bool:
        """
        Check if a file exists in the GCS bucket.
        
        Args:
            blob_name: Name of the file in GCS.
            
        Returns:
            True if the file exists, False otherwise.
        """
        if not self.is_available():
            logger.error("GCS client not available. Cannot check if file exists.")
            return False
            
        try:
            blob = self.bucket.blob(blob_name)
            return blob.exists()
        except Exception as e:
            logger.error(f"Error checking if file exists in GCS: {e}")
            return False
            
    def delete_file(self, blob_name: str) -> bool:
        """
        Delete a file from the GCS bucket.
        
        Args:
            blob_name: Name of the file in GCS.
            
        Returns:
            True if deletion was successful, False otherwise.
        """
        if not self.is_available():
            logger.error("GCS client not available. Cannot delete file.")
            return False
            
        try:
            blob = self.bucket.blob(blob_name)
            blob.delete()
            logger.info(f"File {blob_name} deleted from GCS.")
            return True
        except Exception as e:
            logger.error(f"Error deleting file from GCS: {e}")
            return False
````

## File: src/utils/image_utils.py
````python
import os
import requests
from PIL import Image
from io import BytesIO
import logging
from typing import Tuple, Dict, Optional, List, Any

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def download_image(url: str, save_path: Optional[str] = None) -> Optional[bytes]:
    """
    Download an image from a URL.
    
    Args:
        url: The URL of the image to download.
        save_path: Optional path to save the image to. If None, image is not saved to disk.
        
    Returns:
        The image data as bytes if successful, None otherwise.
    """
    try:
        logger.info(f"Downloading image from {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Get the image data
        image_data = response.content
        
        # Save the image if a path is provided
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(image_data)
            logger.info(f"Image saved to {save_path}")
            
        return image_data
    except Exception as e:
        logger.error(f"Error downloading image from {url}: {e}")
        return None

def get_image_dimensions(image_data: bytes) -> Optional[Tuple[int, int]]:
    """
    Get the dimensions of an image from its binary data.
    
    Args:
        image_data: The image data as bytes.
        
    Returns:
        A tuple of (width, height) if successful, None otherwise.
    """
    try:
        img = Image.open(BytesIO(image_data))
        return img.size
    except Exception as e:
        logger.error(f"Error getting image dimensions: {e}")
        return None

def is_landscape(image_data: bytes, min_ratio: float = 1.2) -> bool:
    """
    Check if an image is in landscape orientation.
    
    Args:
        image_data: The image data as bytes.
        min_ratio: The minimum width-to-height ratio to consider as landscape.
                  Default is 1.2 (20% wider than tall).
        
    Returns:
        True if the image is in landscape orientation, False otherwise.
    """
    dimensions = get_image_dimensions(image_data)
    if not dimensions:
        return False
        
    width, height = dimensions
    return width / height >= min_ratio

def get_image_metadata(image_data: bytes) -> Dict[str, Any]:
    """
    Extract metadata from an image.
    
    Args:
        image_data: The image data as bytes.
        
    Returns:
        A dictionary containing metadata about the image.
    """
    metadata = {}
    try:
        img = Image.open(BytesIO(image_data))
        metadata['format'] = img.format
        metadata['mode'] = img.mode
        metadata['width'], metadata['height'] = img.size
        metadata['aspect_ratio'] = metadata['width'] / metadata['height']
        
        # Extract EXIF data if available
        if hasattr(img, '_getexif') and img._getexif():
            exif = {
                ExifTags.TAGS[k]: v
                for k, v in img._getexif().items()
                if k in ExifTags.TAGS
            }
            metadata['exif'] = exif
    except Exception as e:
        logger.error(f"Error extracting image metadata: {e}")
    
    return metadata

def create_storage_structure(base_dir: str) -> Dict[str, str]:
    """
    Create a directory structure for storing images and metadata.
    
    Args:
        base_dir: The base directory to create the structure in.
        
    Returns:
        A dictionary mapping directory names to their paths.
    """
    structure = {
        'original': os.path.join(base_dir, 'original'),
        'processed': os.path.join(base_dir, 'processed'),
        'metadata': os.path.join(base_dir, 'metadata'),
        'temp': os.path.join(base_dir, 'temp')
    }
    
    for dir_path in structure.values():
        os.makedirs(dir_path, exist_ok=True)
        logger.info(f"Created directory: {dir_path}")
        
    return structure
````

## File: src/main.py
````python
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
from src.phase1_acquisition.instagram_scraper import InstagramScraper
from src.phase1_acquisition.image_filter import ImageFilter
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
    Run the Instagram acquisition phase.
    
    Args:
        args: Command line arguments
        
    Returns:
        List of downloaded image paths
    """
    logger.info("Starting Instagram acquisition phase")
    
    # Initialize Instagram scraper
    username = args.instagram_user or config.INSTAGRAM_USERNAME
    if not username:
        raise ValueError("Instagram username not provided in args or config")
    
    scraper = InstagramScraper(
        username=username,
        output_dir=args.input_dir
    )
    
    # Scrape images
    logger.info(f"Scraping images from Instagram user: {username}")
    scraped_images = scraper.scrape_user_media(limit=args.limit)
    
    # Filter images
    logger.info("Filtering images based on criteria")
    image_filter = ImageFilter()
    filtered_images = image_filter.filter_images(
        image_paths=scraped_images,
        min_width=1200,
        min_height=1200,
        aspect_ratio_range=(0.5, 2.0),  # Allow landscape and portrait
        prefer_landscape=True
    )
    
    logger.info(f"Acquisition complete. {len(filtered_images)} images passed filtering.")
    return filtered_images

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
    
    processor = ImageProcessor(use_gcs=config.USE_GCS)
    
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
````

## File: run.py
````python
#!/usr/bin/env python3
"""
Instagram to Etsy Automation - Main Runner

This script provides a convenient entry point to run the entire workflow.
"""

import os
import sys
import argparse
from src.main import parse_arguments, run_workflow

def main():
    """Main entry point for the application."""
    # Parse arguments
    args = parse_arguments()
    
    # Run the workflow
    metrics = run_workflow(args)
    
    # Exit with appropriate code
    sys.exit(0 if metrics['errors'] == 0 else 1)

if __name__ == "__main__":
    # Ensure we're running from the project root
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    
    # Run the main function
    main()
````

## File: src/phase1_acquisition/instagram_scraper.py
````python
import os
import json
import logging
from typing import List, Dict, Optional, Any, Tuple
from apify_client import ApifyClient
from .. import config
from ..utils.image_utils import download_image, is_landscape, get_image_metadata, create_storage_structure
from ..utils.gcs_storage import GCSStorage

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class InstagramScraper:
    """
    Class for scraping Instagram posts and downloading images.
    Wraps around the functional Instagram scraping utilities.
    """
    
    def __init__(self, username: str = None, output_dir: str = 'data'):
        """
        Initialize the Instagram scraper.
        
        Args:
            username: Instagram username to scrape. If None, uses profiles from config.
            output_dir: Directory to store downloaded images and metadata.
        """
        self.username = username
        self.output_dir = output_dir
        
        # Create storage directories
        self.storage_paths = create_storage_structure(output_dir)
        
        # Determine profile URLs based on username or config
        if username:
            self.profile_urls = [f"https://www.instagram.com/{username}/"]
        else:
            self.profile_urls = config.INSTAGRAM_TARGET_PROFILES
            
        if not self.profile_urls:
            logger.warning("No Instagram profile URLs provided or configured.")
            
        # Initialize Apify client if token is available
        if not config.APIFY_API_TOKEN:
            logger.error("APIFY_API_TOKEN not found. Please set it in your .env file.")
            self.apify_client = None
        else:
            self.apify_client = initialize_apify_client()
            
        logger.info(f"Instagram scraper initialized for profiles: {self.profile_urls}")
    
    def scrape_user_media(self, limit: int = 10) -> List[str]:
        """
        Scrape media from the user's Instagram profile.
        
        Args:
            limit: Maximum number of posts to retrieve.
            
        Returns:
            List of paths to downloaded images.
        """
        if not self.apify_client:
            logger.error("Apify client not initialized. Cannot scrape Instagram.")
            return []
            
        # Scrape posts using the functional approach
        posts = process_instagram_posts(
            profile_urls=self.profile_urls,
            max_posts=limit,
            landscape_only=True,
            base_dir=self.output_dir,
            use_gcs=config.USE_GCS
        )
        
        # Extract image paths from processed posts
        image_paths = [post['local_path'] for post in posts if 'local_path' in post]
        
        logger.info(f"Scraped {len(image_paths)} images from Instagram")
        return image_paths

# Validation check for Apify token
if not config.APIFY_API_TOKEN:
    logger.error("APIFY_API_TOKEN not found. Please set it in your .env file.")
    # Depending on execution context, might want to raise an exception or exit

def initialize_apify_client():
    """Initializes and returns the ApifyClient with the API token."""
    if not config.APIFY_API_TOKEN:
        raise ValueError("APIFY_API_TOKEN is not configured.")
    return ApifyClient(config.APIFY_API_TOKEN)

def extract_hashtags(caption: str) -> List[str]:
    """
    Extract hashtags from a post caption.
    
    Args:
        caption: The post caption text.
        
    Returns:
        A list of hashtags found in the caption.
    """
    if not caption:
        return []
        
    # Split by spaces and filter for words starting with #
    words = caption.split()
    hashtags = [word.strip('#') for word in words if word.startswith('#')]
    
    return hashtags

def extract_post_metadata(post: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract useful metadata from an Instagram post.
    
    Args:
        post: The Instagram post data from Apify.
        
    Returns:
        A dictionary of metadata extracted from the post.
    """
    metadata = {
        'post_id': post.get('id'),
        'shortcode': post.get('shortCode'),
        'timestamp': post.get('timestamp'),
        'caption': post.get('caption', ''),
        'hashtags': extract_hashtags(post.get('caption', '')),
        'likes': post.get('likesCount', 0),
        'comments': post.get('commentsCount', 0),
        'owner_username': post.get('ownerUsername', ''),
        'owner_id': post.get('ownerId', ''),
        'url': post.get('url', ''),
        'location': post.get('locationName', ''),
        'is_video': post.get('isVideo', False),
    }
    
    return metadata

def run_instagram_scraper_for_profiles(client: ApifyClient, profile_urls: List[str], max_posts_per_profile: int = 100):
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
        run = actor.call(run_input=actor_input, timeout_secs=300) # Wait up to 5 minutes for potentially larger scrapes
        print(f"Scraping run for profiles finished. Run ID: {run.get('id')}, Dataset ID: {run.get('defaultDatasetId')}")
        return run
    except Exception as e:
        print(f"Error running Instagram scraper for profiles {profile_urls}: {e}")
        return None

def get_scraped_data(client: ApifyClient, run_id: str) -> Optional[List[Dict[str, Any]]]:
    """
    Fetches items from the dataset produced by an Actor run.

    Args:
        client: An initialized ApifyClient instance.
        run_id: The ID of the Actor run.

    Returns:
        A list of items from the dataset, or None if an error occurs.
    """
    if not run_id:
        logger.error("No run_id provided to fetch scraped data.")
        return None
        
    logger.info(f"Fetching dataset for run ID: {run_id}...")
    try:
        dataset_items = client.dataset(run_id).list_items().items
        logger.info(f"Successfully fetched {len(dataset_items)} items from dataset {run_id}.")
        return dataset_items
    except Exception as e:
        logger.error(f"Error fetching dataset items for run ID {run_id}: {e}")
        return None
        
def download_images_from_posts(posts: List[Dict[str, Any]], 
                               base_dir: str = 'data',
                               min_landscape_ratio: float = 1.2,
                               landscape_only: bool = True,
                               use_gcs: bool = True) -> List[Dict[str, Any]]:
    """
    Download images from Instagram posts, filter for landscape orientation if specified,
    and store metadata.
    
    Args:
        posts: List of Instagram post data from Apify.
        base_dir: Base directory for local storage.
        min_landscape_ratio: Minimum width/height ratio to consider as landscape.
        landscape_only: Whether to filter for landscape images only.
        use_gcs: Whether to upload images to Google Cloud Storage.
        
    Returns:
        A list of processed post dictionaries with local paths and metadata.
    """
    # Create storage structure
    storage_paths = create_storage_structure(base_dir)
    
    # Initialize GCS client if needed
    gcs = GCSStorage() if use_gcs else None
    if use_gcs and not gcs.is_available():
        logger.warning("GCS client not available. Falling back to local storage only.")
        use_gcs = False
    
    processed_posts = []
    
    for i, post in enumerate(posts):
        try:
            # Skip videos if present
            if post.get('isVideo', False):
                logger.info(f"Skipping video post: {post.get('shortCode')}")
                continue
                
            # Get image URL - prefer displayUrl for highest quality
            image_url = post.get('displayUrl')
            if not image_url and 'images' in post and post['images']:
                # Fallback to first image in images array
                image_url = post['images'][0]
                
            if not image_url:
                logger.warning(f"No image URL found for post {post.get('shortCode')}")
                continue
                
            # Extract post metadata
            post_metadata = extract_post_metadata(post)
            shortcode = post.get('shortCode', f"unknown_{i}")
            
            # Generate local filename and path
            local_filename = f"{post_metadata['owner_username']}_{shortcode}.jpg"
            local_path = os.path.join(storage_paths['original'], local_filename)
            
            # Download image
            image_data = download_image(image_url, local_path)
            if not image_data:
                logger.warning(f"Failed to download image for post {shortcode}")
                continue
                
            # Check if landscape orientation
            landscape = is_landscape(image_data, min_landscape_ratio)
            post_metadata['is_landscape'] = landscape
            
            # Skip if not landscape and we only want landscape images
            if landscape_only and not landscape:
                logger.info(f"Skipping non-landscape image for post {shortcode}")
                # Delete the downloaded file
                if os.path.exists(local_path):
                    os.remove(local_path)
                continue
                
            # Extract image metadata
            image_metadata = get_image_metadata(image_data)
            post_metadata['image_metadata'] = image_metadata
            post_metadata['local_path'] = local_path
            
            # Save metadata to JSON file
            metadata_path = os.path.join(storage_paths['metadata'], f"{shortcode}_metadata.json")
            with open(metadata_path, 'w') as f:
                json.dump(post_metadata, f, indent=2)
                
            # Upload to GCS if configured
            if use_gcs:
                # Upload image
                gcs_image_path = f"images/original/{local_filename}"
                if gcs.upload_file(local_path, gcs_image_path):
                    post_metadata['gcs_path'] = gcs_image_path
                
                # Upload metadata
                gcs_metadata_path = f"metadata/{shortcode}_metadata.json"
                gcs.upload_file(metadata_path, gcs_metadata_path)
                
            # Add to processed posts
            processed_posts.append(post_metadata)
            logger.info(f"Successfully processed post {shortcode}")
            
        except Exception as e:
            logger.error(f"Error processing post {post.get('shortCode', 'unknown')}: {e}")
            continue
            
    logger.info(f"Downloaded {len(processed_posts)} images out of {len(posts)} posts.")
    return processed_posts

def process_instagram_posts(profile_urls: List[str] = None, 
                            max_posts: int = 100,
                            landscape_only: bool = True, 
                            min_landscape_ratio: float = 1.2,
                            base_dir: str = 'data',
                            use_gcs: bool = True) -> List[Dict[str, Any]]:
    """
    Complete workflow to scrape Instagram posts, download images, and process metadata.
    
    Args:
        profile_urls: List of Instagram profile URLs to scrape. Defaults to config value.
        max_posts: Maximum number of posts to fetch per profile.
        landscape_only: Whether to filter for landscape images only.
        min_landscape_ratio: Minimum width/height ratio to consider as landscape.
        base_dir: Base directory for local storage.
        use_gcs: Whether to upload images to Google Cloud Storage.
        
    Returns:
        A list of processed posts with image paths and metadata.
    """
    # Use config profiles if none provided
    if not profile_urls:
        profile_urls = config.INSTAGRAM_TARGET_PROFILES
        
    if not profile_urls:
        logger.error("No Instagram profile URLs provided or configured.")
        return []
        
    # Initialize Apify client
    client = initialize_apify_client()
    
    # Run scraper
    logger.info(f"Starting Instagram scraping process for profiles: {profile_urls}")
    scraper_run = run_instagram_scraper_for_profiles(client, profile_urls, max_posts)
    
    if not scraper_run or not scraper_run.get('defaultDatasetId'):
        logger.error("Scraping failed or did not produce a dataset.")
        return []
        
    # Get scraped data
    dataset_id = scraper_run['defaultDatasetId']
    posts = get_scraped_data(client, dataset_id)
    
    if not posts:
        logger.error("No posts found in scraped data.")
        return []
        
    logger.info(f"Retrieved {len(posts)} posts from Instagram.")
    
    # Download and process images
    processed_posts = download_images_from_posts(
        posts, 
        base_dir=base_dir,
        min_landscape_ratio=min_landscape_ratio,
        landscape_only=landscape_only,
        use_gcs=use_gcs
    )
    
    return processed_posts

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
        
        # Test the full process
        print("\n--- Testing full Instagram scraping and image download process ---")
        processed_posts = process_instagram_posts(
            max_posts=5,  # Limit to 5 posts per profile for testing
            landscape_only=True,
            base_dir=os.path.join(PROJECT_ROOT, 'data'),
            use_gcs=False  # Set to True to test GCS upload if configured
        )
        
        if processed_posts:
            print(f"Successfully processed {len(processed_posts)} posts.")
            print("\nFirst processed post details:")
            first_post = processed_posts[0]
            print(f"  Username: {first_post.get('owner_username')}")
            print(f"  Post URL: {first_post.get('url')}")
            print(f"  Local path: {first_post.get('local_path')}")
            print(f"  Is landscape: {first_post.get('is_landscape')}")
            print(f"  Hashtags: {first_post.get('hashtags')}")
            if 'image_metadata' in first_post:
                img_meta = first_post['image_metadata']
                print(f"  Image dimensions: {img_meta.get('width')}x{img_meta.get('height')}")
                print(f"  Aspect ratio: {img_meta.get('aspect_ratio')}")
        else:
            print("No posts were processed. Check the logs for errors.")
````

## File: src/config.py
````python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Apify
APIFY_API_TOKEN = os.getenv('APIFY_API_TOKEN')

# Google Cloud Storage
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
GCS_BUCKET_NAME = os.getenv('GCS_BUCKET_NAME')

# Etsy
ETSY_API_KEY = os.getenv('ETSY_API_KEY')

# Printify
PRINTIFY_API_TOKEN = os.getenv('PRINTIFY_API_TOKEN')

# Instagram Scraper Configuration
# Expects comma-separated full Instagram profile URLs (e.g., https://www.instagram.com/username/)
INSTAGRAM_TARGET_PROFILES = [url.strip() for url in os.getenv('INSTAGRAM_TARGET_PROFILES', '').split(',') if url.strip()]

# Computer Vision Filtering
# Comma-separated descriptive terms for the CV model to filter images by (e.g., 'sunset', 'nyc street at dusk')
CV_CONTENT_DESCRIPTIONS_FILTER = [desc.strip() for desc in os.getenv('CV_CONTENT_DESCRIPTIONS_FILTER', '').split(',') if desc.strip()]

# Basic check to ensure critical tokens are loaded
if not APIFY_API_TOKEN:
    print("Warning: APIFY_API_TOKEN not found in .env file.")

if not GOOGLE_APPLICATION_CREDENTIALS or not GCS_BUCKET_NAME:
    print("Warning: Google Cloud Storage configuration (credentials or bucket name) not found in .env file.")

# Add more checks as needed for Etsy, Printify etc.
````

## File: .gitignore
````
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
myenv/
myenv/*
myenv/.*
venv/
venv/*
venv/.*
ENV/
env/
env.bak/
venv.bak/

# IDE / OS specific
.vscode/
.idea/
.DS_Store
*.swp
*.swo
*~
Thumbs.db
desktop.ini

# Credentials and environment variables
*.env
.env
.env.*
credentials.json
*_credentials.json
*_key.json
google_credentials.json

# Data files and directories
/data/*
!/data/.gitkeep
!/data/raw/.gitkeep
!/data/processed/.gitkeep
!/data/metadata/.gitkeep

# Logs
*.log
logs/
instagram_to_etsy.log

# Notebook checkpoints
.ipynb_checkpoints/
notebooks/.ipynb_checkpoints/

# Project specific
.clinerules/
.clinedirectory/

# Testing
.coverage
htmlcov/
.pytest_cache/
coverage.xml
*.cover

# Caches
.cache/
.pytest_cache/
.mypy_cache/
````

## File: Instagram-to-Etsy-Print-Shop .md
````markdown
\# Comprehensive Guide: Automated Instagram to Etsy Print Shop Pipeline

\#\# \*\*Overview\*\*

This guide provides a complete automated workflow to transform your Instagram landscape photography into a profitable Etsy print shop using print-on-demand services, with intelligent content-based image discovery.

\---

\#\# \*\*Phase 1: Instagram Image Acquisition & Content Analysis\*\*

\#\#\# \*\*1.1 Authentication & Access\*\*

\- \*\*Primary Method:\*\* Instagram Graph API (requires Instagram Business/Creator account)

\- \*\*Alternative:\*\* Instagram Basic Display API for personal accounts

\- \*\*Backup Method:\*\* Instagram MCP server for automated scraping

\#\#\# \*\*1.2 Image Discovery & Filtering\*\*

\`\`\`python

\# Key filtering criteria:

\- Aspect ratio detection (landscape: width \> height)

\- Hashtag filtering (\#landscape, \#nature, \#photography)

\- Image quality assessment (resolution, sharpness)

\- Engagement metrics (likes, comments) for popularity ranking

\- Date range filtering for recent content

\`\`\`

\#\#\# \*\*1.3 Computer Vision Content Analysis\*\*

Implement AI-powered image analysis for content-based search capabilities:

\#\#\#\# \*\*Visual Content Detection:\*\*

\`\`\`python

\# Core CV models and capabilities:

\- Object detection (mountains, trees, water, buildings, etc.)

\- Scene classification (sunset, sunrise, forest, beach, urban, etc.)

\- Color palette analysis (dominant colors, mood detection)

\- Weather condition recognition (cloudy, clear, stormy, foggy)

\- Time of day detection (golden hour, blue hour, midday, night)

\- Seasonal indicators (snow, autumn leaves, spring blooms)

\`\`\`

\#\#\#\# \*\*Advanced Visual Features:\*\*

\- \*\*Composition analysis:\*\* Rule of thirds, leading lines, symmetry

\- \*\*Lighting conditions:\*\* Backlighting, side lighting, dramatic shadows

\- \*\*Landscape elements:\*\* Waterfalls, lakes, mountains, coastlines, deserts

\- \*\*Architectural features:\*\* Bridges, buildings, monuments, ruins

\- \*\*Natural phenomena:\*\* Rainbows, lightning, star trails, aurora

\#\#\#\# \*\*Search Implementation:\*\*

\`\`\`python

\# Natural language to visual query translation:

\- "sunsets" → \[sky\_colors: orange/red/pink, time\_of\_day: evening, lighting: warm\]

\- "mountain lakes" → \[objects: mountain+water, scene: alpine\_lake\]

\- "stormy skies" → \[weather: storm, clouds: dramatic, mood: moody\]

\- "golden hour forests" → \[time: golden\_hour, objects: trees, lighting: warm\]

\`\`\`

\#\#\# \*\*1.4 Metadata Extraction & Enrichment\*\*

\- Location data (if available)

\- Caption text for description generation

\- Hashtags for SEO keyword extraction

\- Post engagement metrics

\- Image EXIF data (camera settings, etc.)

\- \*\*AI-generated tags:\*\* Visual content descriptors from CV analysis

\- \*\*Semantic embeddings:\*\* Vector representations for similarity search

\#\#\# \*\*1.5 Content Database Creation\*\*

\`\`\`python

\# Searchable image database structure:

{

  "image\_id": "unique\_identifier",

  "visual\_tags": \["sunset", "mountain", "reflection", "golden\_hour"\],

  "objects\_detected": \["sky", "water", "trees", "rocks"\],

  "scene\_type": "landscape\_water",

  "dominant\_colors": \["\#FF6B35", "\#F7931E", "\#FFD23F"\],

  "mood": "serene",

  "composition\_score": 8.5,

  "search\_embeddings": \[0.1, 0.3, \-0.2, ...\],  \# 512-dim vector

  "instagram\_metadata": {...},

  "file\_path": "/storage/images/img\_001.jpg"

}

\`\`\`

\#\#\# \*\*1.6 Download & Storage\*\*

\- Save original high-resolution images

\- Implement cloud storage backup (AWS S3, Google Cloud)

\- Create organized folder structure by visual content categories

\- Store CV analysis results in searchable database

\---

\#\# \*\*Phase 2: Image Optimization for Print\*\*

\#\#\# \*\*2.1 Quality Assessment\*\*

\- \*\*Minimum resolution check:\*\* 300 DPI at intended print size

\- \*\*Sharpness analysis:\*\* Reject blurry or low-quality images

\- \*\*Color profile validation:\*\* Ensure sRGB/Adobe RGB compatibility

\- \*\*Composition scoring:\*\* Use CV analysis to prioritize well-composed images

\#\#\# \*\*2.2 Image Enhancement Pipeline\*\*

\`\`\`python

\# Automated enhancement steps:

1\. AI upscaling (Topaz Gigapixel AI, Real-ESRGAN)

2\. Color correction and saturation optimization

3\. Sharpening for print clarity

4\. Noise reduction

5\. Contrast and exposure adjustment

6\. Scene-specific enhancement (e.g., sunset color boosting)

\`\`\`

\#\#\# \*\*2.3 Print Format Preparation\*\*

\- \*\*File formats:\*\* Convert to TIFF (lossless) or high-quality PNG

\- \*\*Color space:\*\* Convert to CMYK for print accuracy

\- \*\*Resolution:\*\* Ensure 300 DPI minimum for all print sizes

\- \*\*Aspect ratio optimization:\*\* Create multiple crops for different print formats

\#\#\# \*\*2.4 Size Variants Generation\*\*

Create optimized versions for common print sizes:

\- 8x10, 11x14, 16x20, 24x36 inches

\- Square formats for Instagram-style prints

\- Panoramic formats for landscape images

\---

\#\# \*\*Phase 3: Print-on-Demand Integration\*\*

\#\#\# \*\*3.1 Platform Selection & Setup\*\*

\- \*\*Primary:\*\* Printify (better Etsy integration)

\- \*\*Secondary:\*\* Printful (higher quality options)

\- \*\*API Authentication:\*\* Secure token management

\#\#\# \*\*3.2 Product Template Creation\*\*

\`\`\`python

\# Product configurations:

\- Canvas prints (multiple sizes)

\- Framed prints (various frame styles)

\- Metal prints

\- Acrylic prints

\- Photo papers (matte, glossy)

\`\`\`

\#\#\# \*\*3.3 Automated Product Creation\*\*

\- Upload optimized images via API

\- Apply predefined templates and specifications

\- Set competitive pricing based on market research

\- Configure shipping options and fulfillment settings

\- \*\*Smart categorization:\*\* Use CV analysis for product placement

\#\#\# \*\*3.4 Quality Control Automation\*\*

\- Mockup generation and review

\- Print preview validation

\- Color accuracy checks

\---

\#\# \*\*Phase 4: Etsy Shop Population\*\*

\#\#\# \*\*4.1 Etsy API Integration\*\*

\- \*\*Authentication:\*\* OAuth 2.0 setup

\- \*\*Shop management:\*\* Automated listing creation

\- \*\*Inventory sync:\*\* Real-time stock updates

\#\#\# \*\*4.2 SEO-Optimized Listing Creation\*\*

\`\`\`python

\# Automated content generation using CV analysis:

\- Titles: "\[Scene Type\] \[Location\] Print | \[Mood\] Photography | Wall Art"

\- Tags: Combine visual tags \+ Instagram hashtags \+ SEO research

\- Descriptions: Template-based with visual content descriptions

\- Categories: Automatic categorization based on scene analysis

\`\`\`

\#\#\# \*\*4.3 Pricing Strategy Automation\*\*

\- Market research integration (competitor analysis)

\- Dynamic pricing based on image popularity and composition scores

\- Bulk pricing for multiple sizes

\- \*\*Visual appeal pricing:\*\* Higher prices for high-scoring compositions

\#\#\# \*\*4.4 Description Generation\*\*

Use NLP tools combined with CV analysis for compelling descriptions:

\`\`\`python

\# Enhanced description template:

"Capture the \[mood\] beauty of this \[scene\_type\] featuring \[main\_objects\]. 

The \[lighting\_condition\] creates a \[emotional\_descriptor\] atmosphere with 

\[color\_description\]. Perfect for \[room\_suggestions\] based on color palette."

\`\`\`

\---

\#\# \*\*Phase 5: Content Search & Discovery System\*\*

\#\#\# \*\*5.1 Search Interface Implementation\*\*

\`\`\`python

\# Natural language search capabilities:

\- Text-based queries: "sunset over water", "misty mountains"

\- Visual similarity search: Upload reference image to find similar content

\- Advanced filters: Color palette, mood, composition quality

\- Combination searches: "golden hour" \+ "high composition score"

\`\`\`

\#\#\# \*\*5.2 Search Algorithm Components\*\*

\- \*\*Semantic search:\*\* Convert queries to visual concepts

\- \*\*Vector similarity:\*\* Find images with similar visual embeddings

\- \*\*Multi-modal matching:\*\* Combine text descriptions with visual features

\- \*\*Relevance ranking:\*\* Score results by visual quality and engagement

\#\#\# \*\*5.3 Search Result Processing\*\*

\- Batch selection for processing

\- Quality filtering integration

\- Automatic enhancement pipeline triggering

\- Print suitability assessment

\---

\#\# \*\*Phase 6: Workflow Automation & Orchestration\*\*

\#\#\# \*\*5.1 MCP Server Setup\*\*

\`\`\`python

\# Core automation components:

\- Instagram scraper module

\- Computer vision analysis pipeline

\- Image processing pipeline

\- Search and discovery engine

\- API integration handlers

\- Error handling and retry logic

\- Logging and monitoring systems

\`\`\`

\#\#\# \*\*5.2 On-Demand Processing\*\*

\- \*\*Manual trigger system:\*\* User-initiated processing batches

\- \*\*Search-driven workflow:\*\* Process images based on search results

\- \*\*Real-time sync:\*\* Inventory and pricing updates

\- \*\*Batch operations:\*\* Bulk processing of selected images

\#\#\# \*\*5.3 Error Handling & Recovery\*\*

\- API rate limit management

\- Failed upload retry mechanisms

\- CV analysis failure fallbacks

\- Quality control checkpoints

\- Notification system for manual intervention

\#\#\# \*\*5.4 Monitoring & Analytics\*\*

\- Processing pipeline health checks

\- CV analysis accuracy metrics

\- Search query performance

\- Sales performance tracking

\- Image popularity correlation

\- ROI analysis per image

\---

\#\# \*\*Phase 7: Advanced Features & Optimization\*\*

\#\#\# \*\*7.1 AI-Powered Enhancements\*\*

\- \*\*Smart cropping:\*\* AI-driven composition optimization using CV analysis

\- \*\*Style transfer:\*\* Artistic filter applications

\- \*\*Seasonal variants:\*\* Automatic color grading for seasons

\- \*\*Trend analysis:\*\* Popular visual style identification

\#\#\# \*\*7.2 Customer Customization\*\*

\- Size selection automation

\- Frame style options based on image mood

\- Custom text overlay capabilities

\- Bulk order discounts

\#\#\# \*\*7.3 Marketing Automation\*\*

\- Social media cross-posting with CV-generated descriptions

\- Email marketing integration

\- SEO content optimization using visual tags

\- Collection creation based on visual themes

\---

\#\# \*\*Phase 8: Legal & Compliance\*\*

\#\#\# \*\*8.1 Instagram Terms Compliance\*\*

\- Respect rate limits and usage guidelines

\- Ensure content ownership rights

\- Implement proper attribution if required

\#\#\# \*\*8.2 Copyright & Licensing\*\*

\- Verify image ownership before listing

\- Include proper copyright notices

\- Consider Creative Commons licensing options

\#\#\# \*\*8.3 Business Compliance\*\*

\- Tax calculation and reporting

\- International shipping regulations

\- Print quality guarantees and return policies

\---

\#\# \*\*Technical Implementation Stack\*\*

\#\#\# \*\*Core Technologies:\*\*

\- \*\*Backend:\*\* Python/Node.js

\- \*\*Computer Vision:\*\* 

  \- TensorFlow/PyTorch for custom models

  \- OpenAI CLIP for semantic understanding

  \- Google Vision API or AWS Rekognition for object detection

  \- Custom scene classification models

\- \*\*Image Processing:\*\* OpenCV, Pillow, ImageMagick

\- \*\*AI Enhancement:\*\* Topaz Labs API, Real-ESRGAN

\- \*\*Search Engine:\*\* Elasticsearch with vector search capabilities

\- \*\*APIs:\*\* Instagram Graph API, Printify API, Etsy API

\- \*\*Database:\*\* PostgreSQL for metadata \+ Vector database (Pinecone/Weaviate)

\- \*\*Cloud Storage:\*\* AWS S3 or Google Cloud Storage

\#\#\# \*\*Computer Vision Pipeline:\*\*

\`\`\`python

\# CV processing workflow:

1\. Image ingestion and preprocessing

2\. Multi-model analysis (objects, scenes, composition)

3\. Feature extraction and embedding generation

4\. Semantic tagging and categorization

5\. Quality and printability assessment

6\. Search index population

\`\`\`

\#\#\# \*\*Monitoring & Deployment:\*\*

\- \*\*Containerization:\*\* Docker for consistent deployment

\- \*\*Monitoring:\*\* Prometheus \+ Grafana

\- \*\*Logging:\*\* ELK Stack (Elasticsearch, Logstash, Kibana)

\- \*\*CI/CD:\*\* GitHub Actions or GitLab CI

\---

\#\# \*\*Success Metrics & KPIs\*\*

\#\#\# \*\*Operational Metrics:\*\*

\- Images processed per batch

\- CV analysis accuracy rates

\- Search relevance scores

\- Processing success rate

\- API uptime and response times

\#\#\# \*\*Business Metrics:\*\*

\- Conversion rate (views to sales)

\- Search-to-purchase correlation

\- Average order value

\- Customer satisfaction scores

\- Revenue per image category

\---

\#\# \*\*Deployment Checklist\*\*

1\. ✅ Set up all API credentials and authentication

2\. ✅ Configure computer vision models and pipelines

3\. ✅ Implement search and discovery system

4\. ✅ Configure cloud storage and backup systems

5\. ✅ Implement image processing pipeline

6\. ✅ Test print-on-demand integration

7\. ✅ Validate Etsy listing automation

8\. ✅ Set up monitoring and alerting

9\. ✅ Configure error handling and recovery

10\. ✅ Implement legal compliance measures

11\. ✅ Test end-to-end workflow with search functionality

12\. ✅ Launch with limited product set for validation

This comprehensive guide now includes intelligent content-based search capabilities and focuses on on-demand processing rather than automated scheduling, providing all necessary components for your coding assistant to implement a fully automated Instagram-to-Etsy print shop pipeline with advanced visual search functionality.
````

## File: repo-structure.md
````markdown
# Repository Structure for Instagram to Etsy Print Shop

This document outlines the directory and file structure for the Instagram to Etsy Print Shop automation project.

## Key Directories and Files

(To be populated as the project develops)

- **`/`** (Root directory)
  - `README.md`: Project overview, setup, and usage instructions.
  - `repo-structure.md`: This file - outlines the repository structure.
  - `Instagram-to-Etsy-Print-Shop .md`: Comprehensive guide and project plan.
  - `.clinerules/`: Contains rules and process documents for Cascade.
  - `requirements.txt` (or similar): Project dependencies (to be created).
  - `src/` (or similar): Source code for the automation pipeline (to be created).
    - `phase1_acquisition/`: Code related to Instagram image acquisition and content analysis.
    - `phase2_processing/`: Code related to image processing and print optimization.
    - `phase3_pod_integration/`: Code related to print-on-demand service integration.
    - `phase4_etsy_management/`: Code related to Etsy shop management and listing automation.
    - `phase5_search_discovery/`: Code related to the search and discovery system.
    - `utils/`: Utility scripts and common modules.
  - `data/`: For storing temporary data, logs, or outputs (if not using cloud storage exclusively).
  - `notebooks/`: Jupyter notebooks for experimentation and analysis (optional).
  - `tests/`: Unit and integration tests.
````

## File: requirements.txt
````
requests
Pillow
google-cloud-storage
python-dotenv
apify-client>=2.0.0
````

## File: README.md
````markdown
# Instagram to Etsy Print Shop Automation (auto_etsy)

## Project Overview

This project aims to create a fully automated pipeline to transform landscape photography from an Instagram account into a profitable Etsy print shop. It leverages print-on-demand services and incorporates intelligent content-based image discovery and search capabilities.

The core goal is to automate the process from image sourcing on Instagram, through content analysis and print optimization, to listing products on Etsy and managing the shop.

### MVP: Application for Personal Use (Initial Focus)

This project will initially be developed as an **MVP (Minimum Viable Product)** tailored for the primary user's personal use. While designed as a reusable application for a repeatable process, the immediate focus is on creating a functional tool for a single-user workflow. Future iterations may expand this to a more general, multi-user application.

The core workflow for this MVP will be:

* **Instagram Image Retrieval:** This is a two-stage process. First, the application will use a scraper (e.g., via Apify) to fetch recent posts from the user's specified Instagram profile(s). Second, for each scraped image, a Computer Vision (CV) model within our application will analyze its visual content. This CV analysis will filter the images based on a descriptive criterion provided by the user (e.g., to find all images visually containing a "sunset" or representing "New York City streets at dusk"), even if the original posts lack hashtags or detailed text descriptions.
* **Image Optimization:** Programmatically enhance and prepare the retrieved images to ensure they are print-worthy.
* **Cloud Storage:** Save the optimized images to the user's designated Google Cloud Storage bucket.
* **Print-on-Demand Integration:** Integrate with Printify to define product templates.
* **Etsy Listing Automation:** Automatically create and post these product templates as new listings on the user's Etsy shop, based on specified print types.
* **Notification:** Inform the user once new listings have been successfully posted.

The application will require the user to provide their credentials for Instagram (for the scraper), Google Cloud Storage, Printify, and Etsy.

## Comprehensive Guide

The detailed plan, technical specifications, and full project scope are documented in the [Comprehensive Guide: Instagram to Etsy Print Shop](./Instagram-to-Etsy-Print-Shop%20.md).

## Repository Structure

The organization of this repository is detailed in [repo-structure.md](./repo-structure.md).

## High-Level Project Phases

The project will be implemented in the following key phases:

1. **Phase 1: Instagram Image Acquisition & Content Analysis**
    * Authentication & Access (Instagram API/Scraping)
    * Image Discovery & Filtering (Criteria: aspect ratio, hashtags, quality, engagement, date)
    * Computer Vision Content Analysis (Object/scene detection, color analysis, composition, etc.)
2. **Phase 2: Image Processing & Print Optimization**
    * Image enhancement, resizing, color correction for print
    * Print quality assessment
3. **Phase 3: Print-on-Demand (PoD) Integration**
    * API integration with selected PoD services
    * Product creation and variant mapping
4. **Phase 4: Etsy Shop Management & Listing Automation**
    * Automated creation of Etsy listings
    * Dynamic population of metadata (titles, descriptions, tags) based on CV analysis
    * Management of pricing and shipping profiles
5. **Phase 5: Search & Discovery System**
    * Building a search index with CV-extracted features
    * Developing a user interface for content-based image search within the print shop
6. **Phase 6: Technical Architecture & Stack Implementation**
    * Setup of cloud storage (e.g., AWS S3, Google Cloud Storage)
    * Development of the Computer Vision processing pipeline
    * Configuration of monitoring (e.g., Prometheus, Grafana) and logging (e.g., ELK Stack)
    * Implementation of CI/CD pipelines (e.g., GitHub Actions)
7. **Phase 7: Success Metrics & KPIs**
    * Defining and tracking operational metrics (e.g., processing speed, CV accuracy)
    * Defining and tracking business metrics (e.g., conversion rates, revenue)
8. **Phase 8: Deployment**
    * Execution of the deployment checklist
    * Initial launch with a limited product set for validation and iteration

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Instagram account (for image acquisition)
- Printify account with API key
- Etsy shop connected to your Printify account
- (Optional) Google Cloud Storage account for image storage

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/auto_etsy.git
   cd auto_etsy
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv myenv
   # On Windows
   myenv\Scripts\activate
   # On macOS/Linux
   source myenv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your credentials:
   ```
   # Instagram credentials
   INSTAGRAM_USERNAME=your_instagram_username
   INSTAGRAM_PASSWORD=your_instagram_password
   
   # Printify API credentials
   PRINTIFY_API_TOKEN=your_printify_api_token
   PRINTIFY_SHOP_ID=your_printify_shop_id
   
   # Google Cloud Storage (optional)
   USE_GCS=False
   GCS_BUCKET_NAME=your_gcs_bucket_name
   GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json
   ```

### Usage

The application can be run using the `run.py` script at the project root:

```bash
# Run the full workflow (all phases)
python run.py --workflow full --instagram-user yourusername --limit 10

# Run only the image acquisition phase
python run.py --workflow acquisition --instagram-user yourusername --limit 5

# Run only the image processing phase (using existing images)
python run.py --workflow processing --input-dir data/raw --output-dir data/processed

# Run only the Print-on-Demand integration phase
python run.py --workflow pod

# Run with debug logging enabled
python run.py --workflow full --debug

# Get help on available options
python run.py --help
```

### Workflow Phases

1. **Acquisition**: Scrapes images from Instagram and filters them based on criteria
2. **Processing**: Optimizes images for printing (resizing, enhancing, etc.)
3. **POD Integration**: Uploads processed images to Printify and creates products
4. **Etsy Management**: Manages Etsy listings via Printify integration
5. **Discovery**: (Future) Implements search capabilities for finding optimal images

### Directory Structure

- `data/`: Stores images and metadata
  - `raw/`: Raw images downloaded from Instagram
  - `processed/`: Processed and optimized images
  - `metadata/`: Metadata about images and workflow runs
- `src/`: Source code
  - `phase1_acquisition/`: Instagram scraping and image filtering
  - `phase2_processing/`: Image processing and optimization
  - `phase3_pod_integration/`: Printify API integration
  - `phase4_etsy_management/`: Etsy shop management
  - `phase5_search_discovery/`: Search and discovery features
  - `utils/`: Utility functions and helpers
- `tests/`: Unit and integration tests
- `notebooks/`: Jupyter notebooks for exploration and analysis

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
````
