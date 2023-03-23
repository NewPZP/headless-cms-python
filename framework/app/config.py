
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#----------------------------------------------------------------------------
#@File    : config.py
#@Time    : 2023/03/24 07:13:48
#@Author  : Mr. Pan
#@Contact : 523141861@qq.com
#@Version : 0.1
#@Desc    : 
#----------------------------------------------------------------------------
from pydantic import BaseSettings
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

class BaseConfig(BaseSettings):
    pass
   