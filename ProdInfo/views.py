from django.http import HttpResponse
import json
import csv
import os

from .models import Price

from .save_data import saving_data
from django.views.decorators.csrf import csrf_exempt  

@csrf_exempt

def get_data(request):
    saving_data()

    data = {} # data 是一个字典
    # 按写入时间降序读 8 个数据的时间、价格、变动率
    content = Price.objects.order_by('-pub_time')[:12].values_list\
        ('name','price','change_num','change_ratio','trading_volumes')
    name, price, change_num, change_ratio, trading_volumes= list(zip(*content))

    data['name'] = name
    data['price'] = price
    data['change_num'] = change_num
    data['change_ratio'] = change_ratio
    data['trading_volumes'] = trading_volumes
    return HttpResponse(json.dumps(data))


def get_position(request):
    # GPS定位模块将小车位置信息通过WIFI通信传输至上位机，存储格式为txt文件
    # 后端读取txt文件，整合信息返回至前端，显示在页面上

    res = []

    f = open('./ProdInfo/vehicle.txt','r')
    for idx,line in enumerate(f.readlines()[1:]):
        info = line.split(' ')
        cur = {"lng":float(info[0]), "lat":float(info[1])} # 经纬度数值

        # 无人车运行状态
        if(int(info[2].strip('\n'))==0):
            cur["value"] = "无人车%d，运行状态良好"%(idx+1)
        else:
            cur["value"] = "无人车%d，运行状态异常"%(idx+1)
        res.append(cur)

    return HttpResponse(json.dumps(res))