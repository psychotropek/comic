from PIL import Image as PIL
import re, argparse
from typing import List
import string
import os
from os import system, name, path

# Set the default save path variable here
DEFAULT_SAVE_PATH = f"{path.expanduser('~')}/Downloads/"

# Convert PIL-modules default Image-class to a more readable format
# (To avoid using Image.Image everywhere!)
class Image:
    PIL.Image

def walk_through_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            list_of_files = []
            #if there's a zip, don't execute this
            for file in files:
                [base,ext] = os.path.splitext(file)
                if ext == '.webp':
                    image: Image = PIL.open(path)
                    image.save(base + '.jpg')
                    list_of_files.append(os.path.join(root,file))   
                elif ext in ['.jpg','.png','.gif']:
                    #TODO: do we need
                    list_of_files.append(os.path.join(root,file))   
            zip_images(list_of_files)
    return 

def zip_images(file_paths: List[str])
    file_name: str = input("Enter file name (*.pdf): ").strip()

    if file_name == "":
        # If no file name is given, generate a random one
        # TODO: get folder name
        file_name = "blargle"
        print(f"-- Generated random file name: {file_name}.pdf --")

    if not file_name[-4:] == ".pdf":
        # If file name is lacking the pdf extension, add it
        file_name += ".pdf"

    if input("Use default save path? (y/n): ") in ["y", "Y", ""]:
        file_name = save_path + file_name

    print(f'Saving {os.path.basename(file_name)}')
    try:
        images[0].save(file_name, save_all=True, append_images=images[1:])
        print(f"\nImages saved to {file_name}\n")
    except OSError:
        print("Error: could not save images as pdf.")



def print_start_message():
    print("\n"+56*"=")
    print("To smush images together into a pdf for ereading.")
    print(56*"="+"\n")


def main():
    print_start_message()

    parser = argparse.ArgumentParser()
    parser.add_argument("comic_path", help="the chapter folder path")
    args = parser.parse_args()

    walk_through_folder(args.comic_path)

# If this file is the main program (if we're executing this instead of loading it)
if __name__ == "__main__":
    main()