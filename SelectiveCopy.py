print("Jay Surya \n1AY24AI048 \nAIML 'M' ")
import os
import shutil

def selective_copy(src_folder, dest_folder, extension):
    extension = extension.lower().strip(".")
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    for foldername, subfolders, filenames in os.walk(src_folder):
        for filename in filenames:
            if filename.lower().endswith("." + extension):
                src_path = os.path.join(foldername, filename)
                dest_path = os.path.join(dest_folder, filename)
                if not os.path.exists(dest_path):
                    shutil.copy(src_path, dest_path)
                    print(f"Copied: {src_path} → {dest_path}")
                else:
                    print(f"Skipped (already exists): {dest_path}")

src = input("Enter source folder path: ").strip()
dest = input("Enter destination folder path: ").strip()
ext = input("Enter file extension to search for (e.g., pdf, jpg): ").strip()

if os.path.isdir(src):
    selective_copy(src, dest, ext)
else:
    print("Invalid source folder.")
