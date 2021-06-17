# IS305_SmartFarm_Web
## Introduction
Code for IS305: Application Software Course Design (SJTU，2021 Spring).
A smart farm platform combining **Web** and **Embedded System**.

## Getting started
```shell
# 前端
# first download and install node.js
# enter the project directory
cd fronted

# install dependency
npm install

# develop
npm run dev

# 后端
python manage.py runserver
```

## 绕过人脸识别登录
在 **/frontend/src/views/login/index.vue#Line268** 注释掉 fun2 并添加 facetoken = 1:
```python
// fun2
facetoken = 1
```
