from io import open
from setuptools import setup

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hanzidentifier_preview',
    version='1.1.0',
    author='Thomas Roten',
    author_email='thomas@roten.us',
    url='https://github.com/tsroten/hanzidentifier',
    description=('Python module that identifies Chinese text as Simplified or '
                 'Traditional.'),
    long_description=long_description,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing :: Linguistic',
        ],
    keywords=['chinese', 'mandarin', 'hanzi', 'characters', 'simplified',
              'traditional', 'identify', 'identification', 'cjk'],
    py_modules=['hanzidentifier'],
    test_suite='tests',
    install_requires=['zhon>=1.1.3'],
)
