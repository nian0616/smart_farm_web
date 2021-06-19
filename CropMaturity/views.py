from django.shortcuts import render
from django.http import HttpResponse
import zipfile
from .test_maturity import get_maturity_rate
import numpy as np
import glob
from django.views.decorators.csrf import csrf_exempt  

@csrf_exempt

def upload(request):
    '''
    上传压缩文件并保存到Data目录下，并解压缩
    '''
    file_list = request.FILES.getlist('file')
    file = file_list[0]
    img_dir = "./CropMaturity/Data/test_images.zip"
    data = file.file.read()

    with open(img_dir, 'wb') as f:
        f.write(data)
    
    with zipfile.ZipFile(img_dir) as zf:
        zf.extractall("./CropMaturity/Data")
    
    return HttpResponse("Upload Success")

    
def test_maturity(request):
    '''
    根据图片检测作物成熟度，并返回给前端
    '''
    maturity_rate = get_maturity_rate("./CropMaturity/Data")
    maturity_rate = np.round(100*maturity_rate,2)

    return HttpResponse(maturity_rate)
