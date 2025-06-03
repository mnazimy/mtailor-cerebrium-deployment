"""
Image Classification API for M-Tailor
Deploys Vision Transformer (ViT) via Cerebrium
Author: [Your Name]
Date: [Current Date]
"""

from cerebrium import model
from transformers import pipeline
from PIL import Image
import io
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model once at startup (optimizes cold starts)
logger.info("Loading ViT-Base model...")
classifier = pipeline(
    "image-classification", 
    model="google/vit-base-patch16-224"
)
logger.info("Model loaded successfully!")

@model
def predict(file: bytes):
    """Classify images from binary data.
    
    Args:
        file: Bytes of uploaded image (JPEG/PNG)
    
    Returns:
        List of top 5 predicted labels with confidence
    """
    try:
        # Convert bytes to PIL Image
        image = Image.open(io.BytesIO(file))
        logger.info(f"Image received: {image.size[0]}x{image.size[1]}")
        
        # Get predictions
        results = classifier(image)
        
        # Return top 5 predictions
        return results[:5]
        
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        return {"error": "Invalid image file. Use JPEG/PNG under 5MB"}
