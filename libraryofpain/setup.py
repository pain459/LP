from setuptools import find_packages, setup

setup(
    name='painlib',
    packages=find_packages(include=['painlib']),
    version='0.1.0',
    description='Library of Pain',
    author='pain',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)