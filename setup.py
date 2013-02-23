from distutils.core import setup

setup(
    name='Django Google Search',
    version='0.1.0',
    author='Ryan Bagwell',
    author_email='ryan@ryanbagwell.com',
    packages=['googlesearch',],
    url='https://github.com/ryanbagwell/django-cms-nivo-slider',
    license='license.txt',
    description='A interface to use Google Custom Search in Django templates',
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.4",
        "requests >= 1.1.0",
    ],
)