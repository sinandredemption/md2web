md2web is a minimalistic, hackable Flask application that renders Markdown files as HTML pages.

[demo.webm](https://user-images.githubusercontent.com/47252029/233772908-5afd56f7-b16a-458d-91f7-fed017127aa4.webm)

## Features
- Real-time synchronization between Markdown files and HTML.
- Simple, flexible URL parsing.
- Code highlighting works out-of-the-box.
- Written with hackability and minimalism in mind.

## Getting Started

- **Clone the project** 
```
git clone https://github.com/sinandredemption/md2web.git
```

- **Install dependencies:** Navigate to the project directory and install the necessary dependencies. 
```
cd md2web
pip install -r requirements.txt
```

- **Start the server** 
```
./start.sh
```

- **Demo:** You can now view the demo website by opening a web browser and navigating to `http://localhost:5000`. The website should display the content of the Markdown files in the `Sample Website` directory.

- **Make changes:** You can modify the content of the Markdown files in the `Sample Website` directory and save the changes. Refresh the website to verify that the changes are reflected in real-time.

By default, md2web will serve a website that will give you a good tour of the features and a jist of md2web. The fastest way to get started would be to build your project on top of that website.

## Usage & Features

### Project Structure
The Project has the following structure:
- **templates/:** This folder contains all the HTML that is generated from the Markdown files.
- **Markdown/:** This folder contains some sample markdown files. You can put your own Markdown files here or configure md2web to search for markdown in a new folder (see configuration).
- **static/:** This folder contains styles for the website and code-highlighting.
- **templates/__base.html:** The base of every page, containing header and footer. Edit to customize to your needs.
- **templates/__404.html**: Error 404 page.
- **app.py:** The main Flask app, containing all the routes.
- **config:** The configuration file.
- **config.py:** Loads the configuration file in the Flask app.
- **md2html.py:** Takes in a markdown file and converts it to HTML.
- **generate-website.py:** Ensures the markdown files and HTML files (and all other files) are in sync. This script is ran at the start of the Flask server.
- **start.sh:** Start and runs the Flask server.

### Configuration

The `config` file contains configuration options (in a `key=value` format). The file `config.py` acts as the configuration parser. Lines starting with a `#` character are treated as comments and ignored by the configuration parser.

#### Options
- `WebsiteName`: The name of the website.
- `PagesPath`: The absolute path to the directory where the Markdown files for the website are located.

A sample `config` with generic defaults is provided.

### Page structure
`Frontpage.md` is automatically set as the default "home" of your website.

### URL Handling
URLs are handled as paths to files inside `templates` folder, but with a bit more flexibility.

##### Ignoring characters and extensions in HTML File Names
When serving HTML files, md2web ignores all characters except for alpha-numeric characters. This means that if you have a file called `My Cool Page!!!.md`, the resulting HTML file will be called `My Cool Page!!!.html`. So, if you want to access that file, you can use the URL `/blog/my-cool-page` regardless of the exact case of the letters or the presence of spaces or hyphens.

##### Case Insensitivity for Folders and Files
Folders and files in md2web are not case-sensitive. This means that if you have a folder called `Blog`, you can access it with any combination of upper and lower case letters, such as `/blog`, `/bLog`, or `/BLOG`. The same applies to files within those folders - for example, if you have a file called `MyFile.html`, you can access it with any combination of upper and lower case letters, such as `/blog/myfile`, `/Blog/Myfile`, or `/BLOG/MYFILE`.

##### '-' (dash) is substituted by space
In md2web, the '-' character in URLs is substituted by a space character ' '. So, for example, `/blog/my-file` and `/blog/my file` both point to the same file.

##### Serving non-HTML Files
If you have non-HTML files in your `templates` directory, md2web will serve them directly if there is an exact match in the URL. For example, if you have a file called `Resume.pdf` in your `templates` directory, you can access it directly with `/Resume.pdf`.

### Real-time synchonization
md2web supports real-time synchronization between files in the `PagesPath` folder (see section on [configuration](#Configuration) above) and the served website. This allows users to see changes made to Markdown (or any) files immediately reflected in their browser without the need to manually regenerate the HTML files or the website.

When a file is modified or created in the `PagesPath` folder, `inotifytools` detects the change and triggers the regeneration/copying of the corresponding HTML/non-HTML file. The changes are then immediately reflected in the browser upon refreshing the page.

### Code Highlighting

Code highlighting in Markdown documents is handled by the `codehilite` extension of the Python Markdown library.

#### Using Code Highlighting

To use code highlighting in your Markdown document, you will need to specify the language of the code snippet at the beginning of the code block using the `~~~` syntax. For example, to highlight a block of Python code, you would use the following syntax:

`~~~python def hello():     print("Hello, world!") ~~~`

**Note:** Without mentioning the language explicitly, code highlighting is disabled.

The `codehilite` extension supports a wide range of programming languages, including Python, HTML, CSS, JavaScript, Java, C++, and many others. To see a full list of supported languages, you can refer to the [official documentation](https://python-markdown.github.io/extensions/code_hilite/) for the `codehilite` extension.

##### Theme
The theme for code highlighting is present in `static/code.css` file. You can customize this or generate new themes using Pygmentize. See [CodeHilite's excellent documentation](https://python-markdown.github.io/extensions/code_hilite/#step-2-add-css-classes) for simple instructions on generating new themes.

## Credits
- [Modern Font Stacks](https://modernfontstacks.com/)
- [Better Website](http://bettermotherfuckingwebsite.com/)

## Philosophy
- http://suckless.org/sucks/web/

## Authors
- [GitHub](https://github.com/sinandredemption)

## License
This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details.
