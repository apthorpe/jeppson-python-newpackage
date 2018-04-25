from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='jeppson',
    version='0.0.1',
    author='Bob Apthorpe',
    author_email='bob.apthorpe@gmail.com',
    packages=find_packages(exclude=['docs']),
    url='https://github.com/apthorpe/jeppson-python',
    license='MIT',
    description='Pipe network flow analysis toolkit',
    long_description=long_description,
    install_requires=[
    ]
)
