from django.http import HttpResponse
import json
from datetime import datetime

import csv

from .models import Environment_monitor

# 读 csv 文件，将其中传感器读出的数据存到数据库中
def csv2db():
    PATH = '/Users/nian/niannian/sjtu/sjtu32/courses/embedded_system/our_project/IS305_SmartFarm_Web/test.csv'
    with open(PATH) as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)[1:]
    for line in data:
        #try:
        test = Environment_monitor(temp = line[0], light_intensity = line[1],
            CO_concentration = line[2], humidity = line[3],
            soil_humidity = line[4], precipitation = line[5],
            year = datetime.now().year, month = datetime.now().month,
            day = datetime.now().day, hour = datetime.now().hour)
        test.save()
        #except:
            #pass

def get_envir_info(request):
    # 删除数据
    # Environment_monitor.objects.filter().delete()
    
    # 调用读取 csv 文件、存入数据库函数
    # csv2db()

    data = {} # data 是一个字典
    # 按写入时间降序读 5 个数据
    content = Environment_monitor.objects.order_by('hour').distinct()
    content = content[:24]
    content = content.values_list\
        ('temp','light_intensity','CO_concentration','humidity',
            'soil_humidity','precipitation', 'year', 'month', 'day', 'hour')
 
    temp, light_intensity, CO_concentration, humidity, soil_humidity,\
        precipitation, year, month, day, hour = list(zip(*content))

    data['temp'] = temp
    data['light_intensity'] = light_intensity
    data['CO_concentration'] = CO_concentration
    data['humidity'] = humidity
    data['soil_humidity'] = soil_humidity
    data['precipitation'] = precipitation
    data['year'] = year
    data['month'] = month
    data['day'] = day
    data['hour'] = hour

    return HttpResponse(json.dumps(data))
