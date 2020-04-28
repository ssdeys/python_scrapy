import requests
import re
from lxml import etree
def get_html_one():
    url = 'https://ddrk.me/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r.encoding=r.apparent_encoding
    html = etree.HTML(r.text)
    list = html.xpath("//div[@class='nav-links']/a/@href")
    num_page = html.xpath("//a[@class='page-numbers']/text()")
    num = int(num_page[-1])
    print(num)
    for i in range(num + 1):
        if i ==0:
            print("no")
        else:
            url = "https://ddrk.me/page/" + str(i)

            print(url)

        # print(type(url))
            url_data(url=url)
def url_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    htmls = etree.HTML(r.text)
    getlink = re.compile(r'<h2 class="post-box-title"><a href="(.*?)" rel="bookmark">.*</a></h2>')
    gettitle = re.compile(r'<h2 class="post-box-title"><a.*?>(.*?)</a></h2>')
    link = re.findall(getlink, r.text)
    title = re.findall(gettitle, r.text)
    print(title, "\n",link)
    with open('ddrk.txt','a',encoding='utf-8')as f:
        for i in range(len(title)):


            f.write(title[i] +":"+link[i] +" \n")
        f.close()
        print("写入完成")


if __name__ == '__main__':
        get_html_one()