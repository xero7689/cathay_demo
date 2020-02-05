from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse

import json
from urllib.parse import urlparse
from .models import SubmittedURL
from .baseX import Base62


def b2e(request):
    return render(request, 'b2e.html')


def verify_url(url):
    if not url.startswith('http'):
        return False
    return True


def shortener(request):
    response = {}

    base62 = Base62()
    if request.method == 'POST':

        # Temporarily use json module to load request body
        # Becuase currently unable to override the Content-Type in POST headers
        # while calling axios.post at front-end.
        url = json.loads(request.body)['url']

        # If URL not valid
        if not verify_url(url):
            response['msg'] = 'Not a valid URL'
            return JsonResponse(response)

        parsed_url = urlparse(url)
        surl = SubmittedURL.objects.filter(url=url, host=parsed_url.hostname)
        if not surl:
            surl = SubmittedURL()
            surl.url = url
            surl.host = parsed_url.hostname
            surl.submit_num = 1
            surl.save()
        else:
            surl = surl[0]
            surl.submit_num += 1
            surl.save()
        short_url = base62.encode(surl.id)
        response['short'] = 'b2e/' + short_url
    elif request.method == 'GET':
        print(request.GET)
    return JsonResponse(response)
