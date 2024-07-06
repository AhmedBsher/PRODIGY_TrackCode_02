import torch
from diffusers import StableDiffusionPipeline
import os
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog

# Load the Stable Diffusion pipeline
pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipeline = pipeline.to("cuda")  # Use GPU for faster generation

# Create the GUI interface
root = tk.Tk()
root.withdraw()  # Hide the root window

# Prompt the user for input
text_prompt = simpledialog.askstring("Input", "Enter the text prompt for image generation:")

# Check if the user provided a text prompt
if text_prompt:
    # Generate the image
    with torch.no_grad():
        images = pipeline([text_prompt], guidance_scale=7.5)
    
    # Save the image in a folder with a unique name
    output_folder = "generated_images"
    os.makedirs(output_folder, exist_ok=True)
    
    # Generate a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_filename = f"generated_image_{timestamp}.png"
    image_path = os.path.join(output_folder, image_filename)
    
    # Get the first generated image
    image = images.images[0]  
    image.save(image_path)
    image.show()
    
    print(f"Image saved at {image_path}")
else:
    print("No text prompt provided. Exiting.")
