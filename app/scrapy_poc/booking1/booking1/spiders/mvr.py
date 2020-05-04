# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MvrSpider(scrapy.Spider):
    name = 'mvr'
    # allowed_domains = ['www.booking.com']
    start_urls = ['http://www.booking.com/']





    def parse(self, response):
        # print(response.text)
        checkin = '30/06/2020'
        checkout = '1/06/2020'
        self.checkin_monthday, self.checkin_month, self.checkin_year = checkin.split('/')
        self.checkout_monthday, self.checkout_month, self.checkout_year = checkout.split('/')
        search_text = "Ratnagiri"
        self.log('I just visited: ' + response.url)
        url =  'https: // www.booking.com / searchresults.en - gb.html?label = gen173nr - 1FCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4Aomz7PQFwAIB & ' +'sid = 1f8f24df45a23dca47ed40a2e91b55df & sb = 1 & sb_lp = 1 & src = index & src_elem = sb & error_url = https % 3A % 2F % 2Fwww.booking.com % 2Findex.en' + ' - gb.html % 3Flabel % 3Dgen173nr - 1FCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4Aomz7PQFwAIB % 3Bsid % 3D1f8f24df45a23dca47ed40a2e91b55df' +' % 3Bsb_price_type % 3Dtotal % 26 % 3B & ss = Ratnagiri % 2C + Maharashtra % 2C + India & is_ski_area = 0 & checkin_year = ' + self.checkin_year + ' & checkin_month = ' + self.checkin_month + ' & ' +'checkin_monthday = ' + self.checkin_monthday + ' & checkout_year = ' + self.checkout_year + ' & checkout_month = ' + self.checkout_year + ' & checkout_monthday = ' + self.checkout_monthday + ' & group_adults = 2 & group_children = 0 & no_rooms = 1 & b_' +'h4u_keep_filters = & from_sf = 1 & ss_raw = ' + search_text + ' & ac_position = 0 & ac_langcode = en & ac_click_type = b & dest_id = -2109258 & dest_type = city &' +' place_id_lat = 16.983299 & place_id_lon = 73.300003 & search_pageview_id = a4786b45fe300022 & search_selected = true'
        url=url.replace(" ", "")
        # print(type(url))
        yield scrapy.Request(url=url,callback=self.parse1)


        url='https://www.booking.com/hotel/in/mango-valley-resort-ratnagiri.en-gb.html?label=gen000nr-10CAEoggI46AdIM1gEaOwBiAEBmAEzuAEFyAEH2AED6AEB-AEBiAIBqAIBuAKs4uX0BcACAQ;sid=1f8f24df45a23dca47ed40a2e91b55df;all_sr_blocks=421644302_174652031_0_42_0;checkin=2020-05-30;checkout=2020-05-31;dest_id=-2109258;dest_type=city;dist=0;from_beach_non_key_ufi_sr=1;group_adults=2;group_children=0;hapos=10;highlighted_blocks=421644302_174652031_0_42_0;hpos=10;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=421644302_174652031_0_42_0__450000;srepoch=1587227734;srpvid=cfec74ab3d5e0018;type=total;ucfs=1&#hotelTmpl'

        # item = {}

        # item['prop_type'] = []

        # for i in range(4):
            # print(i)
            # item['prop_type'].extend(response.css('#basiclayout > div.d-index__section.bui-spacer--largest.js-ds-layout-events-bh_promotions > div > ul > li:nth-child('+str(i+1)+') > div > div.bui-card__content > h3 > a::text').extract())

        # print(response.css('#basiclayout > div.d-index__section.bui-spacer--largest.js-ds-layout-events-bh_promotions > div > ul > li:nth-child(1) > div > div.bui-card__content > h3 > a::text').extract())
        # yield item
        # view(response)  #this is command line tool to open the webpage of response

        # filename = response.url.split("/")[-1] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

    def parse1(self,response):
        print(response.url)
        hotelid='4216443'
        # print(response.css('#right > div:nth-child(5) > div > div.sr_header--title > div > h1::text').extract())
        a=0
        for i in range(25):
            hid=response.css('#hotellist_inner > div:nth-child('+str(i+1)+')::attr(data-hotelid)').extract()
            print(i)
            try:
                if hid[0]==hotelid:
                    self.listing=i+1-a
                    self.next_url='https://www.booking.com'+response.css('#hotel_4216443 > a::attr(href)').extract()[0]
                    self.next_url='https://www.booking.com/hotel/in/mango-valley-resort-ratnagiri.en-gb.html?label=gen173nr-1FCAsobEIdbWFuZ28tdmFsbGV5LXJlc29ydC1yYXRuYWdpcmlICVgEaGyIAQGYAQm4ARfIAQzYAQHoAQH4AQKIAgGoAgO4ApTv7_QFwAIB;sid=1f8f24df45a23dca47ed40a2e91b55df;all_sr_blocks=421644302_174652031_0_42_0;+checkin='+self.checkin_year+'-'+self.checkin_month+'-'+self.checkin_monthday+';checkout='+self.checkout_year+'-'+self.checkout_month+'-'+self.checkout_monthday+';dest_id=-2109258;dest_type=city;dist=0;from_beach_non_key_ufi_sr=1;group_adults=2;group_children=0;hapos=1;highlighted_blocks=421644302_174652031_0_42_0;hp_group_set=0;hpos=1;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=421644302_174652031_0_42_0__450000;srepoch=1587280151;srpvid=8c22324b097400d8;type=total;ucfs=1&#hotelTmpl'
                    # self.next_url='https://www.booking.com/hotel/in/mango-valley-resort-ratnagiri.en-gb.html?label=gen173nr-1FCAsobEIdbWFuZ28tdmFsbGV5LXJlc29ydC1yYXRuYWdpcmlICVgEaGyIAQGYAQm4ARfIAQzYAQHoAQH4AQKIAgGoAgO4ApTv7_QFwAIB;sid=1f8f24df45a23dca47ed40a2e91b55df;all_sr_blocks=421644302_174652031_0_42_0;+checkin=2020-05-30;checkout=2020-05-31;dest_id=-2109258;dest_type=city;dist=0;from_beach_non_key_ufi_sr=1;group_adults=2;group_children=0;hapos=1;highlighted_blocks=421644302_174652031_0_42_0;hp_group_set=0;hpos=1;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=421644302_174652031_0_42_0__450000;srepoch=1587280151;srpvid=8c22324b097400d8;type=total;ucfs=1&#hotelTmpl'
                    print(self.next_url)

                    break
            except Exception as e:
                print(e,e.args)
                a+=1
                continue
        print('listing= '+ str(self.listing))
        yield scrapy.Request(url=self.next_url, callback=self.parse2)


    def parse2(self,response):
        print(response.url)
        print(response.xpath('//*[@id="hprt-table"]').extract())
        # filename =  'acd.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
    #
    # def parse2(self,response):
    #     print(response.css('#hp_hotel_name::text').extract())
    #     print(response.xpath('//*[@id="hprt-table"]').extract())
    #     print(response.css('#hprt-form > div.hprt-container > div.hprt-table-cell.-last.hprt-reservation-summary-col.js-hprt-reservation-summary > div.hprt-block.reserve-block-js > div.hprt-booking-cta-ticker > ul > li.hprt-booking-cta-ticker__list-item.cta-list-item--immediate-conf::text').extract())
    #     print(response.css('#RD421644302 > a::text').extract())
    #     print(response.css('#room_type_id_421644308::text').extract())
    #     yield scrapy.FormRequest.from_response(response,
    #                         formxpath='//*[@id="hotelpage_availform"]',
    #                         # formdata={'name': 'John Doe', 'age': '27'},
    #                         callback=self.parse3)
    #     # filename =  'acd.html'
    #     # with open(filename, 'wb') as f:
    #     #     f.write(response.body)
    #
    #     rd=['RD421644302','RD421644303','RD421644305','RD421644305','RD421644307','RD421644308']
    #
    # def parse3(self,response):
    #     print('a')
    #     print(response.url)
    #     print(response.css('#hprt-table > tbody > tr.hprt-table-cheapest-block.hprt-table-cheapest-block-fix.js-hprt-table-cheapest-block > td.d_pd_hp_price_left_align.hprt-table-cell.hprt-table-cell-price > div > div.prco-wrapper.bui-price-display.prco-sr-default-assembly-wrapper.prc-d-sr-wrapper > div.bui-price-display__value.prco-font16-helper::text').extract())
    #     # yield scrapy.Request(url='https://www.booking.com/searchresults.html?checkin_monthday=7&checkin_year_month=2020-5&checkout_monthday=31&checkout_year_month=2020-5&tab=&origin=hp&src=hotel&hp_avform=1&error_url=%2Fhotel%2Fin%2Fmango-valley-resort-ratnagiri.html%3Flabel%3Dgen173nr-1FCAsobEIdbWFuZ28tdmFsbGV5LXJlc29ydC1yYXRuYWdpcmlICVgEaGyIAQGYAQm4ARfIAQzYAQHoAQH4AQKIAgGoAgO4ApTv7_QFwAIB%3Bsid%3D1f8f24df45a23dca47ed40a2e91b55df%3Bsrpvid%3D8c22324b097400d8%26%3B&do_availability_check=on&label=gen173nr-1FCAsobEIdbWFuZ28tdmFsbGV5LXJlc29ydC1yYXRuYWdpcmlICVgEaGyIAQGYAQm4ARfIAQzYAQHoAQH4AQKIAgGoAgO4ApTv7_QFwAIB&lang=en-us&sid=1f8f24df45a23dca47ed40a2e91b55df&no_redirect_check=1&dest_type=city&dest_id=-2109258&highlighted_hotels=4216443&no_rooms=1&group_adults=2&group_children=0#sort_by',callback=self.parse4)
    #     url='https://www.booking.com/hotel/in/mango-valley-resort-ratnagiri.en-gb.html?aid=378266;label=bdot-Os1%2AaFx2GVFdW3rxGd0MYQS267778093357%3Apl%3Ata%3Ap1%3Ap22%2C583%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-334108349%3Alp1007796%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YYriJK-Ikd_dLBPOo0BdMww;sid=1f8f24df45a23dca47ed40a2e91b55df;all_sr_blocks=421644302_141698786_0_42_0;checkin=2020-05-07;checkout=2020-05-31;dest_id=-2109258;dest_type=city;dist=0;from_beach_non_key_ufi_sr=1;group_adults=2;group_children=0;hapos=12;highlighted_blocks=421644302_141698786_0_42_0;hpos=12;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=421644302_141698786_0_42_0__9720000;srepoch=1587296451;srpvid=cf1e522133f6011b;type=total;ucfs=1&#hotelTmpl'
    #     yield scrapy.Request(url=url,callback=self.parse6)
    #     # filename =  'acd.html'
    #     # with open(filename, 'wb') as f:
    #     #     f.write(response.body)
    #
    # def parse4(self,response):
    #     print(response.url)
    #     print(response.css('#hotellist_inner > div.sr_item.sr_item_new.sr_item_default.sr_property_block.sr_flex_layout.sr_item--highlighted.with_dates > div.sr_item_content.sr_item_content_slider_wrapper > div.sr_property_block_main_row > div.sr_item_main_block > div.sr-hotel__title-wrap > h3 > a > span.sr-hotel__name').extract())
    #     # filename =  'acd.html'
    #     # with open(filename, 'wb') as f:
    #     #     f.write(response.body)
    #
    # def parse6(self,response):
    #     print(response.url)
    #     print(response.css('#hprt-table > tbody > tr.hprt-table-cheapest-block.hprt-table-cheapest-block-fix.js-hprt-table-cheapest-block > td.d_pd_hp_price_left_align.hprt-table-cell.hprt-table-cell-price > div > div.prco-wrapper.bui-price-display.prco-sr-default-assembly-wrapper.prc-d-sr-wrapper > div.bui-price-display__value.prco-font16-helper::text').extract)