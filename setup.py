from setuptools import setup, find_packages


setup(
    name = "cnews",
    version = "0.0.1",
    packages = find_packages(),

    install_requires = [
        "beautifulsoup4==4.12.3",
        "lxml==5.2.1",
        "requests==2.31.0",
    ],

    entry_points = {
        "console_scripts": [
            "cnews = cnews:run",
        ],
    },
)