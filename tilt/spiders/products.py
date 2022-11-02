import scrapy
import json
from scrapy.http import FormRequest
from scrapy.http import Request
from . import category

class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['dummyjson.com']

    def start_requests(self):
        # token = login.token
        return [Request("http://dummyjson.com/auth/products", method='GET', body=json.dumps(token), 
                          headers={'Content-Type':'application/json'})]

    def parse(self, response):
        print(response.text)