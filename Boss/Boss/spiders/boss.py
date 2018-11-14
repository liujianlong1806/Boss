# -*- coding: utf-8 -*-
import scrapy
from Boss.items import BossItem


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    csid=101010100
    baseurl = 'https://www.zhipin.com/c'
    baseur = '/?query=python&page='
    page = 1
    start_urls = [str(baseurl+str(csid)+baseur+str(page))]
    print(start_urls)

    def parse(self, response):
        print(1)
        for i in range(1,11):
            print(2)
            '''取前10页'''
            # zhiweis = response.xpth('//div[@class="job-title"]')
            # gongzis = response.xpth('//span[@class="red"]')
            # gongsis = response.xpth('//div/div/div/h3/a')
            # xiangqings = response.xpth('//div[@class="job-primary"]/div/p')
            gongzuo = response.xpath('//li/div[@class="job-primary"]')
            print(gongzuo)
            for i in gongzuo:
                print('i:',i)
                zhiwei = i.xpath('./div/h3/a/div[@class="job-title"]/text()').extract()
                print('--------------------------')
                print(zhiwei)
                gongzi = i.xpath('./div/h3/a/span/text()').extract()[0]
                gongsi = i.xpath('./div/div/h3/a/text()').extract()[0]
                didian = i.xpath('./div[@class="info-primary"]/p/text()').extract()[0]
                jingyan = i.xpath('./div[@class="info-primary"]/p/text()').extract()[1]
                xueli = i.xpath('./div[@class="info-primary"]/p/text()').extract()[2]
                data = [zhiwei,gongzi,gongsi,didian,jingyan,xueli]
                with open('boss.csv','a') as f:
                    f.write(data)

            if response.xpath('//a[@class="next"]'):
                self.page += 1
                url = self.baseurl+str(self.csid)+self.baseur+str(self.page)
                yield scrapy.Request(url, callback=self.parse)
            else:
                '''如果没有下一页就结束循环'''
                self.page = 1
                self.csid +=100
                url = self.baseurl+str(self.csid)+self.baseur+str(self.page)
                yield scrapy.Request(url,callback=self.parse)
