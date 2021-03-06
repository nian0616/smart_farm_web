from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt  
# Create your views here.

#import face_recognition
import json
import requests
import base64
import cv2

@csrf_exempt

def getPicture(pic_name):#设备摄像函数
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(pic_name,frame)
    cap.release()

def shot_and_search(picture,access_token):#拍照并识别
    picture =  "./FaceRecog/face/tmp/" + picture
    getPicture(picture)
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search" + "?access_token=" + access_token
    headers = {'content-type': 'application/json','Connection':'close'}
    pic = open(picture, "rb")
    pic_base64 = str(base64.b64encode(pic.read()))[2:]
    params = {
        "image":pic_base64,
        "image_type":"BASE64",
        "group_id_list":"normal"
        }
    rp = requests.post(request_url, data=params, headers=headers)
    if rp:
        user_list = rp.json()['result']['user_list']
        max_score = 75
        name = ""
        for user in user_list:
            if user['score'] > max_score:
                max_score = user['score']
                name = user['user_id']
        return name

def Hello(request):
    print('Hello!')
    response = HttpResponse("Hello!", content_type='text/plain')
    return response

def search(picture,access_token):#识别已有图片
    picture =  "./FaceRecog/face/" + picture
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search" + "?access_token=" + access_token
    headers = {'content-type': 'application/json','Connection':'close'}
    pic = open(picture, "rb")
    pic_base64 = str(base64.b64encode(pic.read()))[2:]
    params = {
        "image":pic_base64,
        "image_type":"BASE64",
        "group_id_list":"normal"
        }
    rp = requests.post(request_url, data=params, headers=headers)
    if rp:
        if rp.json()['error_code']:
            return ""
        user_list = rp.json()['result']['user_list']
        max_score = 75
        name = ""
        for user in user_list:
            if user['score'] > max_score:
                max_score = user['score']
                name = user['user_id']
            print(type(user['score']))
        return name

def shot_and_register(name,picture,access_token):#拍照并注册
    picture =  "./FaceRecog/face/" + picture
    getPicture(picture)
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add" + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    pic = open(picture, "rb")
    pic_base64 = str(base64.b64encode(pic.read()))[2:]
    params = {
        "image":pic_base64,
        "image_type":"BASE64",
        "group_id":"normal",
        "user_id":name
        }
    rp = requests.post(request_url, data=params, headers=headers)
    if rp.json()['error_msg'] == "SUCCESS":
        print(pic_base64)
        return pic_base64
    else:
        return ""

def initialize():#初始化人脸库令牌
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=7jkDhGTfRXlgfdl757WdrnGW&client_secret=kHox99d9GF6pNAaGXIwWl7mWvZMvuksb'
    headers = {'Connection':'close'}
    response = requests.get(host, headers = headers)
    if response:
        access_token_tmp = response.json()['access_token']
    else:
        access_token_tmp = ""  
    return access_token_tmp

def login(request):
    token = initialize()
    name = shot_and_search('tmp.jpg',token)
    if name:
        data =[{'value':1}]
    else:
        data =[{'value':0}]
    data = json.dumps(data)
    print(data)
    rpd = HttpResponse(data, content_type='application/json')
    return rpd

def register(request):
    id = request.GET.get('id')
    token = initialize()
    result = shot_and_register(id,"face_r.jpg",token)
    if result:
        data =[{'value':1,"pic":result}]
    else:
        data =[{'value':0,"pic":""}]
    data = json.dumps(data)
    rpd = HttpResponse(data, content_type='application/json')
    return rpd
