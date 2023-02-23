from PIL import Image
import os 

source_folder = "./images"
destination_folder = "/opt/icons/"


if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)


for file in os.listdir(source_folder):
    if file.endswith("dp"):
        # Open the image
        img = Image.open(f"{source_folder}/{file}")
        
        # Rotate the image
        img = img.rotate(90)
        
        # Resize the image
        img = img.resize((128, 128))
        
        # Save the image
        img = img.convert("RGB")  # convert to RGB mode
        img.save(f"{destination_folder}/{file.split('.')[0]}.jpeg", "JPEG")
        

