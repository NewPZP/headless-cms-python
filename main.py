#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#----------------------------------------------------------------------------
#@File    : main.py
#@Time    : 2023/03/24 06:25:19
#@Author  : Mr. Pan
#@Contact : 523141861@qq.com
#@Version : 0.1
#@Desc    : 
#----------------------------------------------------------------------------
import uvicorn

from framework.app.app import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8001,
        debug=False,
        reload=True,
    )