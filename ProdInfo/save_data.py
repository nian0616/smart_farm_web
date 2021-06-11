from .craw_products_prices import main
from .models import Price
from datetime import datetime

def saving_data():
    # delete all data
    Price.objects.all().delete()

    products_list = main()[1:] # 剔除表头

    for prod in products_list:
        # prod[3] 涨跌率，字符串类型，去掉最后的百分号后变为浮点数
        # prod[3][:-1] 有可能是“-”（prod[3]涨跌率是--，表示没有变化）
        try:
            test = Price(name = prod[0], price = prod[1], change_num = prod[2], change_ratio = \
                float(prod[3][:-1]), trading_volumes = prod[-3], pub_time = datetime.now())
            test.save()
        except:
            pass

