from dotenv import dotenv_values
import requests
import json
import os
import random
import time
import shutil
import uuid


# Load the environment variables from .env file
env_vars = dotenv_values('/home/kaowarstail/Documents/finetech/finetech_curve_gen/.env')

# Get the value of STABLE_DIFFUSION_API_KEY
api_key = env_vars.get('STABLE_DIFFUSION_API_KEY')

url = "https://stablediffusionapi.com/api/v5/outpaint"


folder_path = "/home/kaowarstail/Documents/finetech/finetech_curve_gen/screenshot"  # Replace with the actual folder path

# Get a list of all image files in the folder
image_files = [file for file in os.listdir(folder_path) if file.endswith((".png", ".jpg", ".jpeg"))]

# Select a random image file
random_image = random.choice(image_files)
# Construct the URL to the raw image file on GitHub
image_url = f"https://raw.githubusercontent.com/Kaowarstail/finetech_curve_gen/main/screenshot/{random_image}"


payload = json.dumps({
    "key":api_key,
    "seed":12345,
    "width":1024,
    "height":1024,
    "prompt":"the prolongment of the graph's curve in green when the graph is going up and red when the graph is going down",
    "image":image_url,
    "negative_prompt":"unrealistic, boring background, bad, low quality, black background",
    "height_translation_per_step": 64,
    "width_translation_per_step":64,
    "num_inference_steps": 15,
    "as_video":"no",
    "num_interpolation_steps": 32,
    "walk_type":["left", "left", "left", "right", "right", "right", "right"],
    "webhook": None,
    "track_id": None 
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# Parse the response
response_json = response.json()

print(response_json)

# Get the fetch URL
fetch_url = response_json['fetch_result']

# Wait for the image to be ready (use the estimated time provided by the API)
time.sleep(response_json['eta'])

payload2 = json.dumps({
    "key":api_key,
})


# Fetch the image
response_img = requests.request("POST", fetch_url, headers=headers, data=payload2)

# print(response_img.status_code)

# Check if the image was fetched successfully
if response_img.status_code == 200:

    response_img_json = response_img.json()

    # Get the image URL
    image_url = response_img_json['output'][0]

    # Fetch the image
    response = requests.get(image_url, stream=True)

    # Check if the image was fetched successfully
    if response.status_code == 200:
        # Generate a unique file name
        image_file_name = f"{uuid.uuid4()}.png"

        # Open the image file in write mode and download the image
        with open(f'prediction/{image_file_name}', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    else:
        print('Error fetching the image:', response.status_code)
else:
    print('Error:', response_img.status_code)