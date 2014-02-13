from distutils.core import setup

setup(
    name='django-google-search',
    version='1.0',
    author='Ryan Bagwell',
    author_email='ryan@ryanbagwell.com',
    packages=['googlesearch'],
    url='https://github.com/hzdg/django-google-search',
    license='license.txt',
    description='A interface to use Google Custom Search in Django templates',
    long_description=open('README.rst').read(),
    include_package_data=True,
    install_requires=[
        "Django >= 1.3",
        "requests >= 2.0",
        "google-api-python-client == 1.2",
    ],
)
