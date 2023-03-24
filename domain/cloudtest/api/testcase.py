#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#----------------------------------------------------------------------------
#@File    : testcase.py
#@Time    : 2023/03/23 06:43:41
#@Author  : Mr. Pan
#@Contact : 523141861@qq.com
#@Version : 0.1
#@Desc    : 
#----------------------------------------------------------------------------


from fastapi import APIRouter

router = APIRouter(prefix="/testcase")


@router.get("/info")
async def test_demo():
    return "hello word"