## Description: Generate HTML body from a Markdown file
## Usage: python md2html.py /path/to/input.md /path/to/output.html

import sys
import os.path
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

def md2html(input_file, output_file):
    # Check for existence of input file
    if not os.path.isfile(input_file):
        print(f"Error: {input_file} does not exist.")
        sys.exit(1)

    md = open(input_file, "r").read()
    html = markdown.markdown(md, extensions=['extra', 'nl2br', 'wikilinks', CodeHiliteExtension(guess_lang=False)])
    with open(output_file, "w") as f:
        f.write(html)

if __name__ == "__main__":
    # Check if two arguments provided
    if len(sys.argv) != 3:
        print("Error: Provide input and output file names as arguments.")
        sys.exit(1)

    md2html(sys.argv[1], sys.argv[2])
