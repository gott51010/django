from django.http import HttpResponse

# 添加的视图文件


def hello(request):
    return HttpResponse("Hello ! I'm django 的 主页!")



def nihao(request):
    return HttpResponse("你好鸭~我是中文区,被你发现了")