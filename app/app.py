from flask import Flask, render_template, send_file, send_from_directory
from config import config
import os
import re
from urllib.parse import unquote

app = Flask(__name__)

def find_matching_folder(root, item_name):
    # Iterate over all directories
    for item in os.listdir(root):

        # Skip anything that isn't a directory
        if (not os.path.isdir(root + item)):
            continue

        if item.lower() == item_name.lower():
            return item

    # No match found
    return None

def find_matching_file(root, item_name):

    # Convert to lowercase
    item_name = item_name.lower()

    # Iterate over all files and directories in the current directory
    for item in os.listdir(root):

        # Skip anything that isn't a file
        if not os.path.isfile(root + item):
            continue

        # Skip anything that isn't HTML
        if not item.endswith(".html"):
            continue

        # Drop the ".html" extension when matching the name
        sanitized_name = ''.join(c for c in item[:-4] if c.isalnum() or c == " ").lower()

        if sanitized_name == item_name:
            return item

    # No match found
    return None

def page_contents(file_path):
    contents = ''
    file_path.strip("/")

    with open("templates/" + file_path, 'r', encoding='utf-8') as f:
        contents = f.read()

    return contents

@app.route('/<path:url_path>')
def route_url(url_path):
    url_path = url_path.strip("/")

    # Split the URL path into its component folders and files
    path_components = url_path.replace('-', " ").split('/')

    file_path = ''

    # Build the file path by searching for each component folder and appending to file_path along the way
    for component in path_components[:-1]:
        matching_path = find_matching_folder("templates/" + file_path, component)
        if matching_path == None:
            return render_template("__404.html")

        file_path += matching_path + "/"

    # Check for direct file match
    if os.path.isfile("templates/" + file_path + url_path.split('/')[-1]):
        return send_from_directory("templates", file_path + url_path.split('/')[-1])

    # Finally, find the file requested by the URL
    matching_file = find_matching_file("templates/" + file_path, path_components[-1])

    if matching_file == None:
        return render_template("__404.html",
                               title = "404",
                               WebsiteName = config["WebsiteName"])

    file_path += matching_file

    # Set the filename without the extension as the page title
    page_title = '.'.join(matching_file.split('.')[:-1])

    return render_template("__page.html",
                           page_content = page_contents(file_path),
                           title = page_title,
                           WebsiteName = config["WebsiteName"])

@app.route('/')
def frontpage():
    return render_template("__page.html",
                           page_content = page_contents("Frontpage.html"),
                           title = "Frontpage",
                           WebsiteName = config["WebsiteName"])

if __name__ == "__main__":
    app.run(debug=True)
