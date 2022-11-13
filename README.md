# TXAPI

轻量级的腾讯云SDK, 同时支持 yunapi2 与 yunapi3, 支持 公有云 / 专有云(租户端&运营端). 

## DEMO

配置文件 config.py
```python
api_domain = "tencentcloudapi.com" # 环境API域名, 公有云为: tencentcloudapi.com
sid = "" # 个人 secret_id
skey = "" # 个人 secret_key
region = "ap-chongqing"
is_debug = True
is_ssl = True
```

示例文件 demo.py
```python
# -*- coding:utf-8 -*-
from api import API
import config

apiv3 = API.v3(
    api_domain=config.api_domain,
    region=config.region,
    secret_id=config.sid,
    secret_key=config.skey,
    debug=config.is_debug,
    ssl=config.is_ssl)

cvm = apiv3.get_client("cvm", "2017-03-12")

params = {
    "Limit": 20,
    "Offset": 1
}

# 请求示例列表(返回为json格式)
rsp = cvm.request("DescribeInstances", params)

```