# -*- coding:utf-8 -*-
# @time : 2019.12.02
# @IDE : pycharm
# @author : wangzhebufangqi
# @github : https://github.com/wangzhebufangqi

import torch
from torchvision import datasets, models, transforms
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import time
import numpy as np
import matplotlib.pyplot as plt
from .network import resnet50


def get_maturity_rate(valid_directory="./test"):

    test_valid_transforms = transforms.Compose(
            [transforms.Resize([224,224]),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406],
            [0.229, 0.224, 0.225])])

    batch_size = 8
    num_classes = 1

    # 读取需要测试的图片文件
    valid_datasets = datasets.ImageFolder(valid_directory,transform=test_valid_transforms)
    valid_data_size = len(valid_datasets)
    valid_data = torch.utils.data.DataLoader(valid_datasets, batch_size=batch_size, shuffle=False)

    # 初始化网络
    resnet152 = resnet50(pretrained=True)
    for param in resnet152.parameters():
        param.requires_grad = False

    fc_inputs = resnet152.fc.in_features
    resnet152.fc = nn.Sequential(
        nn.Linear(fc_inputs, 1024),
        nn.ReLU(),
        nn.Dropout(0.4),
        nn.Linear(1024, 2),
        nn.LogSoftmax(dim=1)
    )

    # 导入预先训练好的模型
    ckpt = torch.load("./CropMaturity/trained_models/26.pth", map_location=torch.device('cpu'))
    resnet152.load_state_dict(ckpt)
    
    model = resnet152
    device =  torch.device("cuda:0" if torch.cuda.is_available() else "cpu")#若有gpu可用则用gpu
    model.eval()

    # 根据结果，计算成熟率
    maturity = []

    for j, (inputs, labels) in enumerate(valid_data):
        inputs = inputs.to(device)
        labels = labels.to(device)
        model = model.to(device)
        outputs = model(inputs)

        ret, predictions = torch.max(outputs.data, 1)
        maturity.extend(predictions)

    maturity = np.array(maturity)
    maturity_rate = np.sum(maturity)/len(maturity)

    return maturity_rate