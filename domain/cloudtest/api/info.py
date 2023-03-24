#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#----------------------------------------------------------------------------
#@File    : info.py
#@Time    : 2023/03/24 06:49:33
#@Author  : Mr. Pan
#@Contact : 523141861@qq.com
#@Version : 0.1
#@Desc    : 
#----------------------------------------------------------------------------


from fastapi import APIRouter

router = APIRouter(prefix="/system")

@router.get("/info")
async def app_info():
    return "hello world"