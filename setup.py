from setuptools import setup

setup(
    name='website',
    packages=['website'],
    include_package_data=True,
    install_requires=[
        'flask', 'flask-admin', 'flask-sqlalchemy', 'flask-login', 'flask-wtf', 'flask-bcrypt'
    ],
)