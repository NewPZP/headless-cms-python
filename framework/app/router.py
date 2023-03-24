#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#----------------------------------------------------------------------------
#@File    : router.py
#@Time    : 2023/03/24 20:42:17
#@Author  : Mr. Pan
#@Contact : 523141861@qq.com
#@Version : 0.1
#@Desc    : 
#----------------------------------------------------------------------------
from fastapi import FastAPI
from domain.cloudtest.api import info
from domain.cloudtest.api import testcase


def router_init(app:FastAPI):
    app.include_router(info.router,responses={404: {"description": "Not found"}})
    app.include_router(testcase.router,responses={404: {"description": "Not found"}})
