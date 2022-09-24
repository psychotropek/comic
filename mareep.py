
from PIL import Image as PIL
import re, argparse
from typing import List
import string
import os
from os import system, name, path

# Convert PIL-modules default Image-class to a more readable format
# (To avoid using Image.Image everywhere!)
class Image:
    PIL.Image

# This is recursive TODO make function to get all chapter folders and process them one by one
def get_file_paths_from_folder(folder_path):
    list_of_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            [base,ext] = os.path.splitext(file)
            if ext in ['.jpg','.png','.gif']:
                list_of_files.append(os.path.join(root,file))
    return list_of_files

def convert_image(image: Image, format: str = "RGB") -> Image:
    return image.convert(format)

def create_image_list(file_paths: List[str]) -> List[Image]:
    images: List[Image] = []
    for path in file_paths:
        #print(f'Converting {os.path.basename(path)}')
        image: Image = PIL.open(path)
        image = convert_image(image)
        images.append(image)
    return images

def convert_images_to_pdf(images: List[Image]) -> None:
    file_name = 'comic.pdf'
    print(f'Saving {os.path.basename(file_name)}')
    try:
        images[0].save(file_name, save_all=True, append_images=images[1:])
        print(f"\nImages saved to {file_name}\n")
    except OSError:
        print("Error: could not save images as pdf.")

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("comic_path", help="the chapter folder path")
    args = parser.parse_args()

    comic_file_paths: List[str] = get_file_paths_from_folder(args.comic_path) 
    images: List[Image] = create_image_list(comic_file_paths)
    convert_images_to_pdf(images)

# If this file is the main program (if we're executing this instead of loading it)
if __name__ == "__main__":
    main()
