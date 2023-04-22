import os
import shutil
import time
from md2html import md2html
from config import config

print("Generating website...")

# Iterate through all files and folders in Pages folder
for root, dirs, files in os.walk(config["PagesPath"]):

    # Determine the corresponding Flask app directory
    current_flask_dir = 'templates/'
    if os.path.relpath(root, config["PagesPath"]) != '.':
        current_flask_dir += os.path.relpath(root, config["PagesPath"])

    if not current_flask_dir.endswith('/'):
        current_flask_dir += "/"

    # Create directories in the corresponding Flask folder if they don't exist
    for directory in dirs:
        local_dir = current_flask_dir + directory
        if not os.path.isdir(local_dir):
            print(f"Creating folder {local_dir}...")
            os.mkdir(local_dir)

    for filename in files:
        if filename.endswith(".md"): # Markdown file, convert to HTML
            html_file = current_flask_dir + filename[:-2] + "html"

            print(f"Generating {html_file} from Markdown...")
            md2html(root + "/" + filename, html_file)

        else: # If file isn't Markdown, directly copy
            local_file = current_flask_dir + filename
            print(f"Copying {filename} to {current_flask_dir}")
            shutil.copy(root + "/" + filename, local_file)

print("Website generation completed.")
