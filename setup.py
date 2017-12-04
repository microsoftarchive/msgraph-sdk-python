from __future__ import with_statement
from setuptools import setup
from codecs import open
from os import path
import sys

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'src', 'msgraph', 'version.txt'), encoding='utf-8') as f:
    version = f.read()


def main():
    package_list = ['msgraph',
                    'msgraph.request',
                    'msgraph.model',
                    'msgraph.extensions']

    required_packages = ['requests>=2.6.1']

    if sys.version_info >= (3, 4):
        base_dir = 'python3'
    else:
        base_dir = 'python2'
        required_packages.append('enum>=0.4.6')


    setup(
        name='msgraph',

        version=version,

        description='Python SDK for the Microsoft Graph API [DEPRECATED]',
        long_description=long_description,

        url='http://graph.microsoft.io',

        author='Microsoft',
        author_email='',

        license='MIT',

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5',
            'Operating System :: OS Independent',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: MacOS :: MacOS X',
        ],

        keywords='msgraph msgraph sdk microsoft',

        packages=package_list,

        package_dir={'msgraph': path.join('src', 'msgraph'),
                     'msgraph.request': path.join('src', base_dir, 'request')},

        package_data={'msgraph': [r'version.txt']},

        install_requires=required_packages,

        extras_require={
            "samples": ["Pillow"],
            "tests": ["Mock"]
        },

        test_suite='test_graph_sdk'
    )

if __name__ == '__main__':
    main()
