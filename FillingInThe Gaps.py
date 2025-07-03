print("Jay Surya\n1AY24AI048 \nAIML 'M' ")
import os
import re

def fill_gaps(folder, prefix, extension):
    files = os.listdir(folder)
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)\.{re.escape(extension)}$")

    matched_files = []
    for file in files:
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            matched_files.append((number, file))

    matched_files.sort()

    expected_number = 1
    for actual_number, filename in matched_files:
        if actual_number != expected_number:
            new_name = f"{prefix}{str(expected_number).zfill(3)}.{extension}"
            print(f"Renaming {filename} → {new_name}")
            os.rename(
                os.path.join(folder, filename),
                os.path.join(folder, new_name)
            )
        expected_number += 1

# Example usage
folder = input("Enter folder path: ").strip()
prefix = input("Enter file prefix (e.g., spam): ").strip()
extension = input("Enter file extension (without dot, e.g., txt): ").strip()

if os.path.isdir(folder):
    fill_gaps(folder, prefix, extension)
else:
    print("Invalid folder path.")


                                                    

import os
import re

def insert_gap(folder, prefix, extension, position):
    files = os.listdir(folder)
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)\.{re.escape(extension)}$")

    matched_files = []
    for file in files:
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            matched_files.append((number, file))

    matched_files.sort(reverse=True)  

    for number, filename in matched_files:
        if number >= position:
            new_number = number + 1
            new_name = f"{prefix}{str(new_number).zfill(3)}.{extension}"
            print(f"Renaming {filename} → {new_name}")
            os.rename(
                os.path.join(folder, filename),
                os.path.join(folder, new_name)
            )

folder = input("\nEnter folder path: ").strip()
prefix = input("Enter file prefix (e.g., spam): ").strip()
extension = input("Enter file extension (without dot, e.g., txt): ").strip()
position = int(input("Enter position number to insert gap (e.g., 2): ").strip())

if os.path.isdir(folder):
    insert_gap(folder, prefix, extension, position)
else:
    print("Invalid folder path.")

