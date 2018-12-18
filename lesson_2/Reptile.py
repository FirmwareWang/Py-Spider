# -*- coding = utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup


def download_scholar_content(file_name):
    url_base = r'scholar.google.com'
    HTTPS_PRE = r'https://'
    gs_url = HTTPS_PRE + url_base + \
        r'/scholar?hl=en&as_sdt=0%2C5&as_ylo=2014&q=%22systematic+innovation%22&btnG='

    headers = {'Host': url_base,
               'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
               'Accept': r'application/json, text/javascript, */*; q=0.01',
               'Referer': HTTPS_PRE + url_base, }
    req = urllib.request.Request(gs_url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    with open(file_name, "w", encoding='utf-8') as f:
        f.writelines(soup.prettify())


if __name__ == '__main__':
    file_name = 'google_scholar.txt'
    download_scholar_content(file_name)
