#!/bin/bash

## Description: Synchronise every modification to the pages folder with the Flask App

APP_DIR="templates/"
PAGES_DIR=$(cat "config" | grep 'PagesPath')
PAGES_DIR=${PAGES_DIR#*=}

if [[ ! "$PAGES_DIR" =~ .*/$ ]]; then
    PAGES_DIR="${PAGES_DIR}/"
fi

echo "Rendering Markdown pages from '$PAGES_DIR' to '$APP_DIR'"

# Monitor directory for file system events
inotifywait -m -e create,modify,delete "${PAGES_DIR}" --format="%e\n%w\n%f"  |
while read -r -d '\n' action; read -N 1; read -r -d '\n' path; read -N 1; read -r file; do
    # echo "ACTION: $action PATH: $path FILE: $file"

    if [[ "$action" == "DELETE" ]]; then
        echo "Removing ${APP_DIR}${file}"
        rm ${APP_DIR}${file}
    elif [[ "$file" == *.md ]]; then
        echo "Generating Markdown for ${file} -> ${file%.md}.html"
        python md2html.py "${PAGES_DIR}${file}" "${APP_DIR}${file%.md}.html"
    else
        echo "Copying ${PAGES_DIR}${file} -> ${APP_DIR}${file}"
        cp "${PAGES_DIR}${file}" "${APP_DIR}${file}"
    fi
done
