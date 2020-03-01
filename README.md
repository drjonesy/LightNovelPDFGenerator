# Light Novel PDF Generator

A Python 3 script that scrapes a website with light novels, generates an HTML file with all the content, and then generates a PDF with a TOC (Table of Contents)

I am using VSCode as my IDE along with Anaconda to create my virtual environments.

## Required

To build the PDF you will need to install: `wkhtmltopdf`<br />
Installation instructions can be found at: https://wkhtmltopdf.org/

## Python Libraries

```
pip install requests
pip install beautifulsoup4
pip install pdkit
```

## Execute Program
``` 
python ScrapeAndBuild.py 
```
