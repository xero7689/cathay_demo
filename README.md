Cathay Interview Demo Project
---

## Requirements
- python 3.7+
- django 2.1.5
- vue.js 
- axios.js
- boostrap 4.4.1

## Usage
```shell
python manage.py runserver 127.0.0.1:8000
```

F2E
---
For demo the front-end implementation.

## Order API
``` shell
$ curl -L -X GET http://DEMO_HOSTNAME/f2e/orders

{"orders": [{"name": "Livi\u512a\u6d3b \u62bd\u53d6\u5f0f\u885b\u751f\u7d19(100\u62bdx10\u5305x10\u4e32/\u7bb1)", "logo": "https://static.oopocket.com/store/iconTreemall@3x.png", "status": 3, "date": "2018-06-12", "type": "\u5df2\u53d6\u6d88"}, {"name": "BALMUDA The Toaster \u767e\u6155\u9054\u70e4\u9eb5\u5305\u6a5f-\u9ed1\u8272", "logo": "https://static.oopocket.com/store/iconTreemall@3x.png", "status": 2, "date": "2019-07-21", "type": "\u5df2\u6210\u7acb"}, {"name": "\u8d08-\u77ed\u6167\u842c\u7528\u934bHD2133+\u4e09\u5408\u4e00\u6ffe\u7db2\u300cLG\u6a02\u91d1\u300d\u97d3\u570b\u539f\u88dd...", "logo": "https://static.oopocket.com/store/iconTreemall@3x.png", "status": 1, "date": "2019-06-02", "type": "\u8655\u7406\u4e2d"}, {"name": "Apple AirPods 2", "logo": "https://static.oopocket.com/store/iconTreemall@3x.png", "status": 4, "date": "2019-03-02", "type": "\u5df2\u9001\u9054"}]}
```

B2E
---
For demo the URL shortener implementation.

## Base62 Library
### Usage
```python
>>> from b2e.baseX import Base62
>>> base62 = Base62()
>>> base62.encode(123456789)
'8m0Kx'
>>> base62.decode('8m0Kx')
123456789
```
