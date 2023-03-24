#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#----------------------------------------------------------------------------
#@File    : app.py
#@Time    : 2023/03/24 06:57:13
#@Author  : Mr. Pan
#@Contact : 523141861@qq.com
#@Version : 0.1
#@Desc    : 
#----------------------------------------------------------------------------
from fastapi import FastAPI
from .log import log_init
from .router import router_init

def create_app() -> FastAPI:
    app = FastAPI(title="Headless CMS",
                  description="内容管理",
                  version="1.0.0",
                  )

    # 初始化日志
    log_init()

    # # 加载配置
    # conf_init(app)

    # # 初始化路由配置
    router_init(app)

    # # 初始化中间件
    # middleware_init(app)

    # # 建表
    # db_init(app)

    return app