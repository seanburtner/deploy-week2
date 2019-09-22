from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Hello, world!</body></html>"
    return HttpResponse(html)