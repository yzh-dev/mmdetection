# %%
from mmcv import Config

cfg = Config.fromfile('test.py')
print(cfg)

# %%
# 对于所有格式的配置文件，都支持一些预定义变量。它会将 {{ var }} 替换为实际值。
#
# 目前支持以下四个预定义变量：
#
# {{ fileDirname }} - 当前打开文件的目录名，例如 /home/your-username/your-project/folder
#
# {{ fileBasename }} - 当前打开文件的文件名，例如 file.ext
#
# {{ fileBasenameNoExtension }} - 当前打开文件不包含扩展名的文件名，例如 file
#
# {{ fileExtname }} - 当前打开文件的扩展名，例如 .ext
cfg = Config.fromfile('./config_a.py')
print(cfg)

# %%
# 不含重复键值对从基类配置文件继承
cfg = Config.fromfile('./config_b.py')
print(cfg)
# %%
# 含重复键值对从基类配置文件继承
# 在基类配置文件：config_a 里的 b.b2=None被配置文件：config_c.py里的 b.b2=1替代
cfg = Config.fromfile('./config_c.py')
print(cfg)

# %%
# 从具有忽略字段的配置文件继承
cfg = Config.fromfile('./config_d.py')
print(cfg)

# %%
# 从多个基类配置文件继承（基类配置文件不应包含相同的键）
cfg = Config.fromfile('./config_f.py')
print(cfg)

# %%
# 从基类引用变量
cfg = Config.fromfile('./config_g.py')
print(cfg)


