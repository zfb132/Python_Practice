# coding=utf-8
import urllib.request
import re
import urllib
import os
import time


def report_hook(blocks_read, block_size, total_size):
    if not blocks_read:
        print("开始下载")
        return
    if total_size < 0:
        print("读取第%s个8KB数据块，已下载%sB（字节）" % (blocks_read, blocks_read * block_size))
    else:
        amount_read = blocks_read * block_size
        s = amount_read*100.0/(total_size)
        if s >= 100:
            s = 100
        print("读取第%s个8KB数据块， %sB/%sB, %.0f%%" % (blocks_read, amount_read, total_size, s))


def searchurl(word):
    url = 'https://www.qcloud.com'+word
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')]
    print(url)
    str0 = opener.open(url).read()
    str1 = str0.decode('utf-8', 'ignore')
    pa = r'href="(/doc/product/[1-9]{3,3})"'
    patt = re.compile(pa)
    listurl = re.findall(patt, str1)

    pc = r'hotrep="document\.file\.product\.(.*)"'
    pctt=re.compile(pc)
    filename=re.findall(pctt, str1)

    a=0
    for m in listurl:
        filename[a]=filename[a].replace(' ','')
        cmd="cmd.exe /c md C:\\Users\\admin\\Desktop\\%s" %filename[a]
        info=os.system(cmd)
        if info!=1:
            searchpdf(m,filename[a])
        a=a+1

def searchpdf(key,realname):
    url1='https://www.qcloud.com'+key
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')]
    str0=opener.open(url1).read()
    str1=str0.decode('utf-8','ignore')

    pa=r'href="https:(//.{70,90}\.pdf)"'
    patt=re.compile(pa)
    pdfurl=re.findall(patt,str1)

    pb=r'<h3>(.*)</h3>'
    pbtt=re.compile(pb)
    pdftitle=re.findall(pbtt,str1)



    b=0
    for i in pdfurl:
        print("http:"+i+"\t"+pdftitle[b])
        urllib.request.urlretrieve("http:"+i, 'C:\\Users\\admin\\Desktop\\%s\\%d_%s.pdf' %(realname,b+1,pdftitle[b]),reporthook=report_hook)
        b=b+1

if __name__=="__main__":
    searchurl("/doc/product")

