import urllib.request
from urllib import parse
import re
import gzip
import io 
import json
import zlib

def searchtext(placename):
    url='https://movie.douban.com/j/subject_suggest?q='+parse.quote(placename.encode('utf-8'))

    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'movie.douban.com',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache'
    }
    
    req = urllib.request.Request(url, headers=headers, method="GET")
    rawreq=urllib.request.urlopen(req)
    
    encoding = rawreq.getheader('Content-Encoding')
    page = rawreq.read()
    content=''
    if encoding == 'gzip':
        buf = io.BytesIO(page)
        gf = gzip.GzipFile(fileobj=buf)
        content1 = gf.read()
        content=content1.decode()
    else:
        print('No result, please change the keyword')
        return
    moviejson=json.loads(content)
    print('results:')
    for movie in moviejson:
        print('id:',movie["id"],'\t','name:',movie["title"],'(%s)'%movie["year"])
    movieid=input('Choose an id and type it: ')
    if [movie for movie in moviejson if movie["id"]==movieid] is []:
        print('wrong id')
        return
    movieurl='https://movie.douban.com/subject/'+movieid
    req = urllib.request.Request(movieurl, headers=headers, method="GET")
    rawreq=urllib.request.urlopen(req)
    
    encoding = rawreq.getheader('Content-Encoding')
    page = rawreq.read()
    content=''
    if encoding == 'gzip':
        buf = io.BytesIO(page)
        gf = gzip.GzipFile(fileobj=buf)
        content1 = gf.read()
        content=content1.decode()
    content=re.sub('\n','',content)
    tagpattern=re.compile('<div class="tags-body">(.*?)</div>')
    tagtext = re.findall(tagpattern,content)
    eachtagpattern=re.compile('<a href="/tag/(.*?)" class="">(.*?)</a>')
    tags = re.findall(eachtagpattern,tagtext[0])
    for tag in tags:
        print(tag[0]) 

place=input("input the keyword: ")
searchtext(place)