from django.test import TestCase

from urllib.parse import urlparse
from .models import SubmittedURL

class ShortURLTestCase(TestCase):
    def test_saving_and_retrieving(self):
        url = 'http://www.yahoo.com.tw' 
        parsed_url = urlparse(url)
        surl = SubmittedURL()
        surl.url = url
        surl.host = parsed_url.hostname
        surl.submit_num = 1
        surl.save()

        print(surl.id)
        print(SubmittedURL.objects.filter(url=url, host=parsed_url.hostname))

