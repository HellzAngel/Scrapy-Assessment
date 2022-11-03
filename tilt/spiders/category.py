import scrapy
from .login import json,LoginSpider
from scrapy.http import FormRequest
from scrapy.http import Request

class CategorySpider(LoginSpider):
    name = 'category'
    allowed_domains = ['dummyjson.com']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        LoginSpider.start_requests(self)

    def parseToken(self, response):
        token = json.loads(response.text)['token']
        print("Auth Token: ",token)
        headers= {
        'Authorization': 'Bearer', 
        'Content-Type': 'application/json'
        }
        headers['Authorization'] = 'Bearer '+token
        return [Request("http://dummyjson.com/auth/products/categories", method='GET', 
                          headers=headers,callback=self.parseProduct,meta={'token': token})]
