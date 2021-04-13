from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='c2d_api',
    version='0.0.2',
    description='Python package for API of Chat2Desk',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jkasemenov/c2d_api',
    author='Evgeniy Semenov',
    author_email='jkasemenov@mail.ru',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='chat2desk, chat, c2d',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7, <4',
    install_requires=['requests'],
)