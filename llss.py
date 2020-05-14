import requests, re,time
from lxml import etree


class llss:
    def __init__(self):
        pass

    def gethtml(self):
        print("kaishi1")
        url = 'https://llss.li/wp/category/all/anime/page/2/'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Referer': url
        }
        r = requests.get(url, headers=headers)
        r.encoding = r.apparent_encoding
        html = etree.HTML(r.content)
        print('html结束')
        last_url = html.xpath('//*[@id="main"]/center/div/a[6]/@href')

        nwe_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Referer': last_url[0]
        }
        new_r = requests.get(url=last_url[0], headers=nwe_headers)
        new_html = etree.HTML(new_r.content)
        num = new_html.xpath('//*[@id="main"]/center/div/span[3]/text()')
        print("num is ", num)
        for i in range(1, int(num[0]) + 1):
            url = 'https://llss.li/wp/category/all/anime/page/{}/'.format(i)
            self.page_url(url)

    def page_url(self, url):

        item = {}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Referer': url
        }
        r = requests.get(url, headers=headers)
        url = etree.HTML(r.content).xpath('//*[@class="entry-title"]/a/@href')

        for i in url:
            i_headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
                'Referer': i
            }
            time.sleep(1)
            r = requests.get(url=i, headers=i_headers)
            r.encoding=r.apparent_encoding
            html = etree.HTML(r.content)
            title = html.xpath('//h1[@class="entry-title"]/text()')
            # getman = re.compile(r'<div><.*?><.*?/>(.*?)</div>')
            getman=re.compile('\w{40}',re.S)

            manget=re.findall(getman,r.text)
            if len(manget)==0:
                continue
            else:

                with open('llss.txt','a',encoding='utf-8')as f:

                    for cl in manget:
                        set(cl)
                        data="magnet:?xt=urn:btih:"+cl
                     # f.write(title+","+data+"\n")
                        a=title,data,"url is ",i
                        f.write(str(title)+str(data)+"\n")





if __name__ == '__main__':
    llss = llss()
    llss.gethtml()
