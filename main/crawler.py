#coding=utf-8
import json

import datetime
import urllib.request as urllib2
from lxml import etree


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}

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
            "replaceUrl": ("./", "http://www.csrc.gov.cn/pub/newsite/zjhxwfb/xwdd/")
        }
    },
    "保监会": {
        "http://www.circ.gov.cn/web/site0/tab5225/": {
            "xpath": '//div[@id="ess_mailrightpane"]/div/div[2]//td[@valign="top"]',
            "dateXpath": './/td[3]/text()',
            "titleXpath": './/td[2]//a/@title',
            "urlXpath": './/td[2]//a/@href',
            "replaceUrl": (None, "http://www.circ.gov.cn")
        },
        "http://www.circ.gov.cn/web/site0/tab5226/": {
            "xpath": '//div[@id="ess_mailrightpane"]/div/div[2]//td[@valign="top"]',
            "dateXpath": './/td[3]/text()',
            "titleXpath": './/td[2]//a/@title',
            "urlXpath": './/td[2]//a/@href',
            "replaceUrl": (None, "http://www.circ.gov.cn")
        },
        "http://www.circ.gov.cn/web/site0/tab5212/": {
            "xpath": '//div[@id="ess_mailrightpane"]/div/div[2]//td[@valign="top"]',
            "dateXpath": './/td[3]/text()',
            "titleXpath": './/td[2]//a/@title',
            "urlXpath": './/td[2]//a/@href',
            "replaceUrl": (None, "http://www.circ.gov.cn")
        },
        "http://www.gov.cn/pushinfo/v150203/base_14px_pubdate.htm": {
            "xpath": '//ul[@class="list"]/li',
            "dateXpath": 'span/text()',
            "titleXpath": 'a/text()',
            "urlXpath": 'a/@href',
            "replaceUrl": (None, "http://www.circ.gov.cn")
        }
    },
    "国土资源部": {
        "http://www.mlr.gov.cn/xwdt/kyxw/": {
            "xpath": '//table[@id="con"]//tr',
            "dateXpath": 'td[3]/text()',
            "titleXpath": 'td[2]/a/text()',
            "urlXpath": 'td[2]/a/@href',
            "replaceUrl": ("./", "http://www.mlr.gov.cn/xwdt/kyxw/")
        },
        "http://www.mlr.gov.cn/xwdt/jrxw/": {
            "xpath": '//table[@id="con"]//tr',
            "dateXpath": 'td[3]/text()',
            "titleXpath": 'td[2]/a/text()',
            "urlXpath": 'td[2]/a/@href',
            "replaceUrl": ("./", "http://www.mlr.gov.cn/xwdt/jrxw/")
        },
        "http://www.mlr.gov.cn/xwdt/dzdc/": {
            "xpath": '//table[@id="con"]//tr',
            "dateXpath": 'td[3]/text()',
            "titleXpath": 'td[2]/a/text()',
            "urlXpath": 'td[2]/a/@href',
            "replaceUrl": ("./", "http://www.mlr.gov.cn/xwdt/dzdc/")
        }
    },
    "国资委": {
        "http://www.sasac.gov.cn/n2588025/n2588119/index.html": {
            "xpath": '//div[@class="zsy_conlist"]/ul/span/li',
            "dateXpath": 'span/text()',
            "titleXpath": 'a/@title',
            "urlXpath": 'a/@href',
            "replaceUrl": ("../../", 'http://www.sasac.gov.cn/')
        },
        "http://www.sasac.gov.cn/n2588025/n2588129/index.html": {
            "xpath": '//div[@class="zsy_conlist"]/ul/span/li',
            "dateXpath": 'span/text()',
            "titleXpath": 'a/@title',
            "urlXpath": 'a/@href',
            "replaceUrl": ("../../", 'http://www.sasac.gov.cn/')
        },
        "http://www.sasac.gov.cn/n2588025/n2588124/index.html": {
            "xpath": '//div[@class="zsy_conlist"]/ul/span/li',
            "dateXpath": 'span/text()',
            "titleXpath": 'a/@title',
            "urlXpath": 'a/@href',
            "replaceUrl": ("../../", 'http://www.sasac.gov.cn/')
        }
    },
    "财政部": {
        "http://www.mof.gov.cn/zhengwuxinxi/caizhengxinwen/": {
            "xpath": '//table[@id="id_bl"]//tr/td',
            "dateXpath": None,
            "titleXpath": './@title',
            "urlXpath": './a/@href',
            "replaceUrl": (None, "http://www.mof.gov.cn")
        }
    },
    "能源局":{
        "http://www.mof.gov.cn/zhengwuxinxi/caizhengxinwen/": {
            "xpath": '//table[@id="id_bl"]//tr/td',
            "dateXpath": None,
            "titleXpath": './@title',
            "urlXpath": './a/@href',
            "replaceUrl": ('./', "http://www.mof.gov.cn")
        }
    },

    "铁道部": {
        "http://www.nra.gov.cn/xwzx/xwdt/xwlb/": {
            "xpath": '//div[@class="list"]/div/ul/li',
            "dateXpath":'./span/text()',
            "titleXpath":'./a/@title',
            "urlXpath":'./a/@href',
            "replaceUrl":('./', "http://www.nra.gov.cn/xwzx/xwdt/xwlb/")
        }
    },

    "中科院":{
          "http://www.cas.cn/syky/": {
              "xpath": '//div[@class="ztlb_ld_mainR_box01_list"]/ul/li',
              "dateXpath": './span/text()',
              "titleXpath": './span/a/@title',
              "urlXpath": './span/a/@href',
              "replaceUrl": ('./', 'http://www.cas.cn/syky/')
          },
          "http://www.cas.cn/yx/": {
              "xpath": '//div[@class="ztlb_ld_mainR_box01_list"]/ul/li',
              "dateXpath": './span/text()',
              "titleXpath": './span/a/@title',
              "urlXpath": './span/a/@href',
              "replaceUrl": ('./', 'http://www.cas.cn/yx/')
          }
    },

    "工信部":{
        "http://www.miit.gov.cn/n1146290/n1146402/n1146455/index.html": {
            "xpath": '//div[@class="clist_con"]/ul/li',
            "dateXpath": './span/text()',
            "titleXpath": './a/text()',
            "urlXpath": './a/@href',
            "replaceUrl": ('../../..', "http://www.miit.gov.cn")
        }
    },

    "商务部":{
          "http://www.mofcom.gov.cn/article/ae/": {
              "xpath": '//div[@class="MainList"]/div/div/div/ul/li',
              "dateXpath": './span/text()',
              "titleXpath": './a/@title',
              "urlXpath": './a/@href',
              "replaceUrl": (None, "http://www.mofcom.gov.cn")
          }
    },

    "旅游局":{
        "http://www.cnta.gov.cn/xxfb/jdxwnew2/": {
            "xpath": '//div[@class="liebiao"]/div/ul/li',
            "dateXpath": './a/span/text()',
            "titleXpath": './a/text()',
            "urlXpath": './a/@href',
            "replaceUrl": ("./", "http://www.cnta.gov.cn/xxfb/jdxwnew2/")
        }
    },

    "农业部":{
          "http://www.moa.gov.cn/zwllm/zwdt/": {
              "xpath": '//div[@class="zleft"]/ul/li',
              "dateXpath": './span[2]/text()',
              "titleXpath": './span[1]/a/@title',
              "urlXpath": './span[1]/a/@href',
              "replaceUrl": ("./", "http://www.moa.gov.cn/zwllm/zwdt/")
          }
    },

    "人社部":{
        "http://www.mohrss.gov.cn/SYrlzyhshbzb/dongtaixinwen/buneiyaowen/": {
            "xpath": '//div[@class="serviceMainListTabCon"]',
            "dateXpath": './div[3]/span/text()',
            "titleXpath": './div/span/a/@title',
            "urlXpath": './div/span/a/@href',
            "replaceUrl": (
            "./", 'http://www.mohrss.gov.cn/SYrlzyhshbzb/dongtaixinwen/dfdt/')
        },
        "http://www.mohrss.gov.cn/SYrlzyhshbzb/dongtaixinwen/dfdt/": {
            "xpath": '//div[@class="serviceMainListTabCon"]',
            "dateXpath": './div[3]/span/text()',
            "titleXpath": './div/span/a/@title',
            "urlXpath": './div/span/a/@href',
            "replaceUrl": (
            "./", 'http://www.mohrss.gov.cn/SYrlzyhshbzb/dongtaixinwen/dfdt/')
        }
    },

    "社科院":{
        "http://cass.cssn.cn/yaowen/": {
          "xpath": '//div[@class="con"]/div/ul/li',
          "dateXpath": None,
          "titleXpath": './a/text()',
          "urlXpath": './a/@href',
          "replaceUrl": ("./", "http://cass.cssn.cn/yaowen/")
        },
        "http://cass.cssn.cn/gundong/": {
          "xpath": '//div[@class="columnPagemain"]/div/ul/li',
          "dateXpath": None,
          "titleXpath": './a/text()',
          "urlXpath": './a/@href',
          "replaceUrl": ("../", 'http://cass.cssn.cn/')
        }
    },

    "城乡建设部":{
        "http://www.mohurd.gov.cn/xwfb/index.html": {
          "xpath": '//table//tr[2]/td/table//tr[2]/td/table//tr',
          "dateXpath": './td[3]/text()',
          "titleXpath": './td[2]/a/text()',
          "urlXpath": './td[2]/a/@href',
          "replaceUrl": (None, None)
        }
    },

    "交通运输部":{
        "http://www.mot.gov.cn/jiaotongyaowen/": {
        "xpath": '//div[@class="dfxw_main_bottom"]/ul/li',
        "dateXpath": './text()',
        "titleXpath": './a/@title',
        "urlXpath": './a/@href',
        "replaceUrl": (
        './', 'http://www.mot.gov.cn/jiaotongyaowen/')
        }
    },

    "民政部":{
        "http://www.mca.gov.cn/article/zwgk/mzyw/": {
            "xpath": '//div[@class="lalist_cont"]/ul/table//tr',
            "dateXpath": './td[3]/text()',
            "titleXpath": './td/a/@title',
            "urlXpath": './td/a/@href',
            "replaceUrl": (None, 'http://www.mca.gov.cn/')
        }
    },

    "国防部":{
        "http://www.mod.gov.cn/info/node_46924.htm": {
            "xpath": '//div[@class="main-section"]/ul/li/a',
            "dateXpath": './span/text()',
            "titleXpath": './text()',
            "urlXpath": './@href',
            "replaceUrl": (None, 'http://www.mod.gov.cn/info/')
        }
    },

    "教育部":{
        "http://www.moe.gov.cn/jyb_sy/sy_jyyw/": {
            "xpath": '//div[@id="wcmpagehtml"]/div/ul/li',
            "dateXpath": './span/text()',
            "titleXpath": './a/@title',
            "urlXpath": './a/@href',
            "replaceUrl": ("../../", 'http://www.moe.gov.cn/')
        },
        "http://www.moe.gov.cn/jyb_xwfb/s6192/s222/": {
            "xpath": '//div[@id="wcmpagehtml"]/div/ul/li',
            "dateXpath": './span/text()',
            "titleXpath": './a/@title',
            "urlXpath": './a/@href',
            "replaceUrl": ("./",'http://www.moe.gov.cn/jyb_xwfb/s6192/s222/')
        }
    },

    "监察部":{
      "http://www.ccdi.gov.cn/yw/": {
          "xpath": '//div[@id="wcmpagehtml"]/ul/li',
          "dateXpath": './span/text()',
          "titleXpath": './a/text()',
          "urlXpath": './a/@href',
          "replaceUrl": ("./",'http://www.ccdi.gov.cn/yw/')
      }
    },

    "司法部":{
        "http://www.moj.gov.cn/zfyw/index.html":{
            "xpath": '//div[@class="news_list"]/ul/li',
            "dateXpath": './dd/text()',
            "titleXpath": './dt/a/text()',
            "urlXpath": './dt/a/@href',
            "replaceUrl": (None, 'http://www.moj.gov.cn')
        }
    },

    "文化部":{
          "http://www.mcprc.gov.cn/whzx/whyw/": {
              "xpath": '//table[6]//tr/td[3]/table[5]//tr/td[2]/table//tr',
              "dateXpath": './td[3]/text()',
              "titleXpath": './td[2]/a/text()',
              "urlXpath": './td[2]/a/@href',
              "replaceUrl": ("./", 'http://www.mcprc.gov.cn/whzx/whyw/')
          }
    },

    "统计局":{
        "http://www.stats.gov.cn/tjsj/zxfb/":{
            "xpath": '//div[@class="center_list"]/ul/li/a',
            "dateXpath": './span/font[2]/text()',
            "titleXpath": './span/font[1]/text()',
            "urlXpath": './@href',
            "replaceUrl": ("./", 'http://www.stats.gov.cn/tjsj/zxfb/', 'http://www.stats.gov.cn')
        }
    },

    "体育总局":{
        "http://www.sport.gov.cn/n316/n337/index.html": {
            "xpath": '//*[@id="comp_8052"]/table//tr/td/table//tr/td/table//tr',
            "dateXpath": './td[3]/text()',
            "titleXpath": './td[2]/a/text()',
            "urlXpath": './td[2]/a/@href',
            "replaceUrl": ("../../", 'http://www.sport.gov.cn/')
        }
    },

    "食药监局":{
        "http://www.sda.gov.cn/WS01/CL0004/": {
            "xpath": '//td[@class="new2016_erji_content"]/table//tr/td',
            "dateXpath": './span/text()',
            "titleXpath": './a/font/text()',
            "urlXpath": './a/@href',
            "replaceUrl": ("../", 'http://www.sda.gov.cn/WS01/'),
            "decode":"gb2312"
        }
    },

    "网易科技":{
        "http://tech.163.com/": {
             "xpath": '//div[@class="newest-lists"]/ul/li/a',
             "dateXpath": './p/em/text()',
             "titleXpath": './p/text()',
             "urlXpath": './@href',
             "replaceUrl": (None, None)
        }
    },

    "环球科技（5G）":{
        "http://tech.huanqiu.com/comm/": {
            "xpath": '//div[@class="fallsFlow"]/ul/li',
            "dateXpath": './h6/text()',
            "titleXpath": './a/@title',
            "urlXpath": './a/@href',
            "replaceUrl": (None, None)
        }
    }
}


