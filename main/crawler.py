#coding=utf-8
import json

import datetime
from urllib.request import urlopen
from lxml import etree
import sys

def crawler(url, xpath, dateXpath, titleXpath, urlXpath, replaceUrl):
    # r = requests.get(url,)
    # r.encoding = "utf-8"
    # coding = r.encoding
    # print coding
    # html = etree.HTML(r.text)
    r = urlopen(url)
    body = r.read()
    html = etree.HTML(body)
    sels = html.xpath(xpath)
    results = {}
    for sel in sels:
        date,title = None,None
        try:
            if dateXpath:
                date = sel.xpath(dateXpath)[0].strip()
            if titleXpath:
                title = sel.xpath(titleXpath)[0].strip()
            if urlXpath:
                articleUrl = sel.xpath(urlXpath)[0].strip()
            if "http://" not in articleUrl:
                if replaceUrl[0]:
                    articleUrl = articleUrl.replace(replaceUrl[0],replaceUrl[1])
                else:
                    articleUrl = replaceUrl[1]  + articleUrl
            # print date,title,articleUrl
            results[title] = {
                "title":title,
                "updated_at":datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%M:%S"),
                "published_at":date,
                "url":articleUrl
            }
        except:
            pass
    return results


def newsCrawl(needItem=None):
    config = {
        "国务院": {
            "http://www.gov.cn/xinwen/yaowen.htm": {
                "xpath": '//div[@class="news_box"]/div/ul/li/h4',
                "dateXpath": "span/text()",
                "titleXpath": "a/text()",
                "urlXpath": "a/@href",
                "replaceUrl": (None, "http://www.gov.cn")
            }
        },
        "证监会": {
            "http://www.csrc.gov.cn/pub/newsite/zjhxwfb/xwdd/": {
                "xpath": '//div[@class="fl_list"]/ul/li',
                "dateXpath": "span/text()",
                "titleXpath": "a/text()",
                "urlXpath": "a/@href",
                "replaceUrl": ("./", "http://www.csrc.gov.cn/pub/newsite/flb/flfg/xzfg_8248/")
            }
        }
    }
    result = {}
    for key, item in config.items():
        result[key] = {}
        if needItem:
            if key in needItem:
                for url in item:
                    conf = item[url]
                    result[key].update(
                        crawler(url, conf['xpath'], conf['dateXpath'], conf['titleXpath'], conf['urlXpath'],
                                               conf['replaceUrl'])
                    )
        else:
            for url in item:
                conf = item[url]
                result[key].update(
                    crawler(url, conf['xpath'], conf['dateXpath'], conf['titleXpath'], conf['urlXpath'],
                            conf['replaceUrl'])
                )
    return result


