#coding=UTF-8
import urllib.request
import re
import urllib

def report_hook(blocks_read, block_size, total_size):
    if not blocks_read:
        print("开始下载")
        return
    if total_size < 0:
        print("读取第%s个8KB数据块，已下载%sB（字节）" % (blocks_read, blocks_read * block_size))
    else:
        amount_read = blocks_read * block_size
        s=amount_read*100.0/(total_size)
        if s>=100:
            s=100
        print("读取第%s个8KB数据块， %sB/%sB, %.0f%%" % (blocks_read, amount_read, total_size, s))

def searchimg(word):
    #url='http://baike.baidu.com/item/%E5%9C%B0%E7%90%83/6431'
    url='http://baike.baidu.com/view/'+word+'.htm'


    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.8, en-GB; q=0.5, en; q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': url,
    'Connection': 'keep-alive',
    'Host': 'baike.baidu.com',
    }

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')]

    print(url)
    #wp=urllib.request.urlopen(url)
    #str0=wp.read()
    str0=opener.open(url).read()



    print(str0)
    str1=str0.decode('utf-8','ignore')
    pa=r'<title>(.*)</title>'
    patt=re.compile(pa)
    filename=str(re.findall(patt,str1)[0])
    pb = r'src="(.*?\.jpg)" '
    pbtt = re.compile(pb)
    imglist = re.findall(pbtt,str1)
    x = 0
    for imgurl in imglist:
        print("\n准备下载图片%s.jpg" % x)
        urllib.request.urlretrieve(imgurl, '%s_%s.jpg' %(filename,x),reporthook=report_hook)
        x += 1
        if x>=100:
            break
    else:
        print('\n\n')
    f = open("%s.txt" % filename,"a+",encoding="utf-8")
    f.write(str1)
    if f:
        f.close()


def show():
    url="http://baike.baidu.com/"
    webp=urllib.request.urlopen(url)
    str0=webp.read()
    str1=str0.decode('utf-8','ignore')
    print(str0)
    f = open("out.txt","a+",encoding="utf-8")
    f.write(str1)
    if f:
        f.close()

global a
global b
a=1
f = open("out.txt","w",encoding="utf-8")

if f:
    f.close()

while a!=3:
    a=input("请选择功能：1.抓图   2.显示并保存百科首页的源代码   3.退出\n")
    a=int(a)
    if a==1:
        b=input("请输入搜索关键字(数字)\n")
        searchimg(b)
    elif a==2:
        show()
    else:
        break

#str=webp.read().decode("utf-8","ignore")

#print(webp.read().decode("utf-8"))
#res=bs(requests.get(url).text,"html.parser")

