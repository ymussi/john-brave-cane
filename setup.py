from setuptools import setup

with open("requirements.txt") as req:
    install_requires = req.read()

setup(name='john-brave-cane',
        version='0.0.1',
        description='',
        url='',
        author='Yuri Mussi',
        packages=['brave_cane'],
        zip_safe=False
),