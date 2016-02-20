"""
The setup package to install the SeleniumBase Test Framework plugins
"""

from setuptools import setup, find_packages  # noqa

setup(
    name='seleniumbase',
    version='1.1.31',
    url='http://seleniumbase.com',
    author='Michael Mintz',
    author_email='@mintzworld',
    maintainer='Michael Mintz',
    description='Reliable Browser Automation - http://seleniumbase.com',
    license='The MIT License',
    install_requires=[
        'selenium==2.52.0',
        'nose==1.3.7',
        'pytest==2.8.7',
        'flake8==2.5.4',
        'requests==2.9.1',
        'urllib3==1.14',
        'BeautifulSoup==3.2.1',
        'unittest2==1.1.0',
        'chardet==2.3.0',
        'simplejson==3.8.2',
        'boto==2.39.0',
        'ipdb==0.8.1',
        'pyvirtualdisplay==0.1.5',
        ],
    packages=['seleniumbase',
              'seleniumbase.core',
              'seleniumbase.plugins',
              'seleniumbase.fixtures',
              'seleniumbase.common',
              'seleniumbase.config'],
    entry_points={
        'nose.plugins': [
            'base_plugin = seleniumbase.plugins.base_plugin:Base',
            'selenium = seleniumbase.plugins.selenium_plugin:SeleniumBrowser',
            'page_source = seleniumbase.plugins.page_source:PageSource',
            'screen_shots = seleniumbase.plugins.screen_shots:ScreenShots',
            'test_info = seleniumbase.plugins.basic_test_info:BasicTestInfo',
            ('db_reporting = '
             'seleniumbase.plugins.db_reporting_plugin:DBReporting'),
            's3_logging = seleniumbase.plugins.s3_logging_plugin:S3Logging',
            ('hipchat_reporting = seleniumbase.plugins'
             '.hipchat_reporting_plugin:HipchatReporting'),
            ]
        }
    )