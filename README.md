<!--
 * @Author: wuqianying
 * @Date: 2022-10-29 11:21:47
 * @LastEditors: wuqianying
 * @LastEditTime: 2022-11-05 01:19:17
-->

# 2022 按照最新的 python3.10 elasticsearch7.4.0 重写。

# weapp-zhihulive

基于 Zhihu Live 数据的微信小程序.数据归知乎所有，本项目用于技术学习

## Preview

![设计图](./screenshot/zhihulive.png)

如果在 wifi 情况下或者土豪不介意流量的同学可以直接[感受实际使用的动态效果](./screenshot/zhihulive.gif)

## Getting started

本项目包含服务端和微信小程序全部源代码：

```python
❯ git clone https://github.com/dongweiming/weapp-zhihulive
❯ cd weapp-zhihulive
❯ tree -L 1
.
├── App # 小程序代码
├── LICENSE
├── README.md
├── Server  # 服务端+爬虫代码
├── screenshot # 设计图和动态效果
```

启动服务端：

```python
❯ cd Server
❯ python3 -m venv venv3 --system-site-packages
❯ source venv3/bin/activate
❯ python3 -m pip install -r requirements.txt
# 配置MySQL和Elasticsearch
❯ python crawl.py  # 运行爬虫获取全部Live数据
❯ python app.py  # 启动API服务
```

运行小程序：

1. [下载并安装小程序开发工具](https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html)
2. 启动开发工具，添加项目，目录为 App
