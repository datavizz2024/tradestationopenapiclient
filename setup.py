from setuptools import setup, find_packages

setup(
    name='tradestationopenapiclient',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'urllib3',
        'pydantic',
    ],
)
