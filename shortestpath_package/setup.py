from setuptools import setup, find_packages

setup(
    name='shortestpath2200674010',
    version='0.1.0',
    author='Beyza Ören',
    author_email='beyzaoren58@hotmail.com',
    description='Dijkstra algorithm for shortest path calculation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/beyzoren/shortestpath_package.git',
    packages=find_packages(),
    install_requires=[
        'pytest'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
