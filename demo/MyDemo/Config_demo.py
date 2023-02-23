# %%
# https://zhuanlan.zhihu.com/p/346203167
# MMCV 核心组件分析(四): Config
from mmcv import  Config
# 1.1 通过 dict 生成 config
cfg = Config(dict(a=1, b=dict(b1=[0, 1])))
# 可以通过 .属性方式访问，比较方便
cfg.b.b1 # [0, 1]
# %%
# 1.2 通过配置文件生成 config
cfg = Config.fromfile('../../tests/data/configs_mmtrack/faster_rcnn_r50_dc5.py')
cfg.filename
# %%


# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

