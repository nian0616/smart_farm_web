import requests
from bs4 import BeautifulSoup
import bs4

URL = 'http://quote.stockstar.com/futures/agroproductsinternation.shtml'

User-AgentHEADER = {
'':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

def getHTMLText(url):
    '''
    url: 爬取的网站网址
    return: 爬到的 html 内容
    '''
    try:
        r = requests.get(url, timeout=30, headers = HEADER)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fill_products_List(products_list, html):
    '''
    ulist: 目标要获得的农产品信息列表
    html: 爬到的 html 内容
    函数功能：解析 html，将其中需要的信息存储到列表数据结构中
    '''
    soup = BeautifulSoup(html, "html.parser")
    #print(soup.find('tbody').prettify())

    # 先把表头添进来
    for tr in soup.find('thead').children:
        if isinstance(tr, bs4.element.Tag): # 通过对 tag 类型的判断，过滤掉 tbody 的 children 中非标签的类型
            tds = tr('td')
            one_prod_list = []
            for i in range(len(tds)): #0-4
                for a in tds[i].children:
                    if isinstance(a, bs4.element.Tag):
                        one_prod_list.append(a.string)
            #print(one_prod_list)
            products_list.append(one_prod_list)
    
    # 再把表的数据添进来
    for tr in soup.find('tbody').children: # 一个 tr 对应一个农产品
        if isinstance(tr, bs4.element.Tag): # 通过对 tag 类型的判断，过滤掉 tbody 的 children 中非标签的类型
            tds = tr('td')
            one_prod_list = []
            for i in range(len(tds)): #0-4
                for a in tds[i].children:
                    #print(a)
                    if isinstance(a, bs4.element.Tag):
                        one_prod_list.append(a.string)
                    else:
                        one_prod_list.append(a)
            #print(one_prod_list)
            products_list.append(one_prod_list)

def print_products_list(products_list):
    '''
    products_list: 农产品信息列表
    '''
    #num = num+1 # 第一行是表头
    for i in range(len(products_list)):
        prod = products_list[i]
        print("{0:^10}\t{1:^10}\t{2:^10}".format(prod[0],prod[1],prod[2]))

def main():
    products_list = [] # 需要得到的目标：农产品信息列表
    html = getHTMLText(URL)
    fill_products_List(products_list, html)
    #print_products_list(products_list)
    products_list_ = []
    for prod in products_list:
        products_list_.append(prod)
    
    return products_list_
