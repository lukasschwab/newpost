from setuptools import setup

setup (
    name = "newpost",
    version = "0.0.1",
    packages = ['newpost'],
    entry_points = {
        'console_scripts': [
            'post=newpost.__main__:main'
        ]
    }
)