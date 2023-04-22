Code highlighting in Markdown documents is handled by the `codehilite` extension of the Python Markdown library.

## Using Code Highlighting

To use code highlighting in your Markdown document, you will need to specify the language of the code snippet at the beginning of the code block using the `~~~` syntax. For example, to highlight a block of Python code, you would use the following syntax:

`~~~python def hello():     print("Hello, world!") ~~~`

This will produce the following highlighted code block:

~~~python
def hello():     print("Hello, world!")
~~~

Without mentioning the language explicitly, code highlighting is disabled:
~~~
def hello():     print("Hello, world!")
~~~

The `codehilite` extension supports a wide range of programming languages, including Python, HTML, CSS, JavaScript, Java, C++, and many others. To see a full list of supported languages, you can refer to the [official documentation](https://python-markdown.github.io/extensions/code_hilite/) for the `codehilite` extension.

### Theme

The theme for code highlighting is present in `static/code.css` file. You can customize this or generate new themes using Pygmentize. See [CodeHilite's excellent documentation](https://python-markdown.github.io/extensions/code_hilite/#step-2-add-css-classes) for simple instructions on generating new themes.