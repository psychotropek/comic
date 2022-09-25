
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

def convert_images_to_pdf(images: List[Image], comic_path: str) -> None:
    print(comic_path)
    print(f'Saving {os.path.basename(comic_path)}')
    if images:
        try:
            images[0].save(comic_path, save_all=True, append_images=images[1:])
            print(f"\nImages saved to {comic_path}\n")
        except OSError:
            print("Error: could not save images as pdf.")

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("comic_path", help="the base folder path")
    args = parser.parse_args()

    for root, dirs, files in os.walk(args.comic_path):
        #if files not empty

        if files:
            comic_file_paths: List[str] = get_file_paths_from_folder(root) 
            images: List[Image] = create_image_list(comic_file_paths)
            convert_images_to_pdf(images, 'test.pdf')

# If this file is the main program (if we're executing this instead of loading it)
if __name__ == "__main__":
    main()
