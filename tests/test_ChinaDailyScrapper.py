# coding: utf-8
import unittest
import datetime 
from GlobalNewsCollector.China.ChinaDailyScrapper import ChinaDailyScrapper 


class TestChinaDailyScrapper(unittest.TestCase):
        
    def test_get_article(self):
        collector = ChinaDailyScrapper()
        test_article = {
        "body": ['中国日报网1月28日电（记者 张文芳） 来自美国波士顿的媒体人魏思得（Michael Wester）已经在北京居住了21年。这些年里，他见证了冬季运动在中国的蓬勃发展，也深切感受到冬奥会给北京带来的种种变化。', '2000年，魏思得来到北京，致力于向在北京的外国人介绍当地文化活动，增进中外了解，一晃已经在北京生活了20多年。他说，现在的北京生活非常便利，已经是一个非常现代化的城市，无论是地铁还是其他城市基础设施。','谈及举办冬奥会给北京带来的变化，魏思得说：“几个月前我乘高铁去了崇礼，那是一次很棒的经历。我觉得举办奥运会是一个让城市增强基础设施建设的机会，不仅仅是为比赛做准备，也是为了生活在这里的人们，所以我觉得北京因为举办奥运会而有了很大的变化。”', '魏思得特别表示，近年来，北京很让人值得自豪的一点是，环境质量自2008年以来获得了极大改善。','作为冰雪运动爱好者，魏思得见证了冬季运动在中国的蓬勃发展。','20年前，他的公司经常会在冬季组织滑雪游。那时候，大部分去滑雪的都是外国人，上了雪道你就会发现，大部分滑雪的中国人都是新手，他们都在初级道上，或者还在参加滑雪培训。而且那个时候学滑雪的孩子很少。','魏思得说：“现在，几乎所有的小孩都在学滑雪，参加滑雪训练营。你再去雪场，甚至会碰到一些水平高到让你觉得简直能参加奥运会的高手。”','新冠疫情虽未结束，魏思得认为，北京冬奥会不会受到影响。“因为，北京在防控新冠疫情方面，做的更加安全和谨慎。”','他说，新冠疫情基本得到控制，防疫措施比世界上绝大多数城市的防控都更有效，而且针对可能会发生的意外情况也做了准备，这些措施都很超前。','魏思得表示，即使出现运动员感染等最坏的情况，中国也能处理好，因为有相应的规章制度应对这些突发情况，保障大家的安全。', '（编辑：齐磊 刘世东）'],
        "title":  '【中国那些事儿】美国媒体人魏思得：感受到冬奥会给北京带来的种种变化',
        "date_of_publication": '2022-01-28 17:38',
        "date_retrieved": datetime.datetime.now(),
        "url": 'https://cn.chinadaily.com.cn/a/202201/28/WS61f3b9a8a3107be497a047ba.html',
        "author": '张文芳',
        "publisher": 'China Daily'
        }
        url = "https://cn.chinadaily.com.cn/a/202201/28/WS61f3b9a8a3107be497a047ba.html"
        article = collector.get_article(url)
        self.assertEqual(test_article, article)


if __name__ == '__main__':
    unittest.main()