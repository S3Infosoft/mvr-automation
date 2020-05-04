import scrapy


class Mvr1Spider(scrapy.Spider):
    name = 'mvr1'
    allowed_domains = ['www.makemytrip.com']
    start_urls = ['http://www.makemytrip.com/']

    @classmethod
    def parse(self,response):
        checkin = '30/05/2020'
        checkout = '31/05/2020'
        self.checkin_monthday, self.checkin_month, self.checkin_year = checkin.split('/')
        self.checkout_monthday, self.checkout_month, self.checkout_year = checkout.split('/')
        search_text = "Ganpatipule"
        url="https://www.makemytrip.com/hotels/hotel-listing/?checkin=" + self.checkin_month + self.checkin_monthday + self.checkin_year +"&checkout=" + self.checkout_month + self.checkout_monthday + self.checkout_year + "&city=XGP&country=IN&searchText=" + search_text +"%2C%20India&roomStayQualifier=2e0e"
        yield scrapy.Request(url=url,callback=self.parse1)


    def parse1(self,response):
        print(response.url)

