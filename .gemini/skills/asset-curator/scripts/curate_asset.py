import sys
import os
import base64
from io import BytesIO
from PIL import Image
from google import genai
from google.genai.types import GenerateContentConfig, Modality

def curate_asset(prompt, output_filename):
    client = genai.Client(
        vertexai=True,
        project=os.environ.get('GOOGLE_CLOUD_PROJECT'),
        location=os.environ.get('GOOGLE_CLOUD_LOCATION')
    )
    
    print(f"Curating asset with prompt: '{prompt}'...")
    
    # Using the specified model for image generation
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[prompt],
        config=GenerateContentConfig(response_modalities=[Modality.IMAGE]),
    )
    
    # Handle the response parts
    for i, part in enumerate(response.candidates[0].content.parts):
        if part.inline_data is not None:
            image_data = part.inline_data.data
            image = Image.open(BytesIO(image_data))
            
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_filename), exist_ok=True)
            
            # Save the image
            image.save(output_filename)
            print(f"Successfully saved curated asset to: {output_filename}")
            return True
            
    print("Error: No image was generated in the response.")
    return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 curate_asset.py <prompt> <output_filename>")
        sys.exit(1)
    
    prompt = sys.argv[1]
    output_filename = sys.argv[2]
    
    if curate_asset(prompt, output_filename):
        # Print only the success path for the agent to easily parse
        print(f"ASSET_PATH: {output_filename}")
    else:
        sys.exit(1)
