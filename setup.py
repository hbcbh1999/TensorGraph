from distutils.core import setup
from setuptools import find_packages
# from .tensorgraph import __version__
# __version__ = '4.4.3'
import json

with open('./tensorgraph/pkg_info.json') as fp:
    _info = json.load(fp)
__version__ = _info['version']

setup(
    name='tensorgraph',
    version=__version__,
    author='Wu Zhen Zhou',
    author_email='hyciswu@gmail.com',
    install_requires=['numpy>=1.7.1',
                      'six>=1.9.0',
                      'scikit-learn>=0.17',
                      'pandas>=0.17',
                      'scipy>=0.17',
                      'tensorflow-gpu>=1.2.1'],
    url='https://github.com/hycis/TensorGraph',
    download_url = 'https://github.com/hycis/TensorGraph/tarball/{}'.format(__version__),
    license='Apache 2.0, see LICENCE',
    description='A high level tensorflow library for building deep learning models',
    long_description=open('README.md').read(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True
)
