from setuptools import setup, find_packages

setup(
    name='wezer',
    version='0.1.0',
    packages=find_packages('wezer'),
    package_dir={'': 'wezer'},
    entry_points={
        'console_scripts': [
            'wezer = wezer.cli:main',
        ],
    },
    install_requires=[
        'click',
        'colorama',
        'asciichart',
        'python-dotenv',
        'openmeteo-requests',
        'requests-cache',
        'retry-requests',
    ],
    author='kenjitheman',
    author_email='btwdesu@gmail.com',
    author_github='github.com/kenjitheman',
    description='CLI Weather App with colors and data visualization',
    url='https://github.com/kenjitheman/wezer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
