import scrapy
import json
from scrapy.http import FormRequest
from scrapy.http import Request
from . import login

class CategorySpider(scrapy.Spider):
    name = 'category'
    allowed_domains = ["dummyjson.com"]

    def start_requests(self):
        token = login.token
        return [Request("http://dummyjson.com/auth/products/categories", method='GET', body=json.dumps(token), 
                          headers={'Content-Type':'application/json'})]

    def parse(self, response):
        print(response.text)