def crawler(url, xpath, dateXpath, titleXpath, urlXpath, replaceUrl, decode=None):
    # r = requests.get(url,)
    # r.encoding = "utf-8"
    # coding = r.encoding
    # print coding
    # html = etree.HTML(r.text)
    # r = urllib2.urlopen(url)
    req = urllib2.Request(url)
    req.add_header("User-Agent",headers["User-Agent"])
    r = urllib2.urlopen(req, timeout=1000)
    body = r.read()
    if decode:
        body = body.decode(decode)
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
                if not title:
                    title = sel.xpath(titleXpath)[1].strip()
            if urlXpath:
                articleUrl = sel.xpath(urlXpath)[0].strip()
            if "http://" not in articleUrl:
                if replaceUrl[0]:
                    articleUrl = articleUrl.replace(replaceUrl[0],replaceUrl[1])
                else:
                    articleUrl = replaceUrl[1]  + articleUrl
            if "http://" not in articleUrl:
                articleUrl = replaceUrl[2] + articleUrl
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
    print('begin:', datetime.datetime.now())
    result = {}
    for key, item in config.items():
        result[key] = {}
        if needItem:
            if key in needItem:
                for url in item:
                    conf = item[url]
                    result_get = crawler(url, conf['xpath'], conf['dateXpath'],
                                     conf['titleXpath'], conf['urlXpath'],
                                     conf['replaceUrl'])
                    result[key].update(result_get)
        else:
            for url in item:
                conf = item[url]
                result[key].update(
                    crawler(url, conf['xpath'], conf['dateXpath'], conf['titleXpath'], conf['urlXpath'],
                            conf['replaceUrl'], conf.get("decode",None))
                )
    print('end:', datetime.datetime.now())
    return result


if __name__ == "__main__":
    needItem = ["国务院","证监会","保监会","国土资源部","国资委","财政部","能源局","铁道部","中科院","工信部","商务部","旅游局","农业部","人社部","社科院","城乡建设部","交通运输部","民政部","国防部","教育部","监察部","司法部","文化部","统计局","体育总局","食药监局","网易科技","环球科技（5G）"]
    result = newsCrawl(needItem)
    json.dump(result, open('data.json', 'w'))






