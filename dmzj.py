import requests
from bs4 import BeautifulSoup
from lxml import etree
import re
import threading
import time
'''
最终保存为漫画名+链接

需要评的自己改下匹配吧


'''


def GetHtml():
    #//处理第一个页面
    url="https://www.dmzj.com/rank"
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
    r=requests.get(url=url,headers=headers,)
    r.encoding=r.apparent_encoding
    return r.text

def html_work():
    #//页面里面匹配小链接并且传递
    html=GetHtml()
    # bs=BeautifulSoup(html,"html.parser")
    html=etree.HTML(html)
    href_1=html.xpath("//ul[@class='ph_l_li']/li/a/@href")
    title_1=html.xpath("//ul[@class='ph_l_li']/li/a/text()")
    for i in href_1:
        link_Splicing(i)


def link_Splicing(url):
    #//拼接
    new_url="https://www.dmzj.com"+str(url)
    link_tow_Splicing(new_url)






def link_tow_Splicing(url):
    #//第二次处理
    # print("接受到的url是",url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
    r = requests.get(url=url, headers=headers)
    r.encoding=r.apparent_encoding
    html=etree.HTML(r.text)
    page=html.xpath("//div[@class='bottom_page page']/a/@href")
    del page[0]
    del page[0]
    for i in page:
        new_page(i)
    # print(page)
    # seen=set()
    # seen.add(i for i  in page)
    # print()

    # print(type(page))
    # if page != None:
    #     link_tow_Splicing()





def new_page(url):
    #//re匹配保存
    url = "https://www.dmzj.com" + str(url)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
    r=requests.get(url=url,headers=headers)
    r.encoding=r.apparent_encoding
    html=etree.HTML(r.text)
    getlink=re.compile(r'<a target="_blank" class="dec_img" href="(.*?)" title="">')
    gettitle=re.compile(r'<a.*? >(.*?)</a>')
    link=re.findall(getlink,r.text)
    title=re.findall(gettitle,r.text)
    # print(title[0:-4])
    # print(link)
    with open('dmzj.txt','a',encoding='utf-8')as f:
        for i in  range(len(link)):
            print("已保存第{}次".format(i))
            f.write(title[i]+":"+link[i]+"\n")







if __name__ == '__main__':
    start = time.process_time()
    html_work()
    # t1=threading.Thread(target=html_work())
    # t2 = threading.Thread(target=html_work())
    # t3 = threading.Thread(target=html_work())
    # t4 = threading.Thread(target=html_work())
    # t5 = threading.Thread(target=html_work())
    # t6 = threading.Thread(target=html_work())
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()
    # print("over")
    end = time.process_time()
    print('different is %6.3f' % (end - start))

