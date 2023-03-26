#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#----------------------------------------------------------------------------
#@File    : user.py
#@Time    : 2023/03/23 06:36:25
#@Author  : Mr. Pan
#@Contact : 523141861@qq.com
#@Version : 0.1
#@Desc    : 
#----------------------------------------------------------------------------
from schema.user import UserDto, UserLoginForm


from fastapi import APIRouter, Depends

router = APIRouter(prefix="/auth")

@router.post("/register")
async def register(user: UserDto):
    pass
 
 
@router.post("/login")
async def login(data: UserLoginForm):
    pass

@router.get("/github/login")
async def login_with_github(code: str):
    pass


@router.get("/query")
async def query_user_info(token: str):
    pass


# @router.get("/delete")
# async def delete_user(id: int, user=Depends(Permission(Config.ADMIN))):
#     pass