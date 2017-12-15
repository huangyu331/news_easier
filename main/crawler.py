#coding=utf-8
import json

import datetime
import urllib.request as urllib2
from lxml import etree
from urllib.error import HTTPError
import time
import re


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
        },
        "http://www.gov.cn/xinwen/index.htm":{
            # "xpath": '//div[@class="column4"]/div[@class="column4_leftPart1"]/div[@class="zl_channel_body zl_channel_bodyxw"]/dl/dd/h4',
            # "dataXpath": 'span/text()',
            # 'titleXpath': 'a/text()',
            # 'urlXpath': 'a/@href',
            # 'replaceUrl': (None, "http://www.gov.cn"),
            "xpath": '//div[@class="slider-carousel"]/div/div/div/a',
            "dateXpath": None,
            "titleXpath": './text()',
            "urlXpath": './@href',
            "replaceUrl": (None, None),
            "splitVal": ""
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
    "银监会":{
        "http://www.cbrc.gov.cn/chinese/home/docViewPage/110008.html":{
            "xpath":'//div[@class="xia3"]/table/tr',
            "dateXpath":'./td[2]/text()',
            "titleXpath":'./td[1]/a/text()',
            "urlXpath":'./td[1]/a/@href',
            "replaceUrl":(None, "http://www.cbrc.gov.cn")
        },
        "http://www.cbrc.gov.cn/chinese/home/docViewPage/110010.html":{
            "xpath":'//div[@class="xia3"]/table/tr',
            "dateXpath":'./td[2]/text()',
            "titleXpath":'./td[1]/a/text()',
            "urlXpath":'./td[1]/a/@href',
            "replaceUrl":(None, "http://www.cbrc.gov.cn")
        }
    },
    "环保部":{
        "http://www.mep.gov.cn/gkml/73/75/index_835.htm":{
            "xpath": '//div[@id="documentContainer"]/div',
            "dateXpath": './li[4]/@title',
            "titleXpath": './li/div/a/text()',
            "urlXpath": './li/div/a/@href',
            "replaceUrl": ("../../", "http://www.mep.gov.cn/gkml/")
        },
        "http://www.mep.gov.cn/gkml/index_839.htm":{
            "xpath": '//div[@id="documentContainer"]/div',
            "dateXpath": './li[4]/@title',
            "titleXpath": './li/div/a/text()',
            "urlXpath": './li/div/a/@href',
            "replaceUrl": ("./", "http://www.mep.gov.cn/gkml/")
        }
    },
    "科技部":{
        "http://www.most.gov.cn/xinwzx/xwzx/fbhyg/":{
            "xpath":'//div[@id="TRS"]/table//tr/td/div/a',
            "dateXpath":None,
            "titleXpath":'./text()',
            "urlXpath":'./@href',
            "replaceUrl":('./', "http://www.most.gov.cn/xinwzx/xwzx/fbhyg/"),
            "splitVal":"("
        },
        "http://www.most.gov.cn/kjbgz/":{
            "xpath":'//td[@align="left"]/table//tr/td[2]',
            "dateXpath":'./text()',
            "titleXpath":'./a/text()',
            "urlXpath":'./a/@href',
            "replaceUrl":('./', "http://www.most.gov.cn/kjbgz/")
        },
        "http://www.most.gov.cn/dfkj/dfkjyw/dfzxdt/":{
            "xpath": '//div[@class="news1"]/ul/li/a',
            "dateXpath": None,
            "titleXpath": './text()',
            "urlXpath": './@href',
            "replaceUrl": ('../../', "http://www.most.gov.cn/dfkj/"),
            "splitVal":"("
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
            "replaceUrl": ("../../", r'http://www.sasac.gov.cn/')
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
        "http://www.nea.gov.cn/xwzx/nyyw.htm":{
            "xpath": '//div[@class="content"]/div/ul/li',
            "dateXpath": './span/text()',
            "titleXpath": './a/text()',
            "urlXpath": './a/@href',
            "replaceUrl": (None, None),
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
            "replaceUrl": ("./", "http://cass.cssn.cn/yaowen/"),
            # "splitVal": "",
            "conf": {
                "xpath": '//div[@class="con"]/div/h1',
                "dateXpath": None,
                "titleXpath": 'a/text()',
                "urlXpath": 'a/@href',
                "replaceUrl": ("./", "http://cass.cssn.cn/yaowen/"),
                # "splitVal": ""
            }
        },
        "http://cass.cssn.cn/gundong/": {
            "xpath": '//div[@class="columnPagemain"]/div/ul/li',
            "dateXpath": None,
            "titleXpath": './a/text()',
            "urlXpath": './a/@href',
            "replaceUrl": ("../", 'http://cass.cssn.cn/'),
            # "splitVal": ""
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
            "decode":"gbk"
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
    },
    "盖世汽车资讯（新能源）":{
        "http://auto.gasgoo.com/nev/C-501":{
             "xpath": '//div[@class="listLeft"]/div',
             "dateXpath": './div/div[3]/text()',
             "titleXpath": './h2/a/text()',
             "urlXpath": './h2/a/@href',
             "replaceUrl": (None, 'http://auto.gasgoo.com')
         },
        "http://auto.gasgoo.com/smart-connected/C-601":{
             "xpath": '//div[@class="listLeft"]/div',
             "dateXpath": './div/div[3]/text()',
             "titleXpath": './h2/a/text()',
             "urlXpath": './h2/a/@href',
             "replaceUrl": (None, 'http://auto.gasgoo.com')
         },
        "http://auto.gasgoo.com/after-market/C-105":{
             "xpath": '//div[@class="listLeft"]/div',
             "dateXpath": './div/div[3]/text()',
             "titleXpath": './h2/a/text()',
             "urlXpath": './h2/a/@href',
             "replaceUrl": (None, 'http://auto.gasgoo.com')
         },
        "http://auto.gasgoo.com/commercial-vehicle/C-104":{
             "xpath": '//div[@class="listLeft"]/div',
             "dateXpath": './div/div[3]/text()',
             "titleXpath": './h2/a/text()',
             "urlXpath": './h2/a/@href',
             "replaceUrl": (None, 'http://auto.gasgoo.com')
         },
        "http://auto.gasgoo.com/parts-news/C-103":{
             "xpath": '//div[@class="listLeft"]/div',
             "dateXpath": './div/div[3]/text()',
             "titleXpath": './h2/a/text()',
             "urlXpath": './h2/a/@href',
             "replaceUrl": (None, 'http://auto.gasgoo.com')
         },
        "http://auto.gasgoo.com/global-news/C-101":{
             "xpath": '//div[@class="listLeft"]/div',
             "dateXpath": './div/div[3]/text()',
             "titleXpath": './h2/a/text()',
             "urlXpath": './h2/a/@href',
             "replaceUrl": (None, 'http://auto.gasgoo.com')
         }
    },

    "中国新闻网（财经）":{
        "http://finance.chinanews.com/cj/gd.shtml":{
             "xpath": '//div[@class="content_list"]/ul/li',
             "dateXpath": './div[3]/text()',
             "titleXpath": './div/a/text()',
             "urlXpath": './div/a/@href',
             "replaceUrl": (None, 'http://finance.chinanews.com')
         }
    },

    "中国新闻网（产经）":{
        "http://www.chinanews.com/business/gd.shtml":{
             "xpath": '//div[@class="content_list"]/ul/li',
             "dateXpath": './div[3]/text()',
             "titleXpath": './div/a/text()',
             "urlXpath": './div/a/@href',
             "replaceUrl": (None, 'http://www.chinanews.com')
        }
    },

    "中国新闻网（能源）":{
        "http://www.chinanews.com/energy/gd.shtml":{
            "xpath": '//div[@class="content_list"]/ul/li',
            "dateXpath": './div[3]/text()',
            "titleXpath": './div/a/text()',
            "urlXpath": './div/a/@href',
            "replaceUrl": (None, 'http://www.chinanews.com')
        }
    },

    "证券时报网（财经）":{
        "http://kuaixun.stcn.com/finance/internal/":{
            "xpath": '//div[@class="mainlist"]/ul/li/p',
            "dateXpath": './span/text()',
            "titleXpath": './a/text()',
            "urlXpath": './a/@href',
            "replaceUrl": (None, None)
        }
    },

    "证券时报网（实时滚动）":{
        "http://www.stcn.com/gdxw/1.shtml":{
            "xpath": '//div[@class="mainlist"]/ul/li/p',
            "dateXpath": './span/text()',
            "titleXpath": './a/text()',
            "urlXpath": './a/@href',
            "replaceUrl": (None, None)
        }
    },
    "中证网（行业）":{
        "http://www.cs.com.cn/ssgs/hyzx/":{
            "xpath": '//div[@class="box1000"]/div/dl',
            "dateXpath": './dd/span/text()',
            "titleXpath": './dt/a/text()',
            "urlXpath": './dt/a/@href',
            "replaceUrl": ("./", "http://www.cs.com.cn/ssgs/hyzx/")
        }
    },

    "中证网（科技）":{
        "http://www.cs.com.cn/ssgs/kj/":{
            "xpath": '//div[@class="box1000"]/div/dl',
            "dateXpath": './dd/span/text()',
            "titleXpath": './dt/a/text()',
            "urlXpath": './dt/a/@href',
            "replaceUrl": ("./", "http://www.cs.com.cn/ssgs/kj/")
        }
    },

    "中证网（汽车）":{
        "http://www.cs.com.cn/ssgs/qcgs/":{
            "xpath": '//div[@class="box1000"]/div/dl',
            "dateXpath": './dd/span/text()',
            "titleXpath": './dt/a/text()',
            "urlXpath": './dt/a/@href',
            "replaceUrl": ("./", "http://www.cs.com.cn/ssgs/qcgs/")
        }
    },

    "中证网（房产）":{
        "http://www.cs.com.cn/ssgs/fcgs/":{
            "xpath": '//div[@class="box1000"]/div/dl',
            "dateXpath": './dd/span/text()',
            "titleXpath": './dt/a/text()',
            "urlXpath": './dt/a/@href',
            "replaceUrl": ("./", "http://www.cs.com.cn/ssgs/fcgs/")
        }
    },
    "腾讯财经（实时）":{
        "http://roll.finance.qq.com/interface/roll.php?cata=&site=finance&date=&page=1&mode=1&of=json": {
            "xpath": '//ul/li',
            "dateXpath": './span[1]/text()',
            "titleXpath": './a/text()',
            "urlXpath": './a/@href',
            "replaceUrl": (None, None),
            "header": {
                "Referer": "http://roll.finance.qq.com/"
            },
            "type": "jsonxpath",
            "decode": "gb2312"
        }

    },
    "新浪财经（产经）":{
        "http://feed.mix.sina.com.cn/api/roll/get?pageid=164&lid=1693&num=10&page=1":{
            "xpath": 'json',
            "dateXpath": 'ctime',
            "titleXpath": 'title',
            "urlXpath": 'url',
            "replaceUrl": (None, None)
        }
    },
    "新浪财经（财经）":{
        "http://feed.mix.sina.com.cn/api/roll/get?pageid=155&lid=1686&num=10&page=1": {
            "xpath": 'json',
            "dateXpath": 'ctime',
            "titleXpath": 'title',
            "urlXpath": 'url',
            "replaceUrl": (None, None)
        }
    },
    "新华网":{
        "http://www.news.cn/politics/24xsyw.htm":{
            "xpath": '//ul[@class="dataList"]/li',
            "dateXpath": './div/span/text()',
            "titleXpath": './h3/a/text()',
            "urlXpath": './h3/a/@href',
            "replaceUrl": (None, None)
        }
    }
}


def crawler(url, conf, body=None):
    xpath = conf.get('xpath',None)
    dateXpath = conf.get('dateXpath',None)
    titleXpath = conf.get('titleXpath',None)
    urlXpath = conf.get('urlXpath',None)
    replaceUrl = conf.get('replaceUrl',None)
    header = conf.get('header',None)
    type = conf.get('type', None)
    decode = conf.get('decode', None)
    if not body:
        req = urllib2.Request(url)
        req.add_header("User-Agent",headers["User-Agent"])
        if header:
            for key in header:
                req.add_header(key,header[key])
        try:
            r = urllib2.urlopen(req, timeout=20)
        except HTTPError as error:
            r = urllib2.urlopen(req, timeout=20)
        body = r.read()
        if decode:
            body = body.decode(decode)
    results = {}
    if "conf" in conf:
        results.update(crawler(url, conf['conf'], body))
    if xpath == "json":
        body = json.loads(body)
        for new in body['result']['data']:
            results[new[titleXpath]] = {
                "title": new[titleXpath],
                "updated_at": datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"),
                "published_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(new[dateXpath]))),
                "url": new[urlXpath]
            }

    else:
        if type and type == "jsonxpath":
            body = json.loads(body)
            body = body['data']['article_info']
        html = etree.HTML(body)
        sels = html.xpath(xpath)
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
                if not date and not dateXpath:
                    try:
                        splitVal = conf.get("splitVal","（")
                        find = None
                        try:
                            date = title.split(splitVal)[-1]
                            date = splitVal + date
                            find = re.search('\d+-\d+-\d+', date)
                        except:
                            pass
                        if find:
                            pass
                        else:
                            arr = articleUrl.split('/')
                            tem_time = arr[-1]
                            time1 = re.search('t(\d+)_', tem_time)
                            if time1:
                                time1 = time1.groups()[0]
                                try:
                                    date = time1[:4] + '-' + time1[4:6] + '-' + time[6:]
                                except Exception:
                                    date = ''
                                else:
                                    print('data:', date)
                            else:
                                time1 = re.search(r"/(\d{4})-(\d{2})/(\d{2})", articleUrl)
                                if time1:
                                    date = time1.group(1)+"-"+time1.group(2)+"-"+time1.group(3)
                    except:
                        pass

                results[title] = {
                    "title":title,
                    "updated_at":datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%M:%S"),
                    "published_at":date,
                    "url":articleUrl
                }
            except:
                pass
    return results

def newsCrawl(widget, needItem=None):
    print('begin:', datetime.datetime.now())
    result = {}
    total_category_num = len(config.items())
    tem_index = 1
    for key, item in config.items():
        widget.progress.set(int(tem_index / total_category_num * 100))
        tem_index += 1
        result[key] = {}
        if needItem:
            if key in needItem:
                for url in item:
                    conf = item[url]
                    try:
                        result_get = crawler(url, conf)
                    except Exception as e:
                        print('error:', e)
                        raise Exception()
                    else:
                        result[key].update(result_get)
        else:
            for url in item:
                conf = item[url]
                try:
                    result[key].update(
                        crawler(url, conf)
                    )
                except Exception as e:
                    print("error:", e)
    print('end:', datetime.datetime.now())
    return result

def newsCrawl1(needItem=None):
    print('begin:', datetime.datetime.now())
    result = {}
    total_category_num = len(config)
    tem_index = 1
    for key, item in config.items():
        result[key] = {}
        if needItem:
            total_category_num = len(needItem)
            if key in needItem:
                for url in item:
                    conf = item[url]
                    result_get = crawler(url, conf)
                    result[key].update(result_get)
                # widget.progress.set(int(tem_index / total_category_num) * 100)
                # tem_index += 1
        else:
            for url in item:
                conf = item[url]
                try:
                    result[key].update(
                        crawler(url, conf)
                    )
                except Exception:
                    pass
            # widget.progress.set(int(tem_index / total_category_num) * 100)
            # tem_index += 1
    print('end:', datetime.datetime.now())
    return result


if __name__ == "__main__":
    needItem = ["国务院","证监会","保监会","国土资源部","国资委","财政部","能源局","铁道部","中科院","工信部","商务部","旅游局","农业部","社科院","城乡建设部","交通运输部","民政部","国防部","教育部","监察部","司法部","文化部","统计局","体育总局","食药监局","网易科技","环球科技（5G）"]
    result = newsCrawl1()
    json.dump(result, open('data.json', 'w'))






