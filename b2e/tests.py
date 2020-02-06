from django.test import TestCase

from urllib.parse import urlparse
from .models import SubmittedURL
from .baseX import Base62

class ShortURLTestCase(TestCase):
    def test_saving_and_retrieving(self):
        url = 'http://www.yahoo.com.tw' 
        parsed_url = urlparse(url)
        surl = SubmittedURL()
        surl.url = url
        surl.host = parsed_url.hostname
        surl.submit_num = 1
        surl.save()

        filter_url = SubmittedURL.objects.filter(url=url, host=parsed_url.hostname)[0]
        self.assertEqual(filter_url.url, url)

class BaseXTestCase(TestCase):
    def setUp(self):
        self.base62 = Base62()

    def test_encode_decode(self):
        print('Test encode 62^N URLs')
        url_id_set = [(i, 62 ** i) for i in range(1, 10)]
        for power, url_id in url_id_set:
            encode_path = self.base62.encode(url_id)
            self.assertEqual(len(encode_path), power+1)
            print('After encoding {}(62^{}), get short path: {}'.format(url_id, power, encode_path))

            decode_url_id = self.base62.decode(encode_path)
            base = round(pow(decode_url_id, 1/power)) 
            self.assertEqual(base, 62)
            print('After decode {}(62^{}), get base {}'.format(encode_path, power, base))

