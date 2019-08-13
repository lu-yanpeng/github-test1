from django.http import HttpResponse

def index(request):
    return HttpResponse('首页')

def login(request):
    return HttpResponse('登录')
