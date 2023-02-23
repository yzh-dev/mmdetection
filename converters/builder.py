from mmcv.utils import Registry
# 创建转换器（converter）的注册器（registry）
CONVERTERS = Registry('converter')


converter1_cfg = dict(type='Converter1', a=1, b=2)
converter2_cfg = dict(type='converter2', a=11, b=22)
converter1 = CONVERTERS.build(converter1_cfg)
# returns the calling result
result = CONVERTERS.build(converter2_cfg)
value = 10