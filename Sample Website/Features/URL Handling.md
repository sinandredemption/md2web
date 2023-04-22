URLs are handled as paths to files inside `templates` folder, but with a bit more flexibility.

## Ignoring characters and extensions in HTML File Names

When serving HTML files, md2web ignores all characters except for alpha-numeric characters. This means that if you have a file called `My Cool Page!!!.md`, the resulting HTML file will be called `My Cool Page!!!.html`. So, if you want to access that file, you can use the URL `/blog/my-cool-page` regardless of the exact case of the letters or the presence of spaces or hyphens.

## Case Insensitivity for Folders and Files

Folders and files in md2web are not case-sensitive. This means that if you have a folder called `Blog`, you can access it with any combination of upper and lower case letters, such as `/blog`, `/bLog`, or `/BLOG`. The same applies to files within those folders - for example, if you have a file called `MyFile.html`, you can access it with any combination of upper and lower case letters, such as `/blog/myfile`, `/Blog/Myfile`, or `/BLOG/MYFILE`.

## '-' (dash) is substituted by space

In md2web, the '-' character in URLs is substituted by a space character ' '. So, for example, `/blog/my-file` and `/blog/my file` both point to the same file.

## Serving non-HTML Files

If you have non-HTML files in your `templates` directory, md2web will serve them directly if there is an exact match in the URL. For example, if you have a file called `Resume.pdf` in your `templates` directory, you can access it directly with `/Resume.pdf`.

