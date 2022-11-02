import scrapy
import json
from scrapy.http import FormRequest
from scrapy.http import Request


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["dummyjson.com"]

    def start_requests(self):
        auth_data = {'username': f'{self.username}', 'password': f'{self.password}'}
        return [Request("http://dummyjson.com/auth/login", method='POST', body=json.dumps(auth_data), 
                          headers={'Content-Type':'application/json'})]

    def parse(self, response):
        print(response.text)