#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#----------------------------------------------------------------------------
#@File    : user.py
#@Time    : 2023/03/23 06:52:13
#@Author  : Mr. Pan
#@Contact : 523141861@qq.com
#@Version : 0.1
#@Desc    : 
#----------------------------------------------------------------------------
from pydantic import BaseModel, validator
from framework.exception import ParamsError

class UserDto(BaseModel):
    name: str
    password: str
    username: str
    email: str

    @validator('name', 'password', 'username', 'email')
    def field_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ParamsError("不能为空")
        return v
    
    
class UserLoginForm(BaseModel):
    username: str
    password: str

    @validator('password', 'username')
    def name_not_empty(cls, v):
        pass