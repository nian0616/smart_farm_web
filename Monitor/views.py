from django.http import HttpResponse
import json
from datetime import datetime

from .models import Monitor_video, Environment_monitor, Crop_maturity

def get_videos(request):

    data = {} # data 是一个字典
    # 按写入时间降序读 8 个数据的时间、价格、变动率
    content = Price.objects.order_by('-pub_time')[:8].values_list\
        ('name','price','change_num','change_ratio','trading_volumes')
    name, price, change_num, change_ratio, trading_volumes= list(zip(*content))

    data['name'] = name
    data['price'] = price
    data['change_num'] = change_num
    data['change_ratio'] = change_ratio
    data['trading_volumes'] = trading_volumes
    return HttpResponse(json.dumps(data))

def get_envir_info(request):
    saving_data()

    data = {} # data 是一个字典
    # 按写入时间降序读 8 个数据的时间、价格、变动率
    content = Price.objects.order_by('-pub_time')[:8].values_list\
        ('name','price','change_num','change_ratio','trading_volumes')
    name, price, change_num, change_ratio, trading_volumes= list(zip(*content))

    data['name'] = name
    data['price'] = price
    data['change_num'] = change_num
    data['change_ratio'] = change_ratio
    data['trading_volumes'] = trading_volumes
    return HttpResponse(json.dumps(data))

def get_crop_maturity(request):
    saving_data()

    data = {} # data 是一个字典
    # 按写入时间降序读 8 个数据的时间、价格、变动率
    content = Price.objects.order_by('-pub_time')[:8].values_list\
        ('name','price','change_num','change_ratio','trading_volumes')
    name, price, change_num, change_ratio, trading_volumes= list(zip(*content))

    data['name'] = name
    data['price'] = price
    data['change_num'] = change_num
    data['change_ratio'] = change_ratio
    data['trading_volumes'] = trading_volumes
    return HttpResponse(json.dumps(data))
