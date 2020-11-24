import scrapy
from ..items import AmazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
        # 'https://www.amazon.in/s?k=mobiles&i=electronics&ref=nb_sb_noss_2'
        # 'https://www.amazon.in/s?k=tv&i=electronics&ref=nb_sb_noss'
        # 'https://www.amazon.in/s?k=laptops&i=computers&ref=nb_sb_noss_1'
        # 'https://www.amazon.in/s?k=computers&i=computers&ref=nb_sb_noss_1'
        # 'https://www.amazon.in/s?k=home+%26+kichen&i=kitchen&ref=nb_sb_noss_2'
        # 'https://www.amazon.in/s?k=Refrigerators&rh=n%3A1380365031&ref=nb_sb_noss'
        # 'https://www.amazon.in/s?k=furnitures&i=furniture&ref=nb_sb_noss_1'
        # 'https://www.amazon.in/s?k=iphones&i=electronics&ref=nb_sb_noss_2'
        # 'https://www.amazon.in/s?k=clothes&i=apparel&ref=nb_sb_noss_2'
        # 'https://www.amazon.in/s?k=watches&i=watches&ref=nb_sb_noss_1'
        # 'https://www.amazon.in/s?k=industrial+and+scientific&i=industrial&ref=nb_sb_noss_1'
        # 'https://www.amazon.in/s?k=lab+and+scientific+products&rh=n%3A6409335031&ref=nb_sb_noss'
        # 'https://www.amazon.in/s?k=iphone+mobiles&i=electronics&rh=n%3A1389432031%2Cp_89%3AApple&dc&qid=1606137283&rnid=3837712031&ref=sr_nr_p_89_1'
        # 'https://www.amazon.in/s?bbn=1389401031&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cp_89%3ARedmi&dc&fst=as%3Aoff&qid=1606138358&rnid=3837712031&ref=lp_1389401031_nr_p_89_0'
        'https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A976419031%2Cn%3A976420031%2Cn%3A1389401031%2Cp_89%3AOppo&dc&fst=as%3Aoff&qid=1606138752&rnid=3837712031&ref=sr_nr_p_89_1'

    
    
    ]
    def parse(self, response):

        items = AmazonItem()

        all_amazon_data = response.css('div.s-latency-cf-section')                # rush-component
        # all_amazon_data = response.css('div.a-section a-spacing-medium')                # rush-component
        # all_amazon_data = response.css('div.sg-row')                # rush-component
        # all_amazon_data = response.css('div.sg-col-inner .sg-col-24-of-28 ')                # rush-component

        for data in all_amazon_data:
            product_name = data.css('.a-color-base.a-text-normal::text').extract()
            product_image = data.css('.s-image::attr(src)').extract()
            # product_price = data.css('.a-price-whole').css('::text').extract()
            # product_link = data.css('a::attr(href)').extract()                      #      product link css
            
            items['product_name'] = product_name
            items['product_image'] = product_image
            # items['product_price'] = product_price
            # items['product_link'] = product_link

            yield items

            next_page = 'https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A976419031%2Cn%3A976420031%2Cn%3A1389401031%2Cp_89%3AOppo&dc&page=2&fst=as%3Aoff&qid=1606138756&rnid=3837712031&ref=sr_pg_'+ str(AmazonSpiderSpider.page_number)
            print(next_page)
            if AmazonSpiderSpider.page_number <= 10:
                AmazonSpiderSpider.page_number += 1
                yield response.follow(next_page, callback = self.parse)