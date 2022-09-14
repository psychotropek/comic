from PIL import Image as PIL
from zipfile import ZipFile
import re
import argparse
from typing import List
import string
import os
from os import system, name, path


def create_cbz_files(folder_path):

    for dir_path, dir_names, file_names in os.walk(folder_path):
        files_to_zip = []
        for file in file_names:
            [base, ext] = os.path.splitext(file)
            image_file_path = os.path.join(dir_path, file)
            if ext == '.webp':
                image = PIL.open(image_file_path)
                image.save(os.path.join(dir_path, base + '.jpg'))
                if os.path.join(dir_path, base + '.jpg') not in files_to_zip:
                    files_to_zip.append(os.path.join(dir_path, base + '.jpg'))
            elif ext in ['.jpg', '.png', '.gif']:
                if image_file_path not in files_to_zip:
                    files_to_zip.append(image_file_path)
        if len(files_to_zip) > 0:
            zip_images(files_to_zip, dir_path)


def zip_images(file_paths: List[str], dir_path: string):

    [test_head, test_tail] = os.path.split(dir_path)
    [_, file_prefix] = os.path.split(test_head)
    cbzfile_name = test_head + '/' + file_prefix + ' - ' + test_tail + '.cbz'
    print('Zipping ' + cbzfile_name)
    with ZipFile(cbzfile_name, 'w') as zipfile:
        for name in file_paths:
            [head, tail] = os.path.split(name)
            zipfile.write(name, tail)
    zipfile.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'comic_path',
        help='the base comic folder path, should have chapter subfolders')
    args = parser.parse_args()
    create_cbz_files(args.comic_path)


# If this file is the main program
# (if we're executing this instead of loading it)
if __name__ == '__main__':
    main()
