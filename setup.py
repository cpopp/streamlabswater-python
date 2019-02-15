from setuptools import setup

setup(
    name='streamlabswater',
    version='1.0.1',
    packages=['streamlabswater'],
    url='https://github.com/cpopp/streamlabswater-python',
    keywords = ['streamlabs', 'streamlabswater', 'iot', 'water', 'sensor', 'smarthome', 'automation'],
    license='Apache 2.0',
    author='Christopher Popp',
    author_email='christopherpopp@yahoo.com',
    description='Unofficial Python library for the Streamlabs Water API',
    install_requires = ['requests'],
)
