from django.http import HttpResponse
from django.shortcuts import render

# 添加的视图文件


def hello(request):
    return HttpResponse("Hello ! I'm django 的 主页!")



def nihao(request):
    return HttpResponse("你好鸭~我是中文区,被你发现了")


def maopao(request):
    # context = {}
    # context['hello'] = 'Hello World!'
    # return render(request, 'maopao.html', context)
    views_list = ["元素1", "元素2", "元素3"]
    return render(request, "maopao.html", {"views_list": views_list})
    # return HttpResponse("你好鸭~我是个冒泡页面,吐了个泡泡就跑!")