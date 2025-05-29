from setuptools import find_packages
from setuptools import setup

setup(
    name='battery_msg',
    version='0.0.1',
    packages=find_packages(
        include=('battery_msg', 'battery_msg.*')),
)
