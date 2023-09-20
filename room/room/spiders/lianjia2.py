import scrapy
from scrapy_redis.spiders import RedisSpider


class LianjiaSpider(RedisSpider):
    name = 'lianjia2'
    allowed_domains = ['lianjia.com']

    redis_key = 'lianjia:start_urls'
    pn = 1
    # start_urls = ['https://bj.lianjia.com/ershoufang/pg1/']

    def parse(self, response):
        '''
        解析房屋列表页
        '''
        # 获取每一个房子的链接
        all_room_url = response.xpath('//div[@class="title"]/a/@href').getall()
        for url in all_room_url:
            # 发送每一个房子的链接
            yield scrapy.Request(url=url, callback=self.parse_room)
        # 变更页码
        self.pn += 1
        # 获取下一页数据
        yield scrapy.Request(url = 'https://bj.lianjia.com/ershoufang/pg{pn}/')
    def parse_room(self,response):
        '''
        解析房屋详细数据
        '''
        total = response.xpath('//span[@class="total"]/text()').get() # 获取总价
        community_name = response.xpath('//div[@class="communityName"]/a[1]/text()').get()  # 小区名称
        area_name = response.xpath('string(//div[@class="areaName"]/span[@class="info"])').get() # 区域名称

        base =  response.xpath('//div[@class="base"]/div[@class="content"]/ul')
        hu_xing = base.xpath('./li[1]/text()').get() # 户型
        lou_ceng = base.xpath('./li[2]/text()').get() # 楼层
        mian_ji = base.xpath('./li[3]/text()').get() # 面积
        chao_xiang = base.xpath('./li[5]/text()').get() # 朝向
        gong_nuan = base.xpath('./li[last()]/text()').get() # 供暖

        quan_shu = response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[2]/span[2]/text()').get()  # 交易权属
        yong_tu = response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[4]/span[2]/text()').get()  # 房屋用途

        yield {
           'total':total,
            'community_name':community_name,
            'area_name':area_name,
            'hu_xing':hu_xing,
            'lou_ceng':lou_ceng,
            'mian_ji':mian_ji,
            'chao_xiang':chao_xiang,
            'gong_nuan':gong_nuan,
            'quan_shu':quan_shu,
            'yong_tu':yong_tu
        }