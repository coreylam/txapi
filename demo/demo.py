# -*- coding:utf-8 -*-

# 调用云API2
from apiclient.api2 import Api2Client

api_domain = "api2.xxx.cn"
sid = ""
skey = ""
client = Api2Client()
client.set_ssl(False)
client.debug = True
client.set_domain(api_domain)
client.set_region("shanghai")
client.set_secret(sid, skey)
client.switch_module("cam")
client.request("GetAllSubUser", {})

# 调用云API3
from apiclient.api3 import Api3Client

api_domain = "api3.yf-m17.tcecqpoc.fsphere.cn"
sid = ""
skey = ""
client = Api3Client()
client.debug = True
client.set_domain(api_domain)
client.set_ssl(False)
client.set_region("shanghai")
client.set_secret(sid, skey)
client.set_version("cvm", "2017-03-12")
client.switch_module("cvm")
client.request("DescribeInstances", {"Limit": 1})
