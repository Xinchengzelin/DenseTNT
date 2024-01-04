from distutils.core import setup, Extension

import numpy
from Cython.Build import cythonize


# 定义Cython扩展模块, 使用Cython将Python代码编译成C语言扩展模块
setup(
    ext_modules=cythonize(Extension(
        'utils_cython',  # 模块名称
        sources=['utils_cython.pyx'],  # 模块源代码文件
        language='c',  # 编译语言为C
        include_dirs=[numpy.get_include()],  # 包含NumPy头文件路径
        library_dirs=[],  # 库文件路径
        libraries=[],  # 链接的库文件
        extra_compile_args=[],  # 额外的编译参数
        extra_link_args=[]  # 额外的链接参数
    ))
)