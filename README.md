# IS305课程设计：智能农业物联网系统
## 简介
这是SJTU IS305（应用软件课程设计）大作业的网页部分。

项目设计了一个模拟的智能农业物联网系统，总体结构如下所示：

<img src=".\img\overview.png" alt="overview" style="zoom:48%;" />

项目实现了用户友好、功能齐全的软件界面，作为农场的核心控制平台，辅助管理员对农场的管理工作。软件以网页的形式实现，前端基于vue.js框架实现，为用户提供了易于交互的接口；后端基于django实现，实现了相应功能并支持sqlite3数据库操作。

软件功能模块的核心是大棚监控模块，由大棚场景监控模块、大棚环境监测模块、无人车管理模块和农作物管理模块这4部分组成。管理员登录系统后，可以便捷地浏览整个大棚的情况。同时，网页还提供了辅助管理模块，由人脸识别登录模块、行业动态浏览模块和工人排班模块组成，以辅助管理农场。

## 功能实现与界面展示

<img src=".\img\1.png" alt="1" style="zoom:30%;" />

<img src=".\img\2.png" alt="2" style="zoom:30%;" />

<img src=".\img\3.png" alt="3" style="zoom:30%;" />

<img src=".\img\4.PNG" alt="4" style="zoom:30%;" />

<img src=".\img\5.png" alt="5" style="zoom:30%;" />

<img src=".\img\6.png" alt="6" style="zoom:30%;" />

<img src=".\img\7.PNG" alt="7" style="zoom:30%;" />

## 运行步骤

后端实现基于`python3.6`和`Django2.2`，安装必要的依赖包：

```
pip install -r requirements.txt
```

前端基于`vue.js 2.6.10`实现：

```shell
# 第一次启动前端需要安装 node.js 依赖包
cd fronted
npm install
```

运行网页：

```bash
# 启动前端，然后在浏览器访问本地端口
npm run dev

# 启动后端
python manage.py runserver
```

注：如设备受限需要绕过人脸识别登录，在 **/frontend/src/views/login/index.vue#Line177** 注释掉 fun2 并添加 facetoken = 1:

```python
// fun2()
facetoken = 1
```

## 项目结构

```
|-backend # 后端配置文件，包括setting、urls等
|-CropMaturity # 作物成熟度检测，后端功能
  |-views.py # 后端功能入口函数
  |-test_maturity.py # 检测功能函数
  |-trained_models # 预训练模型
  |-network # 深度学习网络
|-FaceRecog # 人脸识别登录，后端功能
|-ProdInfo # 处理大棚环境和行业动态的前后端交互和数据库操作
  |-craw_products_prices # 利用爬虫获取行业动态数据
|-frontend #前端
  |-App.vue #前端界面入口
  |-public
  	|-index.html # 前端页面入口
  |-src
  	|-router # 页面路由
  	|-views 
  	  |-crops # 作物成熟度检测
  	  |-documentation # 行业动态
  	  |-greenhouse # 大棚环境
  	  |-login #登录
  	  |-monitor #大棚监控
  	  |-peoples # 工人排班
  	  |-vehicle # 无人车监控
 |-manage.py

```

## 小组分工与进度安排

小组分工：

| 姓名   | 主要工作                                                     | github账号    |
| ------ | ------------------------------------------------------------ | ------------- |
| 吴小茜 | 循迹小车代码实现，小车与本地机通信，前端页面实现，文档撰写   | enlighten0707 |
| 王轶凡 | 部分传感器功能实现，作物成熟识别模块，文档撰写与整理，demo录制 | wyfzka        |
| 郑幸锴 | 机械臂拼装，机械臂控制，人脸登录验证，文档撰写               | jdxccz        |
| 李思源 | 小车拼装，国际农产品价格爬取展示，数据库交互，文档撰写       | nian0616      |
| 邱祚雨 | 部分传感器功能实现，摄像头实现，工人排班实现，文档撰写       | Chill_Zoe     |

进度安排：

| 工作                               | 日期      |
| ---------------------------------- | --------- |
| 可移动小车拼装与代码实现           | 4.1-4.20  |
| 摄像头部署，中控端监测完成         | 4.15-4.30 |
| 中控端与PC机通信，网页端展示       | 5.1-5.10  |
| 网页端其他辅助功能完成             | 5.7-5.15  |
| 人脸验证等非需求功能实现，代码整合 | 5.20-5.30 |
| 项目测试，报告、文件整理           | 6.1-6.18  |