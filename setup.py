from setuptools import setup
from setuptools import find_packages

setup(
    name = 'tilesampler',
    version = '0.1.1',
    description = ('Image tile samplers that samples tiles from larger images'
                   'for machine learning'),
    author = ['Wei-Yi Cheng', 'Hidy Chiu'],
    author_email = ['ninpy.weiyi@gmail.com', 'hidy0503@gmail.com'],
    url = 'https://github.com/Hidysabc/tile-sampler',
    license = 'GPLv3',
    install_requires = ['numpy == 1.11.1',
                        'pandas == 0.18.1',
                        'pillow'],
    packages=find_packages()
)

