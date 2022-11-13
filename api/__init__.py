# -*- coding:utf -*-
from .api2 import Api2Client
from .api3 import Api3Client


class API(object):
    v2 = Api2Client
    v3 = Api3Client
