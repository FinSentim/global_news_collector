import unittest
from GlobalNewsCollector.China.yicai import Yicai
from datetime import datetime

class TestScrapper(unittest.TestCase):

    # Test for get_article
    def test_article(self):
        collector = Yicai()
        url = "https://www.yicai.com/news/101303550.html"
        article = collector.get_article(url)
        dictionary = {
            'date_published': "2022-01-27 16:54:25",
            'date_retrieved': datetime.today().strftime("%Y-%m-%d"),
            'url' : url,
            'title': "就地过年引发年货春运热潮，年前异地“孝心单”猛增",
            'publisher': 'yicai',
            'publisher_url': 'https://www.yicai.com/',
            'author': "作者：陆涵之    责编：刘佳",
            'body': '今年春节，不少人选择再次“就地过年”，春节前夕电商平台异地订单猛增。交通部此前披露数据显示，预计2022年春运全国将发送旅客11.8亿人次，日均2950万人次，较2021年同比增长35.6%，较2020年同比下降20.3%，较2019年同比下降60.4%。从交通部数据看，因疫情防控需求而选择就地过年的人不在少数。同时，今年春节物流快递实行“春节不打烊”政策。北京市邮政管理局副局长廖凌竹此前介绍，今年春节期间在岗从业人员约3.6万人，在岗率超过60%，其中邮政、顺丰、京东等主要品牌企业在岗率超过80%，能够满足春节期间邮政快递服务需要。此前，物流公司也宣布增加补贴春节在岗的快递小哥。京东物流今年春节将投入近4亿元，对春节坚守一线的员工加大福利补贴。菜鸟将投入超过3亿元的激励补贴，直接发放给值守的菜鸟一线产业员工。一位快递小哥对第一财经表示，今年春节选择继续加班，以应对增加的送货需求，同时增加收入。在异地过年人数增加、快递保障之际，今年的年货订单也飞快增长，引发了“年货春运”等新词汇的诞生。据电商平台，“年货春运”是指人们通过网购等形式置办年货，既满足了回乡过年的人们轻装上阵的需求，也满足了异地过年人群将年货直接寄回家的需求。从京东销售情况看，截至目前发往非常住地址的“异地订单”量同比（去年年货节第一周，下同）去年增长35%，而且异地订单占比已较平日上涨了50%。其中，山东、河南、湖北、江苏、四川是接受异地订单最多地区。截至1月23日下午17时，京东年货节累计已售超6.02亿件年货。从地域分布来看，北京、广东的年货消费热度最高涨，占比全国网购年货的1/4。江苏、山东、上海、四川、浙江紧随其后。美团优选数据显示，截至目前，通过美团优选下单到老家的“孝心单”全国单月订单已突破350万，其中北京孝心单订单量已突破86万单，环比增长12%，是一线城市中增速最快的城市。另一方面，年货订单的主力是年轻人，年轻人的年货订单也显示出与往年不同的特质。例如，有关健康的年货数量不断增加。北京冬奥会即将到来之际，围绕居家消费场景（舒适、运动、健康），年轻人购买的年礼也正在改变长辈眼中的传统习俗，带着长辈一起健身逐渐形成消费风潮。京东消费趋势显示，年轻人购买年礼中的国货占比也要高于平均值，比如“运动户外”的商品中，国货占比达91%。此外，年轻人并不喜欢“胡吃海睡”式过年。京东消费趋势显示，春节前夕，年货礼盒中包含“健康”关键词的商品销量同比增长超400%，养生类产品礼盒近三周销量较日常（10月日均增长）环比增长153%。其中，高端海产干货礼盒销量环比增长近10倍。另外，送枸杞成为35岁以下和56岁以上年龄段消费者的共同年礼选择。值得一提的是，近期电商订单中中国元素也逐渐增多，凸显了年味。从京东消费数据看，与“虎”相关的年货消费已经掀起热潮。12月以来含有“萌虎”元素的珠宝首饰成交额同比增长了85倍，服饰内衣成交额同比增长了14倍，年货节开始后，“萌虎”相关商品销量再次大增。同时，春联、红包、剪纸等代表传统文化的年货持续热销，更赢得了年轻消费者的心。'

        }
        self.assertEqual(article, dictionary)

    # Test for get_articles_list
    # Note that one could test the amount of articles retrieved only if we change the scrapper to include live articles
    def test_articles_list(self):
        collector = Yicai()
        url = "https://www.yicai.com/"
        list = collector.get_articles_list(url)
        for article in list:
            self.assertTrue(article != None)
            self.assertIsInstance(article, dict)

if __name__ == '__main__':
    unittest.main()