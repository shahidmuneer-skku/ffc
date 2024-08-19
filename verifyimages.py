from PIL import Image
import os

def validate_and_delete_images(directory):
    total = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')):
                try:
                    img_path = os.path.join(root, file)
                    img = Image.open(img_path)
                    img.verify()  # Verify that it is, indeed, an image
                except (IOError, SyntaxError) as e:
                    total=total+1
                    print(f'Deleting bad file: {img_path}')
                    os.remove(img_path)  # Delete the corrupted file
    print(f"Deleted total files {total}")
# Run the function to validate and delete corrupted files
validate_and_delete_images('/home/shahid/genimages/genimages/ADM/imagenet_ai_0508_adm/train/nature/')
