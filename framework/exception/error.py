#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#----------------------------------------------------------------------------
#@File    : error.py
#@Time    : 2023/03/23 06:55:44
#@Author  : Mr. Pan
#@Contact : 523141861@qq.com
#@Version : 0.1
#@Desc    : 
#----------------------------------------------------------------------------

class AuthError(Exception):
    """user authorization error
    """


class CaseParametersError(Exception):
    """extract parameters error
    """


class ParamsError(ValueError):
    """request params error
    """


class RedisError(Exception):
    """redis error
    """


class RpcError(Exception):
    """rpc error
    """
