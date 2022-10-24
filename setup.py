from setuptools import setup, find_packages

setup(
    name="COVID19",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'joblib',
        'pyspark',
        'pandas'
    ],
    tests_require=[
        'unittest2',
        'pyhamcrest',
        'pytest'
    ],
    setup_requires=[
        'pytest-runner'
    ]
)