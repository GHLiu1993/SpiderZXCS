# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# useful for handling different item types with a single interface
from fake_useragent import UserAgent
import requests,json
import datetime

class RandomUserAgentMiddlware(object):

    def __init__(self,crawler):
        super(RandomUserAgentMiddlware,self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE','random')

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)

    def process_request(self,request,spider):
        def get_ua():
            return getattr(self.ua,self.ua_type)

        request.headers.setdefault('User_Agent',get_ua())


class ZxcsspiderProxyIPDownloadMiddleware(object):
    def __init__(self):
        self.url = '代理IP的API'
        self.proxy = ''
        self.expire_datetime = datetime.datetime.now() - datetime.timedelta(minutes=4)
        self._get_proxyip()

    def _get_proxyip(self):
        resp = requests.get(self.url)
        info = json.loads(resp.text)
        proxy = info['data'][0]
        self.proxy = proxy['ip']
        self.expire_datetime = datetime.datetime.now() + datetime.timedelta(minutes=4)

    def _check_expire(self):
        if datetime.datetime.now() >= self.expire_datetime:
            self._get_proxyip()

    def process_request(self,spider,request):
        self._check_expire()
        request.meta['proxyip'] ='http://' +  self.proxy
