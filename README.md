# Light Novel PDF Generator

A Python 3 script that scrapes a website with light novels, generates an HTML file with all the content, and then generates a PDF with a TOC (Table of Contents)

I am VSCode as my IDE along with Anaconda to create my virtual environments.

## Required

To build the PDF you will need to install: `wkhtmltopdf`<br />
Installation instructions can be found at: https://wkhtmltopdf.org/

## Python Libraries

```
import requests
import os
from bs4 import BeautifulSoup
import pdfkit
```

## Execute Program
``` 
python ScrapeAndBuild.py 
```
