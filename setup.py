from setuptools import setup, find_packages

setup(
    name='django-google-search',
    version='1.0',
    author='Ryan Bagwell',
    author_email='ryan@ryanbagwell.com',
    packages=find_packages(),
    package_data={
        'googlesearch': ['templates/*.*', 'templatetags/*.*'],
    },
    include_package_data=True,
    url='https://github.com/hzdg/django-google-search',
    license='license.txt',
    description='A interface to use Google Custom Search in Django templates',
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.3",
        "requests >= 2.0",
        "google-api-python-client == 1.2",
    ],
)
