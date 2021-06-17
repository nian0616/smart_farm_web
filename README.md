# Web for our project of IS305
## Introduction
Web of our project for IS305: Application Software Course Design (SJTU，2021 Spring).

## Getting started
```shell
# 如 PC 上没有 node.js 需先安装

# 第一次启动前端需要安装 node.js 依赖包
cd fronted
npm install

# 启动前端
npm run dev

# 启动后端
python manage.py runserver
```

## 绕过人脸识别登录
在 **/frontend/src/views/login/index.vue#Line268** 注释掉 fun2 并添加 facetoken = 1:
```python
// fun2
facetoken = 1
```
