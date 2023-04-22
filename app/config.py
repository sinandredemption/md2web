import os.path
import sys

config_file = "config"
config = {}

# Check if the configuration file exists
if not os.path.isfile(config_file):
    print(f"Error: {config_file} does not exist.")
    sys.exit(1)

# Open the configuration file
with open(config_file, 'r') as f:
    for line in f:
        if line.startswith('#'): # Ignore comments
            continue
        if line.find('=') == -1: # Ignore lines that are not in key=value format
            continue

        key, value = line.strip().split('=')
        config[key] = value

# Check if PagesPath and WebsiteName are set and valid
if "PagesPath" not in config or not os.path.isdir(config["PagesPath"]):
    print("Error: PagesPath is not set or is invalid.")
    sys.exit(1)

if "WebsiteName" not in config or not config["WebsiteName"].strip():
    print("Error: WebsiteName is not set or is invalid.")
    sys.exit(1)

