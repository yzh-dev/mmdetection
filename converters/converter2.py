# converter2.py
from .builder import CONVERTERS
from .converter1 import Converter1

# 使用注册器管理模块
@CONVERTERS.register_module()
def converter2(a, b):
    return Converter1(a, b)