# lianjiaSpider

链家成交数据爬虫，爬取某个小区的成交记录，支持记录去重和自动翻页

成交结果页：`https://bj.lianjia.com/chengjiao/c1111027380378/?sug=卧龙小区`，可以从中提取社区id （c1111027380378）作为爬虫的启动参数

## 运维

```shell
scrapy crawl lianjiadealspider -a communityid=c1111027376953 -a pagelimit=1
```

## 教程

[scrapy教程](https://www.runoob.com/w3cnote/scrapy-detail.html)

[scrapy官网](https://scrapy.org/)

[scrapy selector](https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors)

## 链家数据爬取

https://github.com/cnkai/lianjia/tree/master/lianjia/lianjia

https://blog.csdn.net/wantbar/article/details/78944977

https://www.cnblogs.com/cnkai/p/7405349.html

https://www.cnblogs.com/cnkai/p/7404972.html

https://www.jianshu.com/p/f426478b99c4

https://zhuanlan.zhihu.com/p/25240050

https://python.ctolib.com/sunrise10-lianjia.html