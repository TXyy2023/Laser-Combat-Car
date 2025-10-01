## Laser-Combat-Car
## 项目介绍

本项目是 **第十五届全国大学生光电设计竞赛** 的参赛作品，整体设计由 **Maixcam Pro** 与 **ESP8266** 协同完成：

- **ESP8266**：负责小车底盘的移动与基本控制。  
- **Maixcam Pro**：运行经过裁剪优化的 **YOLO v11 模型**，实现目标小车的识别与打击。同时通过 PID 控制二维云台，让摄像头能够精准对准目标。

### 系统主流程
1. 上电 → ESP8266 与 Maixcam Pro 启动  
2. Maixcam Pro 开始目标识别（无串口指令时不驱动云台）  
3. ESP8266 控制小车移动至预期位置并停止  
4. ESP8266 发送串口指令 → 激光启动  
5. Maixcam Pro 通过 PID 控制二维云台，调整摄像头对准目标  
6. 激光持续照射目标 **2 秒**  
7. Maixcam Pro 触发喇叭与 LED → 判定胜利




/maix-first_try-v1.0.3下是Maixcam pro端代码
/run_code是8266端代码
## BOM 表
| 序号 | 名称                       | 规格                                                                | 数量 | 价格 | 备注                                          | 链接                                                                                                                                                                                                                                                                                                     |
| :--- | :------------------------- | :------------------------------------------------------------------ | :--- | :--- | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Maixcam pro                | CAM Pro(含电池) 内置镜像卡                                          | 1    | 596  | 作为AI摄像头                                  | https://item.taobao.com/item.htm?id=846226367137                                                                                                                                                                                                                                                         |
| 2    | TB6612 FNG双路电机驱动模块 | 【焊接排针】TB6612双路驱动模块带稳压版【多仓发货 大部分区域次日达】 | 1    | 42   | 作为减速电机驱动板                            | https://detail.tmall.com/item.htm?id=645944642035&mi_id=0000f1McOXaTAUkE5JDB20mGM-qJVSsq2O8KxCeTOCk2usU&pvid=00aae127-ba56-418c-b5e4-3ec6f692cf67&scm=1007.56608.446695.0&skuId=5621113741702&spm=tbpc.boughtlist.repurchaseitem.d1.5cef2e8dZtWixR&xxc=home_recommend                                    |
| 3    | 小车开发板底盘             | 底盘不带控制板                                                      | 1    | 245  | 作为小车底盘                                  | https://item.taobao.com/item.htm?id=570479397628&mi_id=00002yqogRWefo-oNQjrTm4M49fsv2VXGY_UOL5syoeOpyw&spm=tbpc.boughtlist.suborder_itemtitle.1.5cef2e8dZtWixR                                                                                                                                           |
| 4    | 二维电动云台               | 简易二维云台（20kg总线舵机）;不含控制系统                           | 1    | 180  | 作为相机的二维云台，用于让Maixcam跟踪目标对象 | https://item.taobao.com/item.htm?id=630117220008&mi_id=0000gTzzBcdKS4MFVyfpOmWshXzpD-kiKADwrVg5lynEb6g&spm=tbpc.boughtlist.suborder_itemtitle.1.5cef2e8dZtWixR                                                                                                                                           |
| 5    | 舵机驱动板                 | USB/TTL调试板（送数据线）                                           | 1    | 22   | 二维云台的驱动板                              | https://item.taobao.com/item.htm?id=586685736957&mi_id=0000oujnpDKLfuJhgV55Dw1YRFroumJs9RTw3B17eteYqSs&spm=tbpc.boughtlist.suborder_itemtitle.1.5cef2e8dZtWixR&skuId=5195518882317                                                                                                                       |
| 6    | 12V电源                    | 12V 2550mAh安全电池E326S(亿纬锂能电芯)+拓展线束包+带3C认证1A充电器  | 1    | 79   | 作为小车的总电源                              | https://detail.tmall.com/item.htm?abbucket=20&id=657166348854&mi_id=0000XqU-Gny9iq1mm1EaAtD8lPM9cLevDBZTkSlmNZ2qpMg&ns=1&priceTId=2150462a17592978510598481e0e72&skuId=4978132892219&spm=a21n57.1.hoverItem.6&utparam=%7B%22aplus_abtest%22%3A%227b368999d4d3e49b422cefe85e9a4975%22%7D&xxc=taobaoSearch |
|      |                            |                                                                     |      |      |                                               |                                                                                                                                                                                                                                                                                                          |
|      |                            |                                                                     |      |      |                                               |                                                                                                                                                                                                                                                                                                          |


## img


[光电比赛官方规则](第十三届全国大学生光电设计竞赛实物赛道竞赛细则.pdf)
摄像头识别
![alt text](src/04A69053-9495-4C08-8720-63DD393E2D64_1_102_o.jpeg)


小车底盘
![alt text](src/C3077A71-F4A0-4F1E-B0C5-1DED945E0B38_1_102_o.jpeg)


pid图像识别
<video controls src="src/db1c7a538065c3b661300650d142a9ff.mov" title="Title"></video>

小车运行效果（早期）
<video controls src="src/IMG_9369.MOV" title="Title"></video>
最终小车形态

<img src="src/C86D8E6F-29C2-4FA4-9D24-F5771092EAC3_1_102_o.jpeg" alt="摄像头识别" width="20" />



## 缺陷
- [x] STM32F103C8T6 （1个）
- [ ] 10kΩ 电阻（10个）
- [ ] 100nF 电容（5个）