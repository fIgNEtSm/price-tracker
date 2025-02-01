from importlib.metadata import entry_points

from setuptools import setup, find_packages

setup(
    name="amazon_price_tracker",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "sqlalchemy",
        "gunicorn",
        "flask_sqlalchemy"
    ],
)