if __name__ == "__main__":
    needItem = ["国务院", "证监会"]
    result = newsCrawl(needItem)
    print(type(result), result)
    json.dump(result, open('data.json', 'w'))

    # with open("text",'w') as code:
    #     code.write(json.dumps(result))

    # print datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%M:%S")
    # 国务院
    # url = "http://www.gov.cn/xinwen/yaowen.htm"
    # xpath = '//div[@class="news_box"]/div/ul/li/h4'
    # dateXpath = 'span/text()'
    # titleXpath = 'a/text()'
    # urlXpath = 'a/@href'
    # replaceUrl = (None,"http://www.gov.cn")

    # 证监会
    # "http://www.csrc.gov.cn/pub/newsite/zjhxwfb/xwdd/"
    # url = "http://www.csrc.gov.cn/pub/newsite/flb/flfg/xzfg_8248/"
    # xpath = '//div[@class="fl_list"]/ul/li'
    # dateXpath = 'span/text()'
    # titleXpath = 'a/text()'
    # urlXpath = 'a/@href'
    # replaceUrl = ("./", "http://www.csrc.gov.cn/pub/newsite/flb/flfg/xzfg_8248/")

    # 银监会（有问题）
    # url = "http://www.cbrc.gov.cn/chinese/home/docViewPage/110008.html"
    # xpath = '//div[@class="xia3"]'
    # dateXpath = 'td[2]/text()'
    # titleXpath = '/td[1]/a/text()'
    # urlXpath = 'td[1]/a/@href'
    # replaceUrl = ("./", "http://www.cbrc.gov.cn")

    # 保监会
    # url = "http://www.circ.gov.cn/web/site0/tab5225/"
    # url = "http://www.circ.gov.cn/web/site0/tab5226/"
    # url = "http://www.circ.gov.cn/web/site0/tab5212/"
    # xpath = '//div[@id="ess_mailrightpane"]/div/div[2]//td[@valign="top"]'
    # dateXpath = './/td[3]/text()'
    # titleXpath = './/td[2]//a/@title'
    # urlXpath = './/td[2]//a/@href'
    # replaceUrl = (None, "http://www.circ.gov.cn")

    # 特例 http://www.circ.gov.cn/web/site0/tab5212/
    # url = "http://www.gov.cn/pushinfo/v150203/base_14px_pubdate.htm"
    # xpath = '//ul[@class="list"]/li'
    # dateXpath = 'span/text()'
    # titleXpath = 'a/text()'
    # urlXpath = 'a/@href'
    # replaceUrl = (None, "http://www.circ.gov.cn")

    # 科技部(有问题，还未写)
    # url = "http://www.gov.cn/pushinfo/v150203/base_14px_pubdate.htm"
    # xpath = '//ul[@class="list"]/li'
    # dateXpath = 'span/text()'
    # titleXpath = 'a/text()'
    # urlXpath = 'a/@href'
    # replaceUrl = (None, "http://www.circ.gov.cn")

    # 国土资源部
    # url = "http://www.mlr.gov.cn/xwdt/kyxw/"
    # url = "http://www.mlr.gov.cn/xwdt/jrxw/"
    # url = "http://www.mlr.gov.cn/xwdt/dzdc/"
    # xpath = '//table[@id="con"]//tr'
    # dateXpath = 'td[3]/text()'
    # titleXpath = 'td[2]/a/text()'
    # urlXpath = 'td[2]/a/@href'
    # replaceUrl = ("./", url)

    # 国资委
    # url = "http://www.sasac.gov.cn/n2588025/n2588119/index.html"
    # url = "http://www.sasac.gov.cn/n2588025/n2588129/index.html"
    # url = "http://www.sasac.gov.cn/n2588025/n2588124/index.html"
    # xpath = '//div[@class="zsy_conlist"]/ul/span/li'
    # dateXpath = 'span/text()'
    # titleXpath = 'a/@title'
    # urlXpath = 'a/@href'
    # replaceUrl = ("../../", 'http://www.sasac.gov.cn')

    # 卫生计生委(有问题)
    # url = "http://www.nhfpc.gov.cn/zhuz/dfxw/list.shtml"
    # xpath = '//div[@class="list"]/ul/li'
    # dateXpath = 'span/text()'
    # titleXpath = 'a/@title'
    # urlXpath = 'a/@href'
    # replaceUrl = (None, None)

    # 财政部
    # url = "http://www.mof.gov.cn/zhengwuxinxi/caizhengxinwen/"
    # xpath = '//table[@id="id_bl"]//tr/td'
    # dateXpath = None
    # titleXpath = './@title'
    # urlXpath = './a/@href'
    # replaceUrl = (None, "http://www.mof.gov.cn")

    # 能源局
    # url = "http://www.mof.gov.cn/zhengwuxinxi/caizhengxinwen/"
    # xpath = '//table[@id="id_bl"]//tr/td'
    # dateXpath = None
    # titleXpath = './@title'
    # urlXpath = './a/@href'
    # replaceUrl = ('./', "http://www.mof.gov.cn")

    # 铁道部
    # url = "http://www.nra.gov.cn/xwzx/xwdt/xwlb/"
    # xpath = '//div[@class="list"]/div/ul/li'
    # dateXpath = './span/text()'
    # titleXpath = './a/@title'
    # urlXpath = './a/@href'
    # replaceUrl = ('./', "http://www.nra.gov.cn/xwzx/xwdt/xwlb")

    # 中科院
    # url = "http://www.cas.cn/syky/"
    # url = "http://www.cas.cn/yx/"
    # xpath = '//div[@class="ztlb_ld_mainR_box01_list"]/ul/li'
    # dateXpath = './span/text()'
    # titleXpath = './span/a/@title'
    # urlXpath = './span/a/@href'
    # replaceUrl = ('./', url)

    # 工信部
    # url = "http://www.miit.gov.cn/n1146290/n1146402/n1146455/index.html"
    # xpath = '//div[@class="clist_con"]/ul/li'
    # dateXpath = './span/text()'
    # titleXpath = './a/text()'
    # urlXpath = './a/@href'
    # replaceUrl = ('../../..', "http://www.miit.gov.cn")




