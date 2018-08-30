#coding=utf-8
import re
import urllib
import urllib.request
import os

def report_hook(blocks_read, block_size, total_size):
    if not blocks_read:
        print("start")
        return
    if total_size < 0:
        print("read %s 8KB blocks , download %sB (bytes)" % (blocks_read, blocks_read * block_size))
    else:
        amount_read = blocks_read * block_size
        s=amount_read*100.0/(total_size)
        if s>=100:
            s=100
        print("read %s 8KB blocks ,  %sB/%sB, %.0f%%" % (blocks_read, amount_read, total_size, s))


def curlist(ckey,img,file):
    url='http://g.sbkk8.cn/mingzhu/ertong/'+ckey
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')]
    str0=opener.open(url).read()
    str1=str0.decode('gb2312','ignore')
    #print(str1)
    pa=r'src="(/uploads/allimg/.{10,25}.jpg)"'
    patt=re.compile(pa)
    pdfurl=re.findall(patt,str1)
    for i in pdfurl:
        img=img.replace(" ","")
        urllib.request.urlretrieve("http://g.sbkk8.cn"+i,"D:\\1acharle\\%s\\%s.jpg" %(file,img),reporthook=report_hook)

def burlist(bkey,name):
    url1='http://g.sbkk8.cn/mingzhu/ertong/'+bkey
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')]
    str0=opener.open(url1).read()
    str1=str0.decode('gb2312','ignore')
    #print(str1)
    pa=r'href="/mingzhu/ertong/(.{10,60})">(.{3,20})<i>></i>'
    patt=re.compile(pa)
    pdfurl=re.findall(patt,str1)
#    print(pdfurl[1][1])    #可以成功显示
    for i in pdfurl:
        curlist(i[0],i[1],name)    #可以成功显示


def aurlist(akey):
    url='http://g.sbkk8.cn/mingzhu/ertong/'+akey
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')]
    str0=opener.open(url).read()
    str1=str0.decode('gb2312','ignore')
    #print(str1)
    pa=r'href="/mingzhu/ertong/(.{6,40})">(.{6,20})<i>></i>'
    patt=re.compile(pa)
    pdfurl=re.findall(patt,str1)
#    print(pdfurl[1][1])    #可以成功显示
    for i in pdfurl:
#        print(i)    #可以成功显示
        filename=i[1].replace(' ','')
        cmd="cmd.exe /c md D:\\1acharle\\%s" %filename
        info=os.system(cmd)
        if info!=1:
            burlist(i[0],filename)

if __name__=="__main__":
    aurlist("chalijiushiquanji")