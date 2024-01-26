from setuptools import setup, find_packages


setup (
    name='PreProPackage',
    version='0.0.1',
    license='MIT',
    description='code for generate preprocessing in gpr',
    long_description='code generate preprocessing in gpr data, include data syntetic, data field, data in laboratory',
    author='Aplatag',
    packages=find_packages(),
    install_requires = ['math','numpy'],

    url='https://github.com/aplatag/testpackegepy'
)
