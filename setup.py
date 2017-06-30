from setuptools import setup

setup(
    name='maxxbook',
    packages=['maxxbook'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask_migrate'
    ],
)
