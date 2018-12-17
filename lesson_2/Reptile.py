import urllib.request
# url_base = r'www.cnblogs.com'
url_base = r'www.google.com.hk'
HTTPS_PRE = r'https://'
gs_url = HTTPS_PRE + url_base #+ r'/scholar?hl=en&as_sdt=0%2C5&as_ylo=2014&q=%22systematic+innovation%22&btnG='

test_url = HTTPS_PRE + url_base + r'/kmonkeywyl/p/8458442.html'
print(gs_url)
headers = {'Host': url_base,
           'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
           'Accept': r'application/json, text/javascript, */*; q=0.01',
           'Referer': HTTPS_PRE + url_base, }
req = urllib.request.Request(gs_url, headers=headers)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
print(html)