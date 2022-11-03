import scrapy
from .category import json,CategorySpider
from scrapy.http import FormRequest
from scrapy.http import Request

class ProductSpider(CategorySpider):
    name = 'product'
    allowed_domains = ['dummyjson.com']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        CategorySpider.__init__(self)

    def parseProduct(self, response):
        categories = json.loads(response.text)
        token = response.meta.get('token') 
        print("Categories:")
        print()
        print(categories)
        headers= {
        'Authorization': 'Bearer', 
        'Content-Type': 'application/json'
        }
        headers['Authorization'] = 'Bearer '+token
        for category in categories:
            yield Request("http://dummyjson.com/auth/products/category/"+category, method='GET', 
                          headers=headers, callback=self.parseList)

    def parseList(self, response):
        print(response.text)



