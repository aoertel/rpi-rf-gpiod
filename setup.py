from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='rpi-rf-gpiod',
    version='0.1.0',
    author='Andy Oertel',
    author_email='oertelandy@gmail.com',
    description='Sending and receiving 433/315MHz signals with low-cost GPIO RF modules on a Raspberry Pi accessed with gpiod',
    long_description=long_description,
    url='https://github.com/aoertel/rpi-rf-gpiod',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=[
        'rpi',
        'raspberry',
        'raspberry pi',
        'rf',
        'gpio',
        'radio',
        '433',
        '433mhz',
        '315',
        '315mhz',
        'gpiod',
        'libgpiod',
        'libgpiod-python'
    ],
    install_requires=[''],
    scripts=['scripts/rpi-rf_send', 'scripts/rpi-rf_receive'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)
