import requests, os, sys
from bs4 import BeautifulSoup
import pdfkit

def digitToStr(num: int=1, size: int=3):
    '''Converts a digit to string with the total characters = size
        
            num: int
            size: int

        ex: size = 3 ...therefore... 1 = 001, 34 = 034
    '''
    num_str = str(num)
    zeros = ''
    if len(num_str) < size:
        zeros = (size - len(num_str)) * '0'
    return f"{zeros}{num_str}"   

def isInt(string: str=''):
    try:
        int(string)
        return True
    except ValueError:
        return False        

# ================ MAIN ===================

if __name__ == "__main__":
    

    URL_PREFIX = 'https://kisslightnovels.info/novel/arifureta-shokugyou-de-sekai-saikyou/arifureta-shokugyou-de-sekai-saikyou-wn-chapter-'
    NOVEL_NAME = URL_PREFIX.lstrip('https://kisslightnovels.info/novel/').split('/')[0]
    
    chapter_count = 0 # starting url chapter
    volume = 0
    current_volume = -1
    error_404_count = 0 # if this value => 3 no more chapter exist

    html_content = f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{NOVEL_NAME}</title></head><body>'
    file_path = f"novels/{NOVEL_NAME}"

    try:
        os.makedirs("novels")
    except FileExistsError:
        pass
    
    # if file exists remove
    if os.path.isfile(f"{file_path}.html"):
        os.remove(f"{file_path}.html")

    # make HTML file
    with open(f"{file_path}.html", 'w+') as htmlFile:
        htmlFile.write(html_content)

    while True:
        html_content = ''
        chapter_count += 1
        URL_NUM = digitToStr(num=chapter_count, size=3) # convert 1 to 001
        URL = URL_PREFIX + URL_NUM
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')

        if "error404" in str(soup.find('body')):
            error_404_count += 1
            print(f"Page Number: {chapter_count} doesn't exist!")
            break
        else:
            content_block = soup.find('div', attrs={'class': 'text-left'})
            # remove the line that starts with: https://novelplanet.com/
            text_list = [f"{p.text}" for p in content_block.findAll('p') if "novelplanet.com" not in p.text]
            
            html_content += '<div style="margin: 110px 0;">&nbsp;</div>'
            html_content += '<hr />'

            
            if isInt(text_list[0].split(" ")[-1]):
                current_volume = int(text_list[0].split(" ")[-1])

            if volume != current_volume:
                print(f"Volume: {volume + 1}")
                html_content += f'<h1 style="font-size: 1em;">Volume: {volume + 1}</h1>'
                html_content += '<hr />'
                volume = current_volume

            chapter_title = text_list[2].split(" : ")[-1]
            html_content += f'<h2 style="font-size: 2em; font-weight: bold;">Chapter {int(URL_NUM)-1} : {chapter_title}</h2>'

            # format as html <p> string
            for i in range(len(text_list)):
                if "* * *" in text_list[i]:
                    html_content +=  f'<p style="text-align: center">{text_list[i]}</p>\n'
                else:
                    html_content +=  f'<p>{text_list[i]}</p>\n'


            # append HTML file
            with open(f"{file_path}.html", 'a+') as htmlFile:
                htmlFile.write(html_content)
                htmlFile.write("\n")
            
            print(f"Volume: {volume} | Chapter: {int(URL_NUM)-1} : {chapter_title}")
            

    # NO MORE CHAPTERS
    print(f"No more chapters available")
    html_content += '</body></html>'
    # append HTML file
    with open(f"{file_path}.html", 'a+') as htmlFile:
        htmlFile.write(html_content)

    pdfkit.from_file(input=f"{file_path}.html",output_path=f"{file_path}.pdf")
    # (html_content, f"{file_path}.pdf")

